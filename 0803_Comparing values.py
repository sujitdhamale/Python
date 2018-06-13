#!/usr/bin/python
#0803_Comparing values.py by Sujit Dhamale
#to Understanding Comparing values 


def main():
    
    print("5 < 6 :",5<6)
    print("6 < 5 :",6<5)
    
    print("5<=6 :",5<=6)
    print("5<=5 :",5<=5)
    print("6>=5 :",6>=5)
    print("6>=6 :",6>=6)
    print("6>=7 :",6>=7)
    
    #Equal to  Operator
    print("5==5 :",5==5)
    print("5==6 :",5==6)
    
    #Not equal to operator
    print("6!=7 :",6!=7)
    print("6!=6 :",6!=6)
    
    #"is" is used to comparing testing id 
    x,y =5,6
    print("\nid(x),id(y)",id(x),id(y))
    print("x is y ",x is y )
    print("x is not y ",x is not y )
    
    y=5
    print("\nid(x),id(y)",id(x),id(y))
    print("x is y ",x is y )
    
    x,y =5,5.0
    print("\nid(x),id(y)",id(x),id(y))
    print("type(x),type(y)",type(x),type(y))
    print("x is y ",x is y )
    print("x == y ",x == y )
    
    
    
    
    
    
        
if __name__ == "__main__": main()
