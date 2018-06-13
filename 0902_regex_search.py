#!/usr/bin/python
#0902_regex_search.py by Sujit Dhamale
#to Understanding regular expression and Searching with regular expressions

import re

def main():
    
    
    fh=open("0902_data.txt")
    print("\n###############Search single word  and print the line")
    for line in fh.readlines():
        if re.search('python',line):
            print(line,end="")   
 
    fh.seek(0)  # to move file pointer at begining
    print("\n###############Search multiple word  and print the line")
    
    for line in fh.readlines():
        if re.search('(us|understand|match)ing',line):
            print(line,end="")
            
    
    
    print("\n###############Search multiple word  and print the single word ")
    fh.seek(0)
    for line in fh.readlines():
        match=re.search('(us|understand|match)ing', line)
        if(match):
            print(match.group())

    
        
if __name__ == "__main__": main()
