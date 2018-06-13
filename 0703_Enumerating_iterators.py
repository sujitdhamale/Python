#!/usr/bin/python
#\0703_Enumerating_iterators.py by Sujit Dhamale
#to Understanding for Enumerating iterators

def main():
    
    
    fh=open('line.txt')
    for line in fh.readlines():
        #print(line)
        print(line,end="")
    
    
    #Enumerate function 
    print("Enumerate function")
    fh=open('line.txt')
    for index,line in enumerate(fh.readlines()):
        #print(line)
        print(index,line,end="")
        
    #Enumerate function on string(container)
    s="this is a string"
    for i, c in enumerate(s):
        print(i,c)   
    
    #Enumerate function to identified index of character 'S'
    print("\nEnumerate function to identified index of character 'S'")
    s="this is a string"
    for i, c in enumerate(s):
        if c=='s':
            print("index {} is an s ".format(i))
            
if __name__ == "__main__": main()