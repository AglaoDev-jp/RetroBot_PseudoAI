from janome.tokenizer import Tokenizer
from collections import Counter

# テスト用の文章（複数行でもOK）
text = """
私は昨日、図書館で友達とプログラミングについて話しました。
プログラミングはとても面白く、友達と一緒に新しいことを学びました。
図書館には多くの本がありましたが、特にAIの本が印象的でした。
"""

# Janomeで形態素解析
tokenizer = Tokenizer()
nouns = [
    token.surface
    for token in tokenizer.tokenize(text)
    if token.part_of_speech.startswith("名詞")
    and len(token.surface) > 1  # 1文字だけの名詞（例：ん、の）は除外
]

# Counterで名詞の出現回数をカウント
noun_counts = Counter(nouns)

# 出現頻度順に並べて上位を表示
print("🔡 名詞の出現頻度ランキング（上位10）:")
for word, count in noun_counts.most_common(10):
    print(f"{word}: {count}回")
"""
実行すると：

🔡 名詞の出現頻度ランキング（上位10）:
図書館: 2回
友達: 2回
プログラミング: 2回
昨日: 1回
一緒: 1回
こと: 1回
多く: 1回
AI: 1回
印象: 1回

…みたいに出ます。

🎯 こんな用途に使えます。

✅ 1. 文章のテーマをざっくり知る
たとえば：

学生のレポート → 「環境」「エネルギー」「社会」
技術記事 → 「AI」「モデル」「データ」「学習」
小説 → 「彼」「夜」「声」「街」「記憶」

➡ キーワードを拾うだけで「どんなジャンルの文か」が見えてくる！

✅ 2. 自分の文章の「口ぐせ」や「クセ」を見つける
日記やブログ、チャットログに使うと…

「自分って 'でも' をすごく使ってるな…」
「やたら '感じ' って言ってる」
「ポジティブな単語が多いぞ！」

➡ 自分の文体・思考の癖を“数値で”発見できます🧠

"""