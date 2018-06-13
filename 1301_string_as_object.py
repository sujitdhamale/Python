#!/usr/bin/python
#1301_string_as_object.py by Sujit Dhamale
#to Understanding strings as objects

def main():
    print()
    s="this is string"
    print(s)
    print(type(s))
    
    #upper 
    print("Upper : ",s.upper())
    s="this is string".upper()
    
    #format method 
    print("\n\nFormat method")
    print("this is string {} ".format(100))
    s="this is string {} ".format(50)
    print(s) 
    
    s="this is string %d " %20
    print(s) 
    
    s="this is string %s " % 'Sujit'
    print(s) 
    
if __name__ == "__main__": main()



