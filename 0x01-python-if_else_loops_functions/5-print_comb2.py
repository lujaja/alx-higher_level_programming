#!/usr/bin/python3
for i in range(00, 100):
    if (i > 0) and (i < 100):
        print(f", ", end='')
    print("{:02}".format(i), end="")
