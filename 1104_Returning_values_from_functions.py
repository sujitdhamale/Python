#!/usr/bin/python
#1103_Using_named_function_arguments.py  by Sujit Dhamale
#to understanding Returning values from functions


def main():
    print(testfunction())
    
    for i in testfunction():
        print(i,end=" ")
    
def testfunction():
    #return "This is test function"
    #return 25
    return range(1,25)
   
if __name__ == "__main__": main()