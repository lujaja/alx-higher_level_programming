#!/usr/bin/python3
# Lujaja Luvuga <jarzcyber@gmail.com>
""""print a text with 2 new line after each . ? :"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    char = 0
    while char < len(text):
        print("{}".format(text[char]), end="")
        if text[char] in ".?:":
            print("\n")
        elif text[char] == " ":
            char += 1
            continue
        char += 1
