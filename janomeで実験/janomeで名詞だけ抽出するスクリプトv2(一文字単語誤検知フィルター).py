from janome.tokenizer import Tokenizer

# Janomeのトークナイザを初期化
tokenizer = Tokenizer()

# テスト用の文章
text = "それに、あなたには「学びを楽しめる目と心」がもうあるんですから"

# 名詞だけを抽出してリストに格納
# 名詞のみ、かつ1文字のひらがなや記号は除外する
nouns = [
    token.surface
    for token in tokenizer.tokenize(text)
    if token.part_of_speech.startswith("名詞")
    and not token.surface in "んゎをがのとでに"
    and len(token.surface) > 1
]


# 結果を表示
print("抽出された名詞：", nouns)
