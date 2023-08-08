def uppercase(str):
    for i in str:
        s = ord(i)
        if (s >= 97 and s <= 122):
            print(chr(s - 32), end="")
        else:
            print(chr(s), end='')
    else:
        print()
