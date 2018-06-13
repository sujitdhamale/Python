#!/usr/bin/python
#1303_str.format.py by Sujit Dhamale
#to Formatting strings with str.format

def main():
    a,b=50,100
    print("this is {} and taht is {}".format(a,b))
    
    #Immutable string 
    s="this is {} and taht is {}"
    print(s.format(a,b))
    print(id(s))
    print(id(s.format(a,b)))
    
    #python #2
    print("\n\npython #2") 
    s="this is %d and taht is %d" %(a,b)
    print(s)
    
    s="this is {0} and taht is {1} this is {0}".format(a,b)
    print(s)
    
    print("\n\nFor placeholder we can use dictionary ")
    d=dict(a="Ram", b="Laxman")
    s="this is {a} and taht is {b}".format(**d)
    print(s)
    
    
    
    
    
    
    
if __name__ == "__main__": main()



