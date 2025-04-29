
---

# 旧式”風”チャットボットv1
“It thinks like an AI. Acts like an AI. But deep down… it's just RetroBot (PseudoAI).”
  
コード作成、画像作成、コーパス作成、テキスト作成、翻訳にChatGPTを使用しています。  
このリポジトリでは、アプリケーションの**ソースコード**を公開しています。  
チャットボットのファイル(実行ファイル)のダウンロードは[こちら](https://github.com/AglaoDev-jp/RetroBot_PseudoAI/releases/download/RetroBot_PseudoAI_v1/RetroBot_PseudoAI_v1.zip)  
チャットボットのあそびかたは[こちら](./README_PLAY.md)  

---

※ このリポジトリは個人学習のために使用しています。そのため、プルリクエスト（Pull Request）は、お受けすることができません。ご了承ください。  

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

- **v1**: 2025年4月10日 ~ 2025年4月29日

---

## 📘 このアプリケーションについて
本アプリケーションは、GUI上で稼働する“チャットボット”です。  
（AI研究に使われる機械学習ライブラリを使用していますが、分類上は対話型ゲーム・人工無能風アプリケーションに近いです。）  

自然言語処理としては `janome` による形態素解析、`Word2Vec` による単語ベクトル化、`cosine_similarity` による類似度計算を組み合わせ、発話コーパスと照らし合わせて返答を選択します。  
GUI部分は `Tkinter` により、ユーザーインターフェースの切り替え（クラシック/モダン）や、発話の入力、ボットの応答が可能になっています。  
また、"追加モード" を使えばユーザーがチャットボットに新しい質問と応答を教えることができ、対話データを継続的に拡張可能です。  

※ 対話コーパス（corpus.json）は、直接書き換えることも可能です。好きなように書き換えてオリジナルのチャットボットを作成することもできます。  

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
対話型AI「ChatGPT」等の支援を受けて作成したオリジナルコンテンツです。  
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

※ 通常のソースコード配布であれば PSF ライセンスの添付は不要ですが、PyInstaller などで実行ファイル化した場合は、内部に Python のコードが含まれるため、PSF ライセンスの同梱が必要です。  
※ Python 3.8.6以降、PSF LicenseとZero-Clause BSDライセンスのデュアルライセンスとなっていますが、
  これはドキュメント内のコード例やレシピ、その他のコードを使用する場合に必要となるようです。  
  通常の使用であれば PSF License のみで大丈夫みたいです。  

#### **Tkinter**  
- © Regents of the University of California, Sun Microsystems, Inc., Scriptics Corporation, and other parties  
TkinterはPythonに含まれるGUIライブラリですが、その動作にはTcl/Tkが使用されています。  
- [Tcl/Tk License](https://www.tcl.tk/software/tcltk/license.html)  

---

### 使用ライブラリとライセンス

### 📚 Janome（日本語形態素解析器）

> 純Python製の日本語形態素解析ライブラリで、辞書を内蔵しており追加の設定なしで利用できます。  
> 本アプリケーションでは、ユーザー入力文、出力文の解析に使用しています。

- **ライセンス**：Apache License 2.0  
- **著作権表示**：© 2015–2025, Tomoko Uchida. All rights reserved.
- **GitHub**：[https://github.com/mocobeta/janome](https://github.com/mocobeta/janome)

- **NOTICE**：Janome には、形態素解析に使用される **MeCab-IPADIC 辞書データ** が含まれており、  
 その辞書に関する以下の注意事項（再配布条件）を満たす必要があります：
 - **この辞書は「無保証（NO WARRANTY）」のもと配布されています。**  

※ 詳細は本リポジトリ内[NOTICE_Janome.txt](./licenses/third_party/NOTICE_Janome.txt)をご確認ください。  
※ Apache License 2.0	には、明確に「NOTICEがある場合は再配布者も添付すること」と記載されています。  
※ Janomeに含まれている辞書データ（MeCab-IPADIC）には「無保証」を明記する義務があり（上記）、それが`NOTICEファイル`に書かれています。  

🔖 NOTICEファイルとは？
- ライセンスでは伝えきれない「追加の著作権情報や注意事項（通知）」を記載するための補足ファイルです。

---

### 🧠 Gensim

自然言語処理や文書ベクトル化のために **Gensim** ライブラリを使用しています。

> Gensim は、トピックモデリング、類似度計算、Word2Vec などのニューラル埋め込みに対応した、拡張性の高い Python 製の自然言語処理ライブラリです。  
> 高速かつメモリ効率に優れ、大規模なコーパスにも対応可能な設計となっています。

- **ライセンス**：LGPLv2.1+（GNU Lesser General Public License）  
- **著作権表示**：Copyright © Radim Řehůřek and contributors  
- **公式サイト**：[https://radimrehurek.com/gensim/](https://radimrehurek.com/gensim/)  
- **GitHub**：[https://github.com/piskvorky/gensim](https://github.com/piskvorky/gensim)
- **ライセンス全文**： [Gensim GitHubリポジトリのLICENSEファイル](https://github.com/piskvorky/gensim/blob/develop/COPYING)  

> ※ Gensim は、OSI承認の GNU LGPLv2.1 ライセンスの下で配布されています。これは、個人・商用を問わず無償で使用可能であることを意味しますが、Gensim を改変して再配布する場合は、その改変部分のソースコードを開示する必要があります。  
> それ以外の用途では自由に再配布が可能ですが、Gensim のライセンス自体を変更することはできません（当然だろ！）。  
> なお、LGPL ライセンスが適さない場合は、商用サポートの利用も検討できます。  
> — [Gensim公式サイトより引用](https://radimrehurek.com/gensim/)

---

### ⚙️ scikit-learn
> 主にベクトル間の距離計算に使用しています。
- **ライセンス**：BSD 3-Clause License  
- **著作権表示**：Copyright (c) 2007-2024 The scikit-learn developers. All rights reserved.  
- **公式サイト**：[https://scikit-learn.org/](https://scikit-learn.org/)  
- **ライセンス全文**：[https://github.com/scikit-learn/scikit-learn/blob/main/COPYING](https://github.com/scikit-learn/scikit-learn/blob/main/COPYING)

> ※ scikit-learn は、カリフォルニア大学バークレー校由来の自由度の高い BSD ライセンス（3条項）に基づき配布されており、商用・非商用を問わず再利用が可能です。  

---

### 🔢 NumPy

> 数値計算処理の基盤として **NumPy** を使用しています。  
> Gensim や scikit-learn など、Python製の多数の科学技術系ライブラリが NumPy に依存しており、**Pythonにおける数値処理の共通基盤**とされています。  

- **ライセンス**：BSD 3-Clause License（通称："NumPy License"）  
- **著作権表示**：© 2005–2025 NumPy Developers. All rights reserved.  
- **ライセンス原文**：[https://github.com/numpy/numpy/blob/main/LICENSE.txt](https://github.com/numpy/numpy/blob/main/LICENSE.txt)  
- **公式サイト**：[https://numpy.org](https://numpy.org)  
- **GitHub**：[https://github.com/numpy/numpy](https://github.com/numpy/numpy)

> NumPyは 基本的にはBSD 3-Clause License に準拠していますが、一部に NumPy Project 独自の補足説明が付いたカスタム表記（"NumPy License" と書かれることもある）を採用しています。  

> NumPy は、自由度の高い BSD ライセンスのもとに配布されており、活発で反応が早く、多様性に富んだコミュニティによって GitHub 上で開発・保守されています。  
> (*Distributed under a liberal BSD license, NumPy is developed and maintained publicly on GitHub by a vibrant, responsive, and diverse community.*)  
> — [NumPy公式サイトより引用](https://numpy.org/)  
> NumPyには、一部内部で使用されている第三者ソフトウェアコンポーネントが存在します。  
> 必須ではないようですがライセンス情報を[LICENSES_NumPy_Bundled.txt](./licenses/third_party/LICENSES_NumPy_Bundled.txt) に記載しています。

---

# 📐 SciPy（数値計算と科学技術計算ライブラリ）

> Pythonにおける数値計算・科学技術計算を担う、強力なオープンソースライブラリです。  
> 本アプリケーションでは、コサイン類似度計算や内部数値処理の一部において使用しています。  
> `scikit-learn`の必須依存です。  

- **ライセンス**：BSD 3-Clause License   
- **著作権表示**：Copyright (c) 2001-2002 Enthought, Inc. 2003, SciPy Developers. All rights reserved.   
- **公式サイト**：[https://scipy.org/](https://scipy.org/)   
- **GitHub**：[https://github.com/scipy/scipy](https://github.com/scipy/scipy)  

---

## 🔍 SciPyについて補足説明

SciPyは、以下のようなモジュール群を通じて、幅広い機能を提供しています：

- `scipy.linalg`：線形代数計算（NumPyの上位互換的な機能）
- `scipy.spatial`：空間探索やコサイン類似度などの計算
- `scipy.optimize`：最適化問題の解法
- `scipy.fft`：高速フーリエ変換（FFT）
- その他、多数の科学技術系モジュール

本アプリケーションでは、特に  
**`scipy.spatial.distance.cosine()` 関数**を使用し、  
ベクトル間の類似度計算を高速かつ安定して行っています。  
（`pyi-archive_viewer`で確認しているときにChatGPTが見つけました。もしかしたらライセンスファイル自体は必須ではないかもしれません。）  

> SciPyは、NumPyを基盤として構築されており、さらにOpenBLASなどの数値計算ライブラリを内部的に活用しています。  
> 本プロジェクトにおいても、PyInstallerによる実行ファイル化の過程で、関連DLL（OpenBLASなど）が含まれています。  
> これらについては、別途記載しているライセンス一覧をご参照ください。  
> SciPyには、一部内部で使用されている第三者ソフトウェアコンポーネントが存在します。  
> 必須ではないようですが、ライセンス情報を[LICENSES_SciPy_Bundled.txt](./licenses/third_party/LICENSES_SciPy_Bundled.txt) に記載しています。

---

### ⚙️ OpenBLAS（数値計算高速化用ライブラリ）

NumPyおよびSciPyが内部的に利用する、オープンソースのBLAS（Basic Linear Algebra Subprograms）実装ライブラリです。  
本アプリケーションを PyInstaller により実行ファイル化した際に、  
OpenBLAS のDLLファイルが自動的に組み込まれていることを確認しています。

- **ライセンス**：BSD 3-Clause License  
- **著作権表示**：Copyright (c) 2011-2014, The OpenBLAS Project All rights reserved.
- **公式サイト**：[http://www.openmathlib.org/OpenBLAS/](http://www.openmathlib.org/OpenBLAS/)  
- **GitHub**：[https://github.com/xianyi/OpenBLAS](https://github.com/xianyi/OpenBLAS)

> ※ 実行ファイル内に含まれている内容の確認には、`pyi-archive_viewer` を使用しています。  
> 例：
> ```
> pyi-archive_viewer dist/YourApp.exe
> ```
> ※ 本アプリケーションにおいては、Intel MKLやLAPACK単体のDLLは確認されておらず、  
> OpenBLASのみが含まれていることを確認済みです。

> 詳細なライセンス条文は [LICENSE_OpenBLAS.txt](./licenses/third_party/LICENSE_OpenBLAS.txt) に記載しています。

---

## 📚 OpenBLASについて

### 🚀 OpenBLASとは  
OpenBLAS（オープンブラス）は、BLAS（Basic Linear Algebra Subprograms）を  
オープンソースで実装した数値計算ライブラリです。  
行列計算・ベクトル計算などを高速に処理するための**基盤となる部品**であり、  
`NumPy`や`SciPy`などのライブラリも、内部では`OpenBLAS`を呼び出して計算速度を向上させています。

### 🛠️ BLAS（Basic Linear Algebra Subprograms）とは  
BLASとは、  
**「線形代数（行列・ベクトル）計算のための標準的な基本プログラム群」**  
のことを指します。

**線形代数**とは──  
➡️ 行列・ベクトル・スカラー（数値）などを使った計算全般のことです。

**なぜ"基本プログラム集"と呼ばれるのか？**  
➡️ 「行列×行列」や「ベクトルの内積」など、標準的な操作をまとめたものだからです。

🔹 BLASで提供される主な操作例
- ベクトル同士の加算
- 行列とベクトルの乗算
- 行列同士の掛け算

### ⚡ OpenBLASがあると？  
OpenBLASは、C言語やアセンブリ言語で記述された最適化コードを利用しており、  
これにより**大規模な行列計算を非常に高速**に行うことができます。

### ℹ️ その他のBLAS実装について  
BLASの実装には、OpenBLAS以外にもいくつか種類があります。

- **OpenBLAS**  
  オープンソースで広く使われている実装（今回はこちらを使用）。
- **Intel MKL（Math Kernel Library）**  
  Intel社製の超高性能版（商用向けライセンスが中心）。
- **ATLAS（Automatically Tuned Linear Algebra Software）**  
  ハードウェアに合わせて自動最適化を行うBLAS実装。

🌟 **まとめ**  
OpenBLASは、Pythonでの数値計算を支える**隠れた重要部品**です。  
特に大量データの演算を行う際、その恩恵は非常に大きなものとなっています。

---

#### 📦 PyInstaller  

このプロジェクトは、**PyInstaller** を使用して実行ファイル化に対応しています。  
PyInstaller は GNU GPL ライセンスですが、例外規定により  
**生成される実行ファイル自体は GPL の制約を受けません**。

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

- このコードではPC内の `Meiryo` 、 `Yu Gothic` 、 `Consolas` を参照する形で記述しています。プロジェクト内にフォントファイルは存在しません。  
- 環境によっては正しく文字が表示されない場合があります。  

---

これらのプロジェクトの開発者および貢献者の皆様に、心より感謝申し上げます。

---

### 問題点
- 音楽や効果音は未実装です。
- 環境によっては正しく文字が表示されない場合があります。
- コーパスの誤検知が起こります。  
- アプリケーション起動時にコーパスを読み込む関係か？起動が遅いです。(5~10秒程度。コーパスの内容や環境によってはもっと時間がかかるかもしれません)

---

# 🛠️ PyInstallerによる実行ファイル化ガイド

## 📁 ディレクトリ構成

```
📁 プロジェクトフォルダ/
├─ corpus/
│  └─ corpus.json           ←  コーパス（外部ファイルとして保持）
├─ RetroBot_PseudoAI_v1.py ← メインコード
└─ icon.ico                 ← アイコン画像
```

---

## 📦 必要なライブラリのインストール

以下のライブラリを事前にインストールしてください。

```shell
pip install janome
pip install gensim
pip install pyinstaller
```

> `gensim` は依存モジュール（`numpy`など）もあわせて自動でインストールされます。

---

## 🧠 Janomeの辞書パスを確認する

**Janomeが使用する日本語辞書**（`sysdic`）は、PyInstallerでは自動で含まれないため、明示的に指定する必要があります。  
通常は `site-packages/janome/sysdic` にあります。

> Janomeの辞書は約4MBあり、サイズは少し増えますが、**オフラインで自然な日本語処理が可能**になる重要なリソースです。

### 1. 辞書の場所を調べる（以下のスクリプトを一度だけ実行）：

```python
import janome
from pathlib import Path

print(Path(janome.__file__).parent / "sysdic")
```

> 📍 このスクリプトは「**Janomeの辞書データがあるパスを出力する確認用スクリプト**」です。

出力されたパス（例：  
`C:/Users/YourName/AppData/Local/Programs/Python/Python312/Lib/site-packages/janome/sysdic`  
）をメモしてください。

---

## 🛠️ 実行ファイルの作成手順

### 2. プロジェクトフォルダに移動

```shell
cd <プロジェクトフォルダのパス>
```

例：デスクトップにある場合

```shell
cd C:/Users/<ユーザー名>/Desktop/RetroBot_PseudoAI_v1
```

### 3. PyInstallerでビルド

```shell
pyinstaller --onefile --noconsole ^
  --add-data "C:/上で確認したパス/janome/sysdic;janome/sysdic" ^
  RetroBot_PseudoAI_v1.py --icon=icon.ico
```

> ※ パスの区切り文字に注意（Windowsでは `\` ではなく `/` を使うと確実です）。

---

## 🔍 オプション解説

| オプション           | 説明                             |
|----------------------|----------------------------------|
| `--onefile`          | すべてを1つの `.exe` にまとめる |
| `--noconsole`        | コンソール非表示（GUI向け）     |
| `--icon=icon.ico`    | アプリに指定したアイコンを設定  |
| `--add-data`         | Janomeの辞書を明示的に含める    |

---

## ✅ 実行ファイルの確認

ビルドが成功すると以下のような構成になります：

```
📁 プロジェクトフォルダ/
├── build/                    ← ビルド時の一時ファイル（削除してOK）
├── dist/                     ← 実行ファイルが出力されるフォルダ
│   └── RetroBot_PseudoAI_v1.exe ← 完成した .exe
├─ corpus/
│  └─ corpus.json             ← 外部参照のコーパス
├─ RetroBot_PseudoAI_v1.py    ← メインスクリプト
├─ icon.ico                   ← アイコンファイル
└─ RetroBot_PseudoAI_v1.spec  ← PyInstaller用設定ファイル（任意で削除OK）
```

---

## 📦 配布時の最終構成例

以下のように を `.exe` の横に配置してください：

```
📁 RetroBot_PseudoAI_v1/
├─ RetroBot_PseudoAI_v1.exe ← 完成した実行ファイル
└─ corpus/                   ← `corpus` フォルダ
    └─ corpus.json           ← コーパスは外部参照なので編集・追加OK！
```

---

## 📝 補足

- `corpus.json` は外部ファイルのため、ユーザーが自由に編集・追加できます。
- Janomeのバージョンが変わるとパスが変わる可能性があります。

### 注意事項

- **セキュリティに関する注意**  
  PyInstallerはスクリプトを実行ファイルにまとめるだけのツールであり、コードの暗号化や高度な保護機能を提供するものではありません。  
  そのため、悪意のあるユーザーが実行ファイルを解析し、コードやデータを取得する可能性があります。  
  コードやデータなどにセキュリティが重要なプロジェクトで使用する場合は、追加の保護手段を検討してください。  

- **OSに応じた調整**  
  MacやLinux環境で作成する場合、`--add-data` オプションのセパレータやアイコン指定の書式が異なるようです。  
  詳細は[PyInstaller公式ドキュメント](https://pyinstaller.org)をご確認ください。  
  実行ファイル化において発生した問題は、PyInstallerのログを確認してください。  

- **ライセンスとクレジットに関する注意**   
    **推奨事項**  
     PyInstallerのライセンスはGPLv2（GNU General Public License Version 2）ですが、例外的に商用利用や非GPLプロジェクトでの利用を許可するための追加条項（特別例外）が含まれています。  
     実行ファイルを配布するだけであれば、PyInstallerの特別例外が適用されるため、GPLv2ライセンスの条件に従う必要はないようです。
     ライセンス条件ではありませんが、プロジェクトの信頼性を高めるため、READMEやクレジットに「PyInstallerを使用して実行ファイルを作成した」旨を記載することを推奨します。  

    **PyInstallerのライセンスが必要な場合**  
     PyInstallerのコードをそのまま再配布する場合、もしくは改変して再利用する場合は、GPLv2ライセンスに従う必要があります。  
     この場合、以下を実施してください：  
      - PyInstallerのライセンス文を同梱する。  
      - ソースコードを同梱するか、ソースコードへのアクセス手段を提供する。  

    **詳細情報**  
     PyInstallerのライセンスについて詳しく知りたい場合は、[公式リポジトリのLICENSEファイル](https://github.com/pyinstaller/pyinstaller/blob/develop/COPYING.txt)をご参照ください。  

---

## このアプリケーションのライセンス

- **このアプリケーションのコード**: MIT License。詳細は[LICENSE-CODE](./licenses/application/LICENSE-CODE)ファイルを参照してください。
- **画像**: Creative Commons Attribution 4.0 (CC BY 4.0)。詳細は[LICENSE-IMAGES](./licenses/application/LICENSE-IMAGES)ファイルを参照してください。
- **コーパス**: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)詳細は[LICENSE-CORPUS](./licenses/application/LICENSE-CORPUS)ファイルを参照してください。  

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

