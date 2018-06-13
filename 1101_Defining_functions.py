#!/usr/bin/python
#1101_Defining_functions.py  by Sujit Dhamale


def main():
    testfunction(10,20,30)
    testfunction(10)
    testfunction(10,15)

def testfunction(number,another=None,onemore=10):
    print("This is Test function :",number,another,onemore)

    
if __name__ == "__main__": main()