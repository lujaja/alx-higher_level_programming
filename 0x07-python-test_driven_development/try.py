#!/usr/bin/python3
"""
matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

new_list = []
print("{}".format(matrix))
print("-----------------")
for row in matrix:
    print("{}".format(row))
    # print("")
[print(len(row)) for row in matrix]
# mat = [[num for num in row] for row in matrix]
# print(mat)
matb = [list(map(lambda x: round(x * 2, 2), row)) for row in matrix](
print(matb)
"""
for i in range(8):
    [print("#", end="") for j in range(8)]
    print()
