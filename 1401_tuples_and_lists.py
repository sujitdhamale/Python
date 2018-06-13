#!/usr/bin/python
#1401_tuples_and_lists.py by Sujit Dhamale
#to understand how to Creating sequences with tuples and lists


def main():
    #Tuple are created with comma operator
    t=1,2,3,4,2
    print(t)
    print(type(t))
    print(t[0])
    print(t[3])
    
    #Last elemet  in tuple
    print(t[-1])
    print(t[len(t)-1])
    
    #Method use in Tuple
    print("\n",len(t))
    print(max(t))
    print(min(t))
    
    #Tuple are created with comma operator.
    print("\nTuple are created with comma operator.(Comma is must)")
    t=(1,2,3,4,5)
    print(t,type(t))
    t=(1)         #Due to missing in comma it is considering integer not tuple
    print(t,type(t))
    t=(1,)
    print(t,type(t))
    
    
    print("\n\n\n ################## list #########################")
    x=[1,2,3,4,5]
    print(x)
    print(type(x))
    
    #Last elemet  in LIST
    print(x[-1])
    print(x[len(t)-1])
    
    #Method use in Tuple
    print("",len(x))
    print(max(x))
    print(min(x))
    
    
    #Tuple are immutable so we can not change element in tuple but List is mutable so we can change element
    t=tuple(range(25))
    print(t)
    print(type(t))
    #t[10]=2   # This statement will give error because tuple is immutable 
    
    t=list(range(25))
    print(t)
    print(type(t))
    t[10]=2   # This statement will give error because tuple is immutable 
    print(t)
    
    
if __name__ == "__main__": main()



