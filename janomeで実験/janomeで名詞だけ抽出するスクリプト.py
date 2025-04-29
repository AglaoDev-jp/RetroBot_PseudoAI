from janome.tokenizer import Tokenizer

# Janomeのトークナイザを初期化
# Tokenizer は Janomeが提供する形態素解析器クラス
tokenizer = Tokenizer()

# テスト用の文章
text = "それに、あなたには「学びを楽しめる目と心」がもうあるんですから"

# 名詞だけを抽出してリストに格納
nouns = [
    token.surface
    for token in tokenizer.tokenize(text)
    if token.part_of_speech.startswith("名詞")
]

# 結果を表示
print("抽出された名詞：", nouns)
