#!/usr/bin/python
#1304_Splitting_joining_strings.py by Sujit Dhamale
#to understand how to Splitting and joining strings 

def main():
    
    s="this is strings of words"
    print(s)
    print(s.split())
    print(s.split('i'))
    
    #Split string into  list 
    print("\n\nSplit string into  list ")
    word=s.split()
    print(word)
    for w in word:
        print(w)
    
    #joining method
    print("\n\nJoining method")
    newstring=":".join(word)
    print(newstring)
    
 
    
    
    
if __name__ == "__main__": main()



