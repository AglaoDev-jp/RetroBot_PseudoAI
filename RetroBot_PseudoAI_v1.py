"""
Copyright © 2025 AglaoDev-jp

---

## 自作コンテンツのライセンス

- **コード**  
  Copyright © 2025 AglaoDev-jp  
  Licensed under the MIT License

- **画像**  
  Copyright © 2025 AglaoDev-jp  
  Licensed under CC BY 4.0  
  (Creative Commons Attribution 4.0 International)

- **コーパス（対話用データ）**  
  Copyright © 2025 AglaoDev-jp  
  Licensed under CC BY-SA 4.0  
  (Creative Commons Attribution-ShareAlike 4.0 International)

---

## 使用ライブラリとライセンス

以下のオープンソースライブラリを利用しています。ライセンスの全文はリポジトリ内の `LICENSES/` フォルダをご確認ください。

- **Tkinter**（GUI構築）  
  Copyright © Regents of the University of California, Sun Microsystems, Inc., Scriptics Corporation, and others  
  Licensed under the Tcl/Tk License  
  [詳細はこちら](https://www.tcl.tk/software/tcltk/license.html)

- **Janome**（日本語形態素解析）  
  Copyright © 2015–2025, Tomoko Uchida. All rights reserved.
  Licensed under the Apache License 2.0  
  ※ 本ライブラリには MeCab-IPADIC 辞書が含まれており、無保証の旨を含む通知が必要です。  
  NOTICE ファイルをご確認ください。

- **Gensim**（Word2Vec モデル）  
  Copyright © Radim Řehůřek and contributors  
  Licensed under GNU LGPL v2.1 or later  
  [LGPL v2.1 詳細](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)

- **scikit-learn**（コサイン類似度計算など）  
  Copyright (c) 2007-2024 The scikit-learn developers. All rights reserved. 
  Licensed under the BSD 3-Clause License  
  [BSD License 詳細](https://github.com/scikit-learn/scikit-learn/blob/main/COPYING)

- **NumPy**（数値演算）  
  Copyright © 2005–2025 NumPy Developers. All rights reserved.  
  Licensed under the BSD 3-Clause License  
  [NumPy License](https://github.com/numpy/numpy/blob/main/LICENSE.txt)

---

## 謝辞

本アプリケーションは、上記をはじめとした多数の素晴らしいオープンソースソフトウェアに支えられて開発されました。開発者・貢献者の皆様に深く感謝いたします。

本プロジェクトの開発、修正には、OpenAI の ChatGPT を利用しました。

"""

import tkinter as tk # GUI（グラフィカルユーザーインターフェイス）の作成に必要なモジュール
from tkinter import font # Tkinterのフォント変更やスタイル調整に使用。
from tkinter import messagebox  # Tkinterのダイアログボックスを利用するためのモジュール(corpus.jsonがない場合のメッセージを出力)
import json # JSON形式のファイル読み書きに利用
from pathlib import Path # ファイルパス操作を簡便にするためのモジュール
from janome.tokenizer import Tokenizer # 日本語の形態素解析（単語分割）に利用
from gensim.models import Word2Vec # 単語をベクトル化し、意味的な類似度計算を可能にするWord2Vecモデル
from sklearn.metrics.pairwise import cosine_similarity # 2つのベクトル間のコサイン類似度計算に利用
import numpy as np # 数値計算や配列操作のためのライブラリ
import random # 選択された入力から出力文をランダムに選ぶ
import sys # エラー発生時に `sys.exit()` による安全な終了(corpus.jsonがない場合のmessageboxを消す)PyInstallerでの凍結状態の判定。

# 実行ファイルと同じ場所にある corpus フォルダを探す
if getattr(sys, 'frozen', False):
    base_path = Path(sys.executable).parent  # .exe のある場所
else:
    base_path = Path(__file__).parent        # スクリプト実行時の場所

corpus_path = base_path / "corpus" / "corpus.json"

print(f"Looking for corpus at: {corpus_path}") # デバック用

if not corpus_path.exists():
    from tkinter import messagebox
    messagebox.showerror("エラー", f"corpus.json が見つかりませんでした。\n{corpus_path}")
    sys.exit(1)

# --- グローバル状態変数 ---
# ユーザが新しい要素（質問と返答ペア）を追加する際の状態を管理するための変数群

is_adding_mode = False   # 追加モードのON/OFF状態（Falseの場合は通常モード）
add_step = None          # 追加モード内での現在のステップを示す値（None, 'input', 'response', 'confirm' のいずれか）
temp_input = None        # 追加しようとしている質問を一時保存する変数
existing_entry = None    # 既に存在しているエントリと一致する場合、そのエントリを保持するための変数
temp_response = None     # 追加しようとしている返答を一時保存する変数
is_classic_mode = False  # フォント切り替え用ボタンとフラグ（Falseで初期状態はモダン）

# --- 形態素解析とコーパスの読み込み ---

# Janomeトークナイザのインスタンスを生成
tokenizer = Tokenizer() 
def tokenize(text): # 文章 → 単語リスト
    """
    文章（text）を形態素解析により単語リストに変換する。
    :param text: 入力の文章（文字列）
    :return: トークン化された単語のリスト（各単語は token.surface として取り出す）
    """
    return [token.surface for token in tokenizer.tokenize(text)]
# corpus.json を読み込み、JSONオブジェクト（基本的には辞書やリスト）としてパースする
with corpus_path.open(encoding="utf-8") as f:
    corpus = json.load(f)

# --- Word2Vec モデルの準備 ---
# 各エントリ（質問）のテキストをトークナイズし、Word2Vecの学習用データとする
# この部分では「自然言語（日本語）を機械が理解しやすい数値（ベクトル）に変換する処理」を行っています。

sentences = []  # 学習用の文章リスト（各文章はトークンのリスト）例： [['今日', 'は', 'いい', '天気'], ['明日', 'も', '晴れる']]）
for item in corpus:
    # 各エントリの "input" 部分はリストか単一の文字列かの場合があるので、統一的にリストに変換
    inputs = item["input"] if isinstance(item["input"], list) else [item["input"]]
    for text in inputs:
        # 各テキストを形態素解析してトークンのリストに変換し、学習用データに追加する
        sentences.append(tokenize(text))
    """
    🌱 ここでやってること
        1.コーパス（例文集） の各入力文を取り出す
        2.tokenize(text) によって形態素解析（単語の分解）を行う
        3.その結果（単語のリスト）を sentences に追加していく
    """
# --- Word2Vecモデルの生成 --- 
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1) # 単語 → 数値ベクトル
"""
・vector_size: 生成される単語ベクトルの次元 ハイパーパラメータ（hyperparameters）
（ここでは100次元、数字が大きいほど細かい意味の違いを表現できるが、学習に時間がかかる、過学習（覚えすぎ）しやすい、ノイズも増えるらしい😵）
・window: 前後何語をコンテキストとして考慮するか（ここでは5語、何語までの関係を学習に使うか？）
・min_count: 単語が登場する最小回数（1なら全ての単語）  
"""

def sentence_vector(tokens): # 単語の集合 → 文ベクトル
    """
    単語のリスト（tokens）から、各単語のWord2Vecベクトルの平均を計算し、
    文章全体のベクトル表現を生成する。
    :param tokens: 単語のリスト
    :return: 単語ベクトルの平均（numpy配列）。該当単語がない場合は0ベクトルを返す。
    文章を「単語ごとのベクトル」に分解し、それらの平均値を取ることで、文章全体の意味を表すベクトルを作る関数です。
    """
    # モデルに存在する単語のみベクトルを抽出
    vectors = [model.wv[word] for word in tokens if word in model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)

def get_best_response(user_input):
    """
    ユーザの入力テキストに対して、コーパス中の各エントリの入力文と
    コサイン類似度を計算し、最も類似したエントリの応答を返す。
    :param user_input: ユーザが入力した文章
    :return: 類似度が最も高かったエントリの返答文（なければ既定のエラーメッセージ）
    """
    # ユーザ入力を形態素解析し、トークンリストに変換
    input_tokens = tokenize(user_input)
    # ユーザ入力の文ベクトルを計算
    input_vec = sentence_vector(input_tokens)
    best_score = -1 # 現在の最高類似度の初期値
    best_response = "申し訳ありません。該当の応答が見つかりませんでした。"  # 該当エントリがない場合のデフォルト返答(一応)
    # コーパス中の各エントリについてループ処理
    for item in corpus:
        # エントリ内の "input" 部分をリスト形式に統一する
        input_list = item["input"] if isinstance(item["input"], list) else [item["input"]]
        max_score = -1 # そのエントリ内での最高類似度を初期化。ここ改善点かな？👷
        for text in input_list:
            # 各入力文をトークン化し、文ベクトルに変換
            tokens = tokenize(text)
            vec = sentence_vector(tokens)
            # ユーザ入力とのコサイン類似度を計算
            # これは、「ユーザーの入力ベクトル」と「コーパス内の入力ベクトル」の角度の近さ（＝意味の近さ）を計算しています。
            score = cosine_similarity([input_vec], [vec])[0][0]
            if score > max_score:
                max_score = score  # エントリ内の最高類似度を更新

        # エントリごとの最高類似度がグローバルな最高値より大きければ更新する
        if max_score > best_score:
            best_score = max_score
            # 複数の返答パターンがある場合はランダムに1つ選択、なければ単一の返答を使用
            best_response = random.choice(item["responses"]) if "responses" in item else item["response"]
    return best_response

"""
 --- cosine_similarity（コサイン類似度）とは？ ---
 cosine_similarity は、「ベクトルの向きの近さ（＝角度の小ささ）」を測る方法です。

 📐 イメージ（図は頭で思い浮かべてね）：
   ベクトル A：→→→（例えば「こんにちは」）
   ベクトル B：↗↗↗（例えば「おはよう」）
   この2つのベクトルのなす角θが小さいほど、コサイン類似度は「1」に近くなります。

   θ（角度）     類似度
   0°            1.0（完全に同じ方向）
   90°           0.0（完全に無関係）
   180°         -1.0（正反対：自然言語ではまず出ない）

 🧮 数式で書くとこうなります（※気になる人向け）：
   cos(θ) = (A・B) / (||A|| * ||B||)
   ・A・B は「内積（ドット積）」
   ・||A|| は A の「長さ（ノルム）」 → √(a1^2 + a2^2 + ... + an^2)
   ・cos(θ) が「コサイン類似度」そのもの

"""

# --- メッセージ送信やその他の関数群 ---
def send_message(event=None):
    """
    ユーザのメッセージ送信時に呼び出されるイベントハンドラ。
    追加モードと通常モードの両方で動作し、各種制御（応答生成、モード切替、終了コマンドの処理）を行う。
    """
    global entry, chat_log, is_adding_mode, add_step, temp_input, temp_response, existing_entry
    # ユーザ入力を取得して前後の空白を除去
    user_input = entry.get().strip()
    if not user_input:
        return "break" # 空の入力では何もせず終了
    entry.delete(0, tk.END) # 入力欄をクリア

    # 追加モードがONの際、"やめる"と入力されたら追加モードを終了する
    if user_input.lower() == "やめる" and is_adding_mode: 
        toggle_add_mode()
        return "break"
    
    # チャットログにユーザの入力を表示
    chat_log.config(state="normal")
    chat_log.insert(tk.END, f"あなた: {user_input}\n")

    # "exit" コマンドでプログラムのシャットダウン処理を実行
    if user_input.lower() == "exit":
        shutdown_sequence()
        return "break"
    
    # 追加モードの処理（新規質問・返答の追加）
    if is_adding_mode:
        if add_step == "input":
            # 追加モード：質問入力段階
            # 既存のエントリと重複がないか確認する
            for item in corpus:
                inputs = item["input"] if isinstance(item["input"], list) else [item["input"]]
                if user_input in inputs:
                    append_to_log("AI: その質問はすでに登録されています。他の表現を試してください。\n")
                    return "break"
                elif user_input in inputs:
                    # ここは重複検出のための処理（実質上、上の条件と同じ処理になっている）
                    existing_entry = item

            # 重複がなければ、ユーザの質問を一時保存して次のステップへ        
            temp_input = user_input # 一時保存
            add_step = "response" # 次は返答入力段階へ
            append_to_log("AI: では、この質問に対する返答を入力してください。\n")
            return "break"
        
        elif add_step == "response":
            # 追加モード：返答入力段階
            # 他のエントリで同じ返答が使われていないかをチェックする
            if any(user_input == r for item in corpus for r in item.get("responses", [])):
                append_to_log("AI: その返答はすでにどこかで使われています。他の表現を試してください。\n")
                return "break"
            
            # 重複しなければ、返答を一時保存し確認のステップへ進む
            temp_response = user_input # 一時保存
            add_step = "confirm" # 確認へ
            append_to_log("AI: 以下の内容を保存しますか？（はい / いいえ）\n")
            append_to_log(f"質問: {temp_input}\n返答: {temp_response}\n")
            return "break"
        
        elif add_step == "confirm":
            # 追加モード：確認段階
            if user_input.lower() == "はい":
                # ユーザが「はい」と答えた場合、既存エントリがあるなら質問を追加し、
                # 無ければ新規エントリとして質問と返答のペアを登録する
                if existing_entry:
                    existing_entry["input"].append(temp_input)
                else:
                    corpus.append({"input": [temp_input], "responses": [temp_response]})
                # 変更をJSONファイルに保存する
                with corpus_path.open("w", encoding="utf-8") as f:
                    json.dump(corpus, f, indent=2, ensure_ascii=False)
                append_to_log("AI: 記憶しました。ありがとうございます。\n")
                toggle_add_mode() # 追加モードを終了
                
            elif user_input.lower() == "いいえ":
                # いいえ → 保存をキャンセルして最初から質問入力へ
                append_to_log("AI: 保存をキャンセルしました。もう一度最初からお願いします。\n")
                add_step = "input"
            else:
                # その他の入力 → 確認ステップを繰り返す
                append_to_log("AI: すみません。「はい」か「いいえ」でお答えください。\n")
                append_to_log("以下の内容をもう一度ご確認ください：\n")
                append_to_log(f"質問: {temp_input}\n返答: {temp_response}\n")
                # add_step はそのまま "confirm" にしておく
            return "break"
        
    # 追加モードに該当しない場合、通常の応答生成処理を行う
    response = get_best_response(user_input)
    entry.config(state="disabled") # 応答生成中は入力欄を一時的に無効化
    type_response(response) # タイピング風に応答を表示
    chat_log.see(tk.END) # 最新メッセージまでスクロール
    entry.focus_set() # 入力欄にフォーカスを戻す
    return "break"

def type_response(text, index=0):
    """
    タイピング風に1文字ずつAIの応答を表示する関数です。
    :param text: 表示すべきテキスト（応答）
    :param index: 現在表示中の文字位置
    """
    if index == 0:
        # 最初に"AI:"ラベルを表示
        chat_log.config(state="normal")
        chat_log.insert(tk.END, "AI: ")

    if index < len(text):
        # 現在の文字を表示し、次の文字表示を30ミリ秒後にスケジュールする
        chat_log.insert(tk.END, text[index])
        chat_log.see(tk.END)
        root.after(30, type_response, text, index + 1)
    else:
        # 全ての文字を出力した後、改行と入力欄の再有効化を行う
        chat_log.insert(tk.END, "\n\n")
        chat_log.config(state="disabled")
        entry.config(state="normal")
        entry.focus_set()

def startup_sequence():
    """
    起動時の演出として、システム情報や起動メッセージを段階的に表示する関数です。
    統計情報の表示とその後の起動メッセージ、最終的に入力欄を有効化します。
    """
    # システムの統計情報（現在登録されているデータなど）を表示するメッセージリスト
    stats = [
        f"== AI データ情報 ==",
        f"記憶している入力数: {len(corpus)}",
        f"返答パターン数: {sum(len(entry['responses']) if 'responses' in entry else 1 for entry in corpus)}",
        f"データ要素の合計: {len(corpus) + sum(len(entry['responses']) if 'responses' in entry else 1 for entry in corpus)}",
        "" # ← 視認性を上げるための空行
    ]
    # 起動時に表示するその他のメッセージリスト
    messages = [
        "AI: システムチェック中……",
        "AI: モジュールロード完了",
        "AI: 起動成功。ようこそ。"
    ]
    delay = 1000    # 各メッセージ間の基本待機時間（ミリ秒単位、ここでは1秒）
    total_delay = 0 # 各メッセージ表示の累計遅延時間

    # 統計情報を短い間隔で表示
    for line in stats:
        root.after(total_delay, lambda m=line: append_to_log(m))
        total_delay += 200

    # 起動メッセージを1秒間隔で表示
    for msg in messages:
        root.after(total_delay, lambda m=msg: append_to_log(m))
        total_delay += delay

    # 全メッセージ表示後、入力欄を有効化する
    root.after(total_delay, enable_input)

def enable_input():
    """
    起動シーケンスの最後に呼ばれ、チャットログに入力促進のメッセージを追加し、
    入力欄をアクティブにするための関数
    """
    chat_log.config(state="normal")
    chat_log.insert(tk.END, "\n▼ メッセージを入力してください ▼\n\n")
    chat_log.config(state="disabled")
    entry.config(state="normal")
    entry.focus_set()

def shutdown_sequence():
    """
    "exit" コマンドが入力された際に呼ばれ、レトロ風のシャットダウンメッセージを順次表示後、
    アプリケーションを終了する関数
    """
    messages = [
        "AI: シャットダウンシーケンスを開始します……",
        "AI: セッションログを保存中……完了",
        "AI: システムを終了します。おつかれさまでした。"
    ]
    delay = 1000 # 各メッセージの表示間隔（1秒）
    total_delay = 0

    # 各シャットダウンメッセージを順次表示
    for msg in messages:
        root.after(total_delay, lambda m=msg: append_to_log(m))
        total_delay += delay

    # 最終メッセージ表示後1秒でアプリケーション終了
    root.after(total_delay + 1000, root.destroy)

def append_to_log(message):
    """
    指定されたメッセージをチャットログに追加し、最新のメッセージが画面に表示されるようにする補助関数
    :param message: 追加するメッセージ（文字列）
    """
    chat_log.config(state="normal")
    chat_log.insert(tk.END, message + "\n")
    chat_log.config(state="disabled")
    chat_log.see(tk.END) # チャットログを最新行にスクロール

def toggle_add_mode():
    """
    追加モードをオンまたはオフに切り替える関数。
    追加モードオンでユーザが新しい質問・返答ペアをシステムに学習できるようにします。
    """
    global is_adding_mode, add_step, temp_input, temp_response, existing_entry
    if is_adding_mode:
        # 追加モードから通常モードに切り替える際は、
        # すべての一時変数をリセットし、モードボタンの表示と背景色を更新
        is_adding_mode = False
        add_step = None
        temp_input = None
        temp_response = None
        existing_entry = None
        mode_button.config(text="追加モード：OFF", bg="lightgray")
        append_to_log("AI: 要素追加モードを終了しました。記憶はキャンセルされました。\n")
    else:
        # 追加モードを開始。初期設定を行い、ユーザに質問の入力を促す。
        is_adding_mode = True
        add_step = "input"
        temp_input = None
        temp_response = None
        existing_entry = None
        mode_button.config(text="追加モード：ON", bg="lightyellow")
        append_to_log("AI: 要素追加モードを開始します。覚えさせたい質問を入力してください。\n")

# --- toggle_font_style の定義 ---
def toggle_font_style():
    global is_classic_mode
    if is_classic_mode:
        # モダンフォント
        new_font = ("Yu Gothic", 11)
        chat_log.config(font=new_font, bg="white", fg="black")
        entry.config(font=new_font, bg="white", fg="black", insertbackground="black")
        label.config(font=new_font)
        send_button.config(font=new_font)
        font_button.config(text="フォント: クラシック") # 逆のほうがいいのかな？
    else:
        # クラシックフォント
        new_font = ("Consolas", 11)
        chat_log.config(font=new_font, bg="black", fg="lime")
        entry.config(font=new_font, bg="black", fg="white", insertbackground="white")
        label.config(font=new_font)
        send_button.config(font=new_font)
        font_button.config(text="フォント: モダン")
    is_classic_mode = not is_classic_mode

# --- GUI（Tkinter）の設定 ---
root = tk.Tk()
root.title("旧式風 AI チャット")
root.geometry("500x600")
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Meiryo", size=9)

chat_font = ("Yu Gothic", 11)
chat_bg = "white"
chat_fg = "black"
entry_font = ("Yu Gothic", 11)
entry_bg = "white"
entry_fg = "black"
entry_cursor = "black"

# ボタンを配置するフレームを作成
button_frame = tk.Frame(root)
button_frame.pack(pady=(0, 5))

mode_button = tk.Button(button_frame, text="追加モード：OFF", bg="lightgray", command=toggle_add_mode)
mode_button.pack(side=tk.LEFT, padx=5)

# フォント切り替えボタンを作成
font_button = tk.Button(button_frame, text="フォント: クラシック", command=toggle_font_style)
font_button.pack(side=tk.LEFT, padx=5)

# チャットログ表示領域（読み取り専用）を作成
chat_log = tk.Text(root, font=chat_font, bg=chat_bg, fg=chat_fg)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# アプリ起動時の初期メッセージをチャットログに挿入する
chat_log.config(state="normal")
chat_log.insert(tk.END, "AI起動しました。\n終了するには、`exit` と入力してください。\n\n")
chat_log.config(state="disabled")

# 入力欄のラベルを作成して配置
label = tk.Label(root, text="▼ メッセージを入力してください ▼")
label.pack()

# ユーザからのメッセージ入力用のエントリ（入力フィールド）を作成
entry = tk.Entry(root, font=entry_font, bg=entry_bg, fg=entry_fg, insertbackground=entry_cursor)
entry.pack(padx=10, pady=(0, 10), fill=tk.X)
entry.bind("<Return>", send_message) # Enterキーが押されたときに send_message 関数を実行

# 送信ボタンを作成し、クリック時の動作として send_message を設定
send_button = tk.Button(root, text="送信", command=send_message)
send_button.pack(pady=(0, 10))

# 初期フォーカスを入力欄に設定し、起動シーケンスが終わるまで一時的に入力を無効にしておく
entry.focus_set()
entry.config(state="disabled")
startup_sequence() # 起動演出を開始する（統計情報や起動メッセージの表示）
root.mainloop() # Tkinterのイベントループを開始してGUIを表示
