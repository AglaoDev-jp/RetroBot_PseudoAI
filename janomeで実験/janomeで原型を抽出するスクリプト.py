from janome.tokenizer import Tokenizer

# Janomeのトークナイザを初期化
# Tokenizer は Janomeが提供する形態素解析器クラス
tokenizer = Tokenizer()
text = "昨日はたくさん走って、泳いで、勉強しました。"

# 動詞の原形だけを抽出
base_verbs = [
    token.base_form
    for token in tokenizer.tokenize(text)
    if token.part_of_speech.startswith("動詞")
]

print("抽出された動詞の原形：", base_verbs)
"""
 原形とは？
✨「活用して変化した単語を、辞書に載っている“もとの形”に戻すこと」です。

✅ 例で見ると…
表示されている形（surface）	原形（base_form）
話しました	➡ 話す
走って	    ➡ 走る
飲んだ	    ➡ 飲む
学びたい    ➡ 学ぶ
しています	➡ する

💬 なぜ原形に戻すの？
同じ意味の単語でも、形が違うと別の単語として扱われてしまうからです。

❌ 原形を使わない場合
「走った」

「走って」

「走る」

➡ それぞれ別の単語としてベクトル化され、意味的な集約ができない

✅ 原形に統一する
→ 全部「走る」にすれば、一つの行動として学習させられる！

Word2Vecとの連携やテキストマイニングにおいて、「同じ単語は同じ形にしておく」のはとても大切なんです😊

"""