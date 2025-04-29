from janome.tokenizer import Tokenizer 
from collections import Counter

# カスタム感情分類（追加可能）
filler_emotions = {
    "えーっと": "迷い",
    "あのー": "遠慮・戸惑い",
    "うーん": "悩み・否定",
    "はぁ": "落胆・ため息",
    "ふー": "安堵・解放",
    "ふう": "安堵・解放",  # 表記ゆれ対応
    "まあ": "仕方なさ・妥協",
    "なんか": "曖昧さ・もやもや"
}

# 入力テキスト
text = """
えーっと、それは……うーん、どうなんでしょうね。
あのー、私もちょっと分からなくて。
はぁ……まあ、仕方ないですね。ふう……
"""

tokenizer = Tokenizer()
tokens = list(tokenizer.tokenize(text))

known_fillers = []
unknown_fillers = []

# 各トークンをチェック
for token in tokens:
    surface = token.surface
    parts = token.part_of_speech.split(",")
    # まず、辞書に登録されているフィラーなら「既知」として登録
    if surface in filler_emotions:
        known_fillers.append(surface)
    # 登録されていなく、かつ品詞が「感動詞」の場合は「未知」（その他）として登録
    elif parts[0] == "感動詞":
        unknown_fillers.append(surface)

# 結果のカウント
known_counts = Counter(known_fillers)
unknown_counts = Counter(unknown_fillers)

# 出力
print("🔍 検出されたフィラーと感情傾向：")
for word, count in known_counts.items():
    emotion = filler_emotions[word]
    print(f"・{word}（{emotion}）: {count}回")
for word, count in unknown_counts.items():
    print(f"・{word}（その他）: {count}回")

# 感情傾向のサマリー作成
emotion_summary = Counter()
for filler in known_fillers:
    emotion_summary[filler_emotions[filler]] += 1
for _ in unknown_fillers:
    emotion_summary["その他"] += 1

print("\n🧠 感情の傾向サマリー：")
for emotion, count in emotion_summary.items():
    print(f"{emotion}: {count}回")
