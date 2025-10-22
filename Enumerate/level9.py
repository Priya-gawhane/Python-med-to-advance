#use enumerate() to get both the row index and the row itself when iterating through a nested list.

matrix = [[1,2,3],[4,5,6],[7,8,9]]

for i, row in enumerate(matrix):
    print(i, row)