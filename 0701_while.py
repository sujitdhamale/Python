#!/usr/bin/python
#0701_while.py by Sujit Dhamale
#to Understanding while loop
#we are creating Fibonacci series 

def main():
    a,b=0,1
    while b < 50:
        print(b,end=" ")
        a,b=b,a+b
  
if __name__ == "__main__": main()
