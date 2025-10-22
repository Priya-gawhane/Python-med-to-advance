#Print indices and values of all scores >= 80.

scores = [95, 67, 88, 45, 90, 76]

for i, score in enumerate(scores):
    if score >= 80:
        print(i, score)