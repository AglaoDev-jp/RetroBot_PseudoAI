from janome.tokenizer import Tokenizer
from collections import Counter

# フィラー語と対応する感情
filler_emotions = {
    "えーっと": "迷い",
    "あのー": "遠慮・戸惑い",
    "うーん": "悩み・否定",
    "はぁ": "落胆・ため息",
    "ふー": "安堵・解放",
    "まあ": "仕方なさ・妥協",
    "なんか": "曖昧さ・もやもや"
}

# テスト文章（自由に変えてOK）
text = """
えーっと、それは……うーん、どうなんでしょうね。
あのー、私もちょっと分からなくて。
はぁ……まあ、仕方ないですね。
"""

# Janomeによるトークン化
tokenizer = Tokenizer()
tokens = [token.surface for token in tokenizer.tokenize(text)]

# フィラーの抽出（読み込んだ語句と照合）
fillers_found = [word for word in tokens if word in filler_emotions]

# 結果カウント
counter = Counter(fillers_found)
emotion_summary = Counter(filler_emotions[word] for word in fillers_found)

# 表示
print("🔍 検出されたフィラーと感情傾向：")
for word, count in counter.items():
    emotion = filler_emotions[word]
    print(f"・{word}（{emotion}）: {count}回")

print("\n🧠 感情の傾向サマリー：")
for emotion, count in emotion_summary.items():
    print(f"{emotion}: {count}回")
