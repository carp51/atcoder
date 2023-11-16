A = [[1, 2, 3], [4, 5, 6]]

transposed_matrix = [list(x) for x in zip(*A)]

print(transposed_matrix)