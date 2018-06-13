#!/usr/bin/python
#0507_identity_of_variable.py by Sujit Dhamale

def main():

    x=10
    print("\nID of x=",id(x))
    print("Type =",type(x))
    print("Value =",x)

    y=10
    print("\nID of y=",id(y))  
    print("Type =",type(y))
    print("Value =",y)

    print("\nID of x=",id(x))
    print("\nID of y=",id(y))
    print("\nID of 10=",id(10))
    
    x=20
    print("\nID =",id(x))
    print("Type =",type(x))
    print("Value =",x)

    x=10
    print("\nID =",id(x))
    print("Type =",type(x))
    print("Value =",x)

    x,y=10,10.0
    print("x,id(x),type(x)",x,id(x),type(x))
    print("y,id(y),type(y)",y,id(y),type(y))
    
    #we can compare value of two variable using equal operator "="
    print("X==Y :",x==y)

    
    #we can compare id of two variable using "is" operator
    print("X is Y :",x is y)

    

if __name__ == "__main__": main()
