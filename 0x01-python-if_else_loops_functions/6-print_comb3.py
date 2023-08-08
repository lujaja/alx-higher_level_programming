#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if (i < j):
            print(f"{i}{j}", end='')
            if (i != 8 or (i == 8 and j != 9)):
                print(f", ", end='')
