#!/usr/bin/python
#0702_for.py by Sujit Dhamale
#to Understanding for loop

def main():
    fh=open('line.txt')
    for line in fh.readlines():
        #print(line)
        print(line,end="")
    
    print()    
    #all container type are iterator
    for i in [1,2,3,4,5]: # list is container
        print(i)
    
    for i in 'string':   # String is container
        print(i)
        
        
if __name__ == "__main__": main()
