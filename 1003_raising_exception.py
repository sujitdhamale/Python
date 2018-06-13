#!/usr/bin/python
#1003_raising_exception.py by Sujit Dhamale
#to Understanding how to raise exception in Python


def main():
    print("Handling Exception")

    try:
        for line in readfile('1003_data.txt'):
            print(line.strip())
    except IOError as e :
        print("can not read file : ",e)
    except ValueError as e:
        print("bad filename : ",e)
        
def readfile(filename):
    
    if filename.endswith('.txt'):
        fh=open(filename)
        return fh.readlines()
    else:
        raise ValueError("Bro i am able to process on .TXT file ")
    
if __name__ == "__main__": main()
