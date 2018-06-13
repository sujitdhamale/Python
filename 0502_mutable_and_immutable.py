#!/usr/bin/python
#0502_mutable_and_immutable.py by Sujit Dhamale

def main():
    # immutable object cannot change value

    x=10
    print("\nID =",id(x))
    print("Type =",type(x))
    print("Value =",x)
    
    x=20
    print("\nID =",id(x))
    print("Type =",type(x))
    print("Value =",x)

    x=10
    print("\nID =",id(x))
    print("Type =",type(x))
    print("Value =",x)
    
    #mutable object may change value
    x=[1,2,3,4]
    print("\nID =",id(x))
    print("Type =",type(x))
    print("Value =",x)
    x.append(5)
    print("\nID =",id(x))
    print("Type =",type(x))
    print("Value =",x)

    

if __name__ == "__main__": main()
