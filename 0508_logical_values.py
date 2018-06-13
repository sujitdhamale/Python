#!/usr/bin/python
#0508_logical_values.py by Sujit Dhamale

def main():
    a,b =1,1
    
    #"==" specify equality between two values and return either True or False
    print("a==b :",a==b)

    #"<,>,<=,>=" compare two values and return either True or False
    print("a==b :",a>=b)

    a=True
    print(a,type(a))

    #True and false are object of class "bool" and they are mutable objects
    a=True
    b=True
    print(a,type(a),id(a))
    print(b,type(b),id(b))  #id of both a and b are same
    print(id(True))
    
if __name__ == "__main__": main()
