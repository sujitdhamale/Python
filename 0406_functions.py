#!/usr/bin/python
#0406_functions.py by Sujit Dhamale


def main():
    print("Hello Worlds ")
    rang(5)
    rang(3)
    rang()

def rang(n=0):
    for i in range(n,10):
        print(i,end=" ")

    print()
    print("rang function completed " )
    
    
if __name__ == "__main__": main()
