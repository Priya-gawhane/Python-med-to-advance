# Check if String is Palindrome
# Determine if a string reads the same forwards and backwards.

# Input: "racecar" → Output: true

a = 'helleh'

if a == a[::-1]:
    print('palindrome')
else:
    print('not palindrome')