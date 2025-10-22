#👉 Use enumerate() twice — once for rows and once for columns —


matrix = [[1,2,3],[4,5,6],[7,8,9]]

for i, row in enumerate(matrix):
    for j, column in enumerate(row):
        print(i, j, column, row)