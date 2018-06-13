#!/usr/bin/python
#0604_conditional_expression.py by Sujit Dhamale
#to Understanding conditional expression

def main():
    a,b=10,1
    if a < b :
        v="A is less tahn B"
    else :
        v="A is not less than B"
    print(v)
    

    #conditional expression
    v="A is less tahn B" if a < b else "A is not less than B"
    print(v)
    
    
if __name__ == "__main__": main()
