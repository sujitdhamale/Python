#!/usr/bin/python
#0405_conditionals.py by Sujit Dhamale

def main(): 
    #1.	conditional execution 

    a,b=2,1

    if a<b:
        print("A is less than B")
    elif a > b:
        print("A is greter than B")
    else:
        print("A is equal to B")


    #2.	conditional values or conditional expression

    a,b=1,1
    s="A is less Than B" if a < b else "A is not Less than B"
    print(s)
    
if __name__ == "__main__": main()
