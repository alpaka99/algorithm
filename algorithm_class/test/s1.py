from pandas import DataFrame as df

row = [i for i in range(10)]
matrix = []
for _ in range(10):
    matrix.append(row)
print(df(matrix))

for i in range(12):
    print(*matrix[0][:i])