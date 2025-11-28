# Count Vowels and Consonants
# Count the number of vowels and consonants in a string.

a = 'absnsnxioujxnsj'

def count_vowels(a):
    return sum(1 for char in a if char in 'aeiouAEIOU')

print(count_vowels(a))  