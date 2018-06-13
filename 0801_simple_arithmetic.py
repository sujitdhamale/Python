#!/usr/bin/python
#0801_simple_arithmetic.py by Sujit Dhamale
#to Understanding simple arithmetic


def main():
    a,b=5,3
    print("Addition A+B =",a+b)
    print("Subtraction A-B =",a-b)
    print("Multiplication A*B =",a*b)
    print("Division A/B =",a/b)
    print("Floor division A//B =",a//b)  #floor division which is simple integer division
    print("modulo/remainder  A%B =",a%b)
    print("divmod function : divmod(A,B) =",divmod(a,b)) # "divmod"  that give the two result together. First result is Division and second is remainder
    
    #increment and decrement operator 
    print("\nincrement and decrement operator ")
    num=5
    
    num+=2
    print("num+=2 :",num)
    
    num-=2
    print("num-=2 :",num)
    
    num*=2
    print("num*=2 :",num)
    
    num/=2
    print("num/=2 :",num)
    
    
    
        
if __name__ == "__main__": main()
