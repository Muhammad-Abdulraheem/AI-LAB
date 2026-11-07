import re

raw = [
    "ai, search!",
    "i can't log in.",
    "help@example.com",
    "su92 bssems25 039",
    "",
    "یہ ایک مثال ہے"
]

print("tokenization demo")
for text in raw:
    ws = text.split()
    words = re.findall(r"\b\w+\b", text, flags=re.unicode)
    print(repr(text), "whitespace:", ws, len(ws))
    print("word-like:", words, len(words))

documents = [
    "nlp helps computers understand language.",
    "python is used for programming.",
    "tokenization splits text into words.",
    "artificial intelligence is a useful field."
]

print("\nsimple document search chatbot")
query = input("enter your question: ").lower()

scores = []
for doc in documents:
    score = 0
    for word in query.split():
        if word in doc.lower():
            score += 1
    scores.append((score, doc))

scores.sort(reverse=True)

print("\nsearch results:")
for score, doc in scores[:3]:
    print(f"score: {score} | doc: {doc}")