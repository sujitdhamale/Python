#!/usr/bin/python
#0903_regex_replace.py by Sujit Dhamale
#to Understanding regular expression and Replacing with regular expressions

import re

def main():
    
    
    fh=open("0903_data.txt")
    print("\n###############Search and replace using re.sub()")
    for line in fh.readlines():
        print(re.sub('python', '#python3#',line))   

    
    print("\n###############Search and replace using re.search() and re.repalce() ")
    fh.seek(0)
    for line in fh.readlines():
        match=re.search('python', line)
        if(match):
            print(line.replace(match.group(),'#python3#'))

    
        
if __name__ == "__main__": main()
