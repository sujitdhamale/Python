#!/usr/bin/python
#0404_assignValue.py by Sujit Dhamale
#script for showiing showing comments syntax

def main(): 
    a=10
    b="ten"

    print(a)
    print(type(a))
    print(b)
    print(type(b))

    #assign multiple variable at a same time   
    c,d = 5,7
    print(c,d)

    #Swaping variable
    c,d = d,c
    print(c,d)

    #Sequence of list like tuples 
    a=(1,2,3,4,5)
    print(a)
    print(type(a))

    #Sequence of list like tuples 
    a=[1,2,3,4,5]
    print(a)
    print(type(a))
    
if __name__ == "__main__": main()
