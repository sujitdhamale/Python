#!/usr/bin/python
#1002_handling_exception.py by Sujit Dhamale
#to Understanding how to handle exception in python

def main():
    print("Handling Exception")
 
    try:
        fh=open("1002_data.txt")
    except:
        print("Bhai file galat hai ")
    else:
        for line in fh:
            print(line.strip())
    
if __name__ == "__main__": main()
