# Python - Network #1

Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file at the root of the repo, containing a description of the repository
A README.md file, at the root of the folder of this project, is mandatory
Your code should use the pycodestyle (version 2.8.*)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
Your code should not be executed when imported (by using if __name__ == "__main__":)

Tasks

0. What's my status? #0
mandatory
Write a Python script that fetches https://alx-intranet.hbtn.io/status

You must use the package urllib
You are not allowed to import any packages other than urllib
The body of the response must be displayed like the following example (tabulation before -)
You must use a with statement

1. Response header value #0
mandatory
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

You must use the packages urllib and sys
You are not allow to import packages other than urllib and sys
The value of this variable is different for each request
You don’t need to check arguments passed to the script (number or type)
You must use a with statement
