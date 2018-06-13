#!/usr/bin/python
#1103_Using_named_function_arguments.py  by Sujit Dhamale
#to understanding in function how to use named function arguments


def main():
    testfunction(one=1, two=2, three=3, four=4 , five=5)  ## These are keywords arguments 
    testfunction1(1,2,3,4,5,6,7,one=1, two=2, three=3, four=4 , five=5)  ## These are keywords arguments 


def testfunction(**kwargs):
    print("This is Test function :",kwargs['one'],kwargs['two'],kwargs['three'],kwargs['four'])

def testfunction1(number,another=None,onemore=10,*args,**kwargs):
    print("number,another,onemore,args  :",number,another,onemore,args)
    print("kwargs :",kwargs['one'],kwargs['two'],kwargs['three'],kwargs['four'])
   
if __name__ == "__main__": main()