# Find First Non-Repeating Character
# Find the first character that appears only once.


a = "sodiums"

def nonrepchar(a):

    for char in a:
        if a.count(char) == 1:
            return char

print(nonrepchar(a))