
# 旧式”風”チャットボットv1 🤖あそびかた😊
“It thinks like an AI. Acts like an AI. But deep down… it's just RetroBot (PseudoAI).”
  
コード作成、テキスト作成、アイコン作成、コーパス作成、翻訳にChatGPTを使用しています。  

---

本プロジェクトの制作にあたり、OpenAIの対話型AI「ChatGPT」のサポートを受けて、画像生成、アイデア出し、コード修正、文章の表現の改善、翻訳などをスムーズに行うことができました。開発に携わったすべての研究者、開発者、関係者の皆様に、心より感謝申し上げます。    

---

## 実行ファイルのセキュリティに関する注意事項
本アプリケーションは、**悪意のあるコード（ウイルス・マルウェア）は含まれていません。**  
しかし、一部のアンチウイルスソフトにより、**誤検出**されることがあります。  

### ** 誤検出が起こる理由**
- **圧縮やパッキング処理を行っていること**
- **デジタル署名がないこと**

これらの要因により、一部のウイルス対策ソフトが誤って「疑わしい」と判断することがあります。  

### **安全性を確認する方法**
本アプリケーションが安全かどうかを確認する場合は、以下の方法を推奨します：
- **[VirusTotal](https://www.virustotal.com/)にアップロードし、スキャン結果を確認する** 
- **仮想環境（VirtualBox, Windows Sandbox など）で実行してみる**
- **公式の配布元（GitHub）からダウンロードする**

### **※誤検出が気になる場合や、安全性に不安がある場合は、ダウンロードや実行を控えてください。**

---

## 免責事項
- 本アプリケーションの利用や環境設定に起因するいかなる損害や不具合について、作者は一切の責任を負いません。  
- **本プロジェクトで作成・使用しているコーパスを直接的な機械学習（ファインチューニング・リファインメント学習等）に使用することを固く禁止します。**  
---

**製作期間**

- **v1**: 2025年4月10日 ~ 2025年4月19日  

---

## 🤖 はじめに  

このアプリは、少しとぼけたところのある旧式チャットボットです。  
うまく噛み合わないこともあるかもしれませんが、のんびりと会話を楽しんでいただけたら嬉しいです。  

---

## 💬 基本操作  

1. アプリを起動すると、中央の画面にメッセージログが表示されます。  
2. 下部の入力欄に話しかけたい内容を入力して、`Enterキー` または `送信ボタン` を押します。  
3. AIがゆっくりと返事をしてくれます。  
4. 「exit」と入力すると終了します。  

---

## 🔁 モード切り替え

### ✍️ 追加モード（記憶させる）

- ボタン「追加モード：OFF」をクリックすると、**質問・返答のペアを新しく記憶させるモード**になります。  
- 手順にそって入力すると、AIの返答パターンが増えていきます。  

🪧 キーワード：「やめる」  
→ 入力中にやめたくなったら、`やめる`と打つと追加モードを終了できます。

### 🎨 フォント切り替え

- フォントボタンを押すと、文字・背景が切り替わります。
- お好みの表示スタイルでお楽しみください。

---

## 💉 注意
- 起動には少し時間がかかります。起動時に解析モデル（Word2Vec）の学習を行うため、環境によっては数秒〜十数秒ほど待機時間があります。  
- 起動や終了の動作には**演出（セリフ）**が含まれています。
- 入力によっては適切な返答ができず、ピントのずれた返事をしてしまうことがあります。  
その場合は、表現を変えてみたり、少し言い方を工夫してみてください。

---

## 📁 コーパスについて

- アプリは `corpus.json` というファイルを使用して、入力と返答のセットを記憶しています。
- このファイルは **テキストエディタで直接編集・追記することも可能**です（UTF-8形式）。  
好きなように書き換えてオリジナルのチャットボットを作成することもできます。
- 直接編集する際には、JSON形式の構造を崩さないよう注意してください。
- `corpus.json`は、必ず`corpus フォルダ`内に入れてください。

### 📄 コーパスのライセンスについて  

- 本アプリケーションに同梱されているコーパス（`corpus.json`）は、**Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** ライセンスのもとで提供されています。  
- 再配布や改変を行う際には、**著作権者クレジット（例：「Corpus by AglaoDev-jp © 2025」）を明記し、改変後も同じCC BY-SA 4.0ライセンスを適用**していただくことを推奨します。
- ただし、**ご自身で新たにすべてオリジナルでコーパスを作成された場合**には、このライセンス条件には縛られません。自由にご利用いただけます。  
必要に応じて独自のライセンスを設定することも可能です。  
- **改変を行う際、その内容に関する責任は作成者様ご自身に帰属します。不適切な表現、誤情報、権利侵害などがないようご配慮ください。**

---

## 🔍 本プロジェクトにおけるコーパスと学習方法について

本プロジェクトでは、チャットボット応答システムの構築にあたり、以下の技術・方法を使用しています。

- 形態素解析（日本語テキストの単語分割）
- Word2Vec（単語や文章の意味を数値ベクトルに変換）
- 意味ベクトル同士の類似度計算による応答選択

これらの技術は、テキスト内容を直接保存・再現するものではなく、  
単語や文章間の意味関係を統計的に学習するものです。

つまり**リファインメント学習（Reinforcement Fine-Tuning）**や
**ファインチューニング（Fine-tuning）**は行っておりません。

---

## 📚 コーパスの作成と利用について

本プロジェクトで使用しているコーパス（対話データ）は、  
対話型AI「ChatGPT」の支援を受けて作成したオリジナルコンテンツです。  
コーパスの著作権は作成者に帰属し、自由な使用・改変・再配布が可能です。

`Word2Vec`による学習処理は、テキスト内容を数値的な特徴量に変換するものであり、  
元の文章を再現・複製するものではありません。  
したがって、OpenAIの利用規約、著作権ポリシー、倫理指針に抵触しない形で運用されています。

---

## ✅ 安心してご利用いただくために

本アプリケーションは以下を遵守しています。

- **ChatGPT出力物の利用ポリシー**（利用者への権利帰属）
- **機械学習による二次生成禁止ルールの非該当**（本アプリは生成型AIではありません）
- **元データの個別再現リスクの回避**（数値変換にとどまる学習方式）
  
これにより、  
**利用者様がアプリを使用することによって、規約違反や権利侵害が発生することはありません。**

安心してお楽しみいただければ幸いです。

## ⚠️ コーパスの二次利用について
- **本プロジェクトで作成・使用しているコーパスを直接的な機械学習（ファインチューニング・リファインメント学習等）に使用することを固く禁止します。**
これは、OpenAIの利用規約においても、ChatGPT等の出力物を用いたモデル再学習が原則禁止されていることに基づいています。
万一、本コーパスを許可なく機械学習に利用した場合、
OpenAIのポリシー違反、ならびに著作権侵害に該当する可能性がありますので、十分ご注意ください。

---

## 🧯 その他

- 起動や終了の動作は**演出**です。ウィンドウを途中で閉じても、アプリやデータが壊れることはありません。
- 保存は自動的に行われますが、追加モードで「はい」と答えるまでは保存されません。

---

## 📘 使用言語とライブラリ

### 使用言語
- **Python 3.12.5**

### 使用モジュール・ライブラリ

#### 🏛 標準モジュール

- **tkinter** – GUI（グラフィカルユーザーインターフェイス）を構築するために使用。
- **tkinter.font** – GUI部品のフォント変更やスタイル調整に使用。
- **tkinter.messagebox** – ファイル読み込みエラー時に警告ダイアログを表示。
- **json** – 対話コーパス（corpus.json）の読み書きに使用。
- **pathlib** – ファイル存在確認や読み書きに使用。
- **sys** – エラー発生時に `sys.exit()` による安全な終了。PyInstallerでの凍結状態の判定。
- **random** – コーパス内の返答候補からランダムで選択するために使用。

#### 📦 外部ライブラリ

- **Janome** – 日本語の形態素解析を行うために使用。ユーザーの入力や発話を単語ごとに分割。
- **Gensim (Word2Vec)** – 単語をベクトル化し、意味の近さを数値で表現。ユーザー入力と既存入力の類似度計算に使用。
- **scikit-learn（cosine_similarity）** – ベクトル間のコサイン類似度を計算し、最も近い質問を選出。(Gensimインストール時に同時にインストール)
- **NumPy** – ベクトルの平均計算、ゼロベクトル生成など、数値演算を支えるライブラリ。(Gensimインストール時に同時にインストール)

### 実行ファイル化
- **PyInstaller** – PythonスクリプトをWindows用の単一実行ファイル（.exe）に変換するために使用。

### 使用エディター
- **Visual Studio Code (VSC)** – スクリプトの作成、整形、デバッグなど開発全般に使用。

---

### 著作権表示とライセンスについて

## 📂 ライセンスファイルまとめ[licenses](./licenses/)
- Python [LICENSE-PSF.txt](./licenses/LICENSE-PSF.txt)
- Tkinter [Tcl/Tk License](./licenses/third_party/LICENSE-TclTk.txt)
- Janome(License) [Apache License 2.0](./licenses/third_party/LICENSE_Janome.txt)
- Janome(NOTICE) [NOTICE_Janome](./licenses/third_party/NOTICE_Janome.txt)
- Gensim [LGPLv2.1+](./licenses/third_party/LICENSE_Gensim.txt)
- scikit-learn [BSD 3-Clause License](./licenses/third_party/LICENSE_ScikitLearn.txt)
- SciPy [BSD 3-Clause License](./licenses/third_party/LICENSE_SciPy.txt)
- SciPy(Bundled) [LICENSES_SciPy_Bundled](./licenses/third_party/LICENSES_SciPy_Bundled.txt)
- NumPy [NumPy License](./licenses/third_party/LICENSE_NumPy.txt)
- NumPy(Bundled) [LICENSES_NumPy_Bundled](./licenses/third_party/LICENSES_NumPy_Bundled.txt) 
- OpenBLAS [BSD 3-Clause License](./licenses/third_party/LICENSE_OpenBLAS.txt) 
- PyInstaller [GNU GPL v2 or later（例外付き）](./licenses/third_party/LICENSE_PyInstaller.txt)

### **Python**  
- © Python Software Foundation  
Licensed under the Python Software Foundation License (PSF License).  
[Python license](https://docs.python.org/3/license.html)  

#### **Tkinter**  
- © Regents of the University of California, Sun Microsystems, Inc., Scriptics Corporation, and other parties  
TkinterはPythonに含まれるGUIライブラリですが、その動作にはTcl/Tkが使用されています。  
- [Tcl/Tk License](https://www.tcl.tk/software/tcltk/license.html)  

---

### 使用ライブラリとライセンス

### 📚 Janome（日本語形態素解析器）

> 本アプリケーションでは、ユーザー入力文、出力文の解析に使用しています。

- **ライセンス**：Apache License 2.0  
- **著作権表示**：© 2015–2025, Tomoko Uchida. All rights reserved.
- **GitHub**：[https://github.com/mocobeta/janome](https://github.com/mocobeta/janome)

- **NOTICE**：Janome には、形態素解析に使用される **MeCab-IPADIC 辞書データ** が含まれており、  
 その辞書に関する以下の注意事項（再配布条件）を満たす必要があります：
 - **この辞書は「無保証（NO WARRANTY）」のもと配布されています。**  

※ 詳細は本リポジトリ内[NOTICE_Janome.txt](./licenses/third_party/NOTICE_Janome.txt)をご確認ください。  

---

### 🧠 Gensim

> 自然言語処理や文書ベクトル化のために **Gensim** ライブラリを使用しています。

- **ライセンス**：LGPLv2.1+（GNU Lesser General Public License）  
- **著作権表示**：Copyright © Radim Řehůřek and contributors  
- **公式サイト**：[https://radimrehurek.com/gensim/](https://radimrehurek.com/gensim/)  
- **GitHub**：[https://github.com/RaRe-Technologies/gensim](https://github.com/RaRe-Technologies/gensim)
- **ライセンス全文**： [Gensim GitHubリポジトリのLICENSEファイル](https://github.com/RaRe-Technologies/gensim/blob/develop/LICENSE)  

---

### ⚙️ scikit-learn
> 主にベクトル間の距離計算に使用しています。
- **ライセンス**：BSD 3-Clause License  
- **著作権表示**：Copyright (c) 2007-2024 The scikit-learn developers. All rights reserved.  
- **公式サイト**：[https://scikit-learn.org/](https://scikit-learn.org/)  
- **ライセンス全文**：[https://github.com/scikit-learn/scikit-learn/blob/main/COPYING](https://github.com/scikit-learn/scikit-learn/blob/main/COPYING)

---

### 🔢 NumPy

> 数値計算処理の基盤として **NumPy** を使用しています。   

- **ライセンス**：BSD 3-Clause License（通称："NumPy License"）  
- **著作権表示**：© 2005–2025 NumPy Developers. All rights reserved.  
- **ライセンス原文**：[https://github.com/numpy/numpy/blob/main/LICENSE.txt](https://github.com/numpy/numpy/blob/main/LICENSE.txt)  
- **公式サイト**：[https://numpy.org](https://numpy.org)  
- **GitHub**：[https://github.com/numpy/numpy](https://github.com/numpy/numpy)

---

# 📐 SciPy（数値計算と科学技術計算ライブラリ）
 
> 本アプリケーションでは、コサイン類似度計算や内部数値処理の一部において使用しています。

- **ライセンス**：BSD 3-Clause License  
- **著作権表示**：Copyright (c) 2001-2002 Enthought, Inc. 2003, SciPy Developers. All rights reserved. 
- **公式サイト**：[https://scipy.org/](https://scipy.org/)  
- **GitHub**：[https://github.com/scipy/scipy](https://github.com/scipy/scipy)

---

### ⚙️ OpenBLAS（数値計算高速化用ライブラリ）

>NumPyおよびSciPyが内部的に利用する、オープンソースのBLAS（Basic Linear Algebra Subprograms）実装ライブラリです。  
>本アプリケーションを PyInstaller により実行ファイル化した際に、  
>OpenBLAS のDLLファイルが自動的に組み込まれていることを確認しています。

- **ライセンス**：BSD 3-Clause License  
- **著作権表示**：Copyright (c) 2011-2014, The OpenBLAS Project All rights reserved.
- **公式サイト**：[https://www.openblas.net/](https://www.openblas.net/)  
- **GitHub**：[https://github.com/xianyi/OpenBLAS](https://github.com/xianyi/OpenBLAS)

---

#### 📦 PyInstaller
  
> PyInstaller は GNU GPL ライセンスですが、例外規定により  
> **生成される実行ファイル自体は GPL の制約を受けません**。

- **著作権表示：**  
  ```
  Copyright (c) 2010–2023, PyInstaller Development Team  
  Copyright (c) 2005–2009, Giovanni Bajo  
  Based on previous work under copyright (c) 2002 McMillan Enterprises, Inc.
  ```

#### ⚖️ PyInstaller のライセンス構成について

PyInstaller は以下のように**複数のライセンス形態**で構成されています：

- 🔹 **GNU GPL v2 or later（例外付き）**  
  本体およびブートローダに適用されます。  
  → **生成された実行ファイルは任意のライセンスで配布可能**です（依存ライブラリに従う限り）。

- 🔹 **Apache License 2.0**  
  ランタイムフック（`./PyInstaller/hooks/rthooks/`）に適用されています。  
  → 他プロジェクトとの連携や再利用を意識した柔軟なライセンス。

- 🔹 **MIT License**  
  一部のサブモジュール（`PyInstaller.isolated/`）およびそのテストコードに適用。  
  → 再利用を目的としたサブパッケージに限定適用されています。

####  詳細情報へのリンク

- [PyInstallerのライセンス文書（GitHub）](https://github.com/pyinstaller/pyinstaller/blob/develop/COPYING.txt)  
- [PyInstaller公式サイト](https://pyinstaller.org/en/v6.13.0/index.html)  

---

## フォントについて

- 本アプリケーションでは、PC内の `Meiryo` 、 `Yu Gothic` 、 `Consolas` を参照する形で記述しています。プロジェクト内にフォントファイルは存在しません。  
- 環境によっては正しく文字が表示されない場合があります。  

---

これらのプロジェクトの開発者および貢献者の皆様に、心より感謝申し上げます。

---

## このアプリケーションのライセンス

- **このアプリケーションのコード**: MIT License。詳細は[LICENSE-CODE](./licenses/application/LICENSE-CODE)ファイルを参照してください。
- **画像**: Creative Commons Attribution 4.0 (CC BY 4.0)。詳細は[LICENSE-IMAGES](./licenses/application/LICENSE-IMAGES)ファイルを参照してください。
- **コーパス**: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)詳細は[LICENSE-IMAGES](./licenses/application/LICENSE-IMAGES)ファイルを参照してください。  

## ライセンスの簡単な説明

- **このアプリケーションのコード**: （MIT License）
このアプリケーションのコードは、MITライセンスのもとで提供されています。自由に使用、改変、配布が可能ですが、著作権表示とライセンスの文言を含める必要があります。

- **画像**: （Creative Commons Attribution 4.0, CC BY 4.0）
このアプリケーションの画像は、CC BY 4.0ライセンスのもとで提供されています。自由に使用、改変、配布が可能ですが、著作権者のクレジットを表示する必要があります。

- **コーパス**:（Creative Commons Attribution-ShareAlike 4.0, CC BY-SA 4.0）
このアプリケーションのコーパスの`対話データ`は、CC BY-SA 4.0ライセンスのもとで提供されています。自由に使用、改変、配布が可能ですが、著作権者のクレジットを表示し、改変後も同じライセンス条件を適用する必要があります。 

※これらの説明はライセンスの概要です。詳細な内容は各ライセンスの原文に準じます。  

---

## クレジット表示のテンプレート（例）  

### コード
```plaintext
Code by AglaoDev-jp © 2025, licensed under the MIT License.
```

### 画像
```plaintext
Image by AglaoDev-jp © 2025, licensed under CC BY 4.0.
```

### コーパス
```plaintext
Corpus by AglaoDev-jp © 2025, licensed under CC BY-SA 4.0.
```

---

#### ライセンスの理由
現在のAI生成コンテンツの状況を踏まえ、私は本作品を可能な限りオープンなライセンス設定になるように心がけました。  
問題がある場合、状況に応じてライセンスを適切に見直す予定です。  

このライセンス設定は、権利の独占を目的とするものではありません。明確なライセンスを設定することにより、パブリックドメイン化するリスクを避けつつ、自由な利用ができるように期待するものです。  
  
© 2025 AglaoDev-jp

