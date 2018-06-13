#!/usr/bin/python
#0802_bitwise_operator.py by Sujit Dhamale
#to Understanding 0802_bitwise_operator


def main():
    print(5)
    print(0b0101)
    b(5)
    
    x,y=0x55,0xaa
    print("X==",end=" ")
    b(x)
    
    print("Y==",end=" ")
    b(y)
    
    #OR operator
    print("\n#OR operator")
    b(x | y)
    
    #AND operator
    print("\n#AND operator")
    b(x & y)
    
    #Exclusive OR operator
    print("\n#OR operator")
    b(x ^ y)
    b(x ^ 0)
    b(x ^ 0xff)   # All bit's will be filpped
    
    #Shift Operator
    print("\n#Shift Operator")
    b(x >> 3)
    b(x << 3)
    
    
    
def b(n):
    print('{:8b}'.format(n))   # {:8b} is format string
    
        
if __name__ == "__main__": main()
