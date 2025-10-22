#Print each vowel with its index

word = "enumerate"

for i, vowel in enumerate(word):
    if vowel in "aeiou":
        print(i, vowel)