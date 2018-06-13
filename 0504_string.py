#!/usr/bin/python
#0504_string.py b y SUjit Dhamale

def main():
    s="This is string ! "
    print(s)

    #you can use escape character in strings 
    s="This is \n \" string \" ! "
    print(s)

    #raw string 
    s=r"This is \n \" string \" ! "
    print(s)

    #to insert value  in the middle of the string  "format()" method is use
    n=2
    s="value of n ={} as per difination ".format(n)
    print(s)

    #python 2 format
    n=2
    s="value of n =%s as per difination  " %n
    print(s)

    #multiline string can be use with triple quote  (single/double)
    s='''\
Hello world !!
This is Sujit Dhamale
line number 1
\
line number 2\
line number 3
'''
    print(s)
if __name__ == "__main__": main()
