#!/usr/bin/python
#1102 Using lists of arguments.py  by Sujit Dhamale
#to understanding in function how to use use  lists of arguments


def main():
    testfunction(10,20,30,40,50)
    testfunction(10)
    testfunction(10,15)

def testfunction(number,another=None,onemore=10,*args):
    print("This is Test function :",number,another,onemore)
    print("args ==>",args)
    
if __name__ == "__main__": main()