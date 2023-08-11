#!/usr/bin/python3
# Lujaja Luvuga

"""Write a program that prints all the names defined by the compiled module
    You should print one name per line, in alpha order
    You should print only names that do not start with __
    Your code should not be executed when imported
    Make sure you are running your code in Python3.8.x (hidden_4.pyc has
    been compiled with this version)
"""
if __name__ == "__main__":
    import hidden_4

    names = dir("hidden_4")

    for name in names:
        if (name[:2] != "__"):
            print(name)
