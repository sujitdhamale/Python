#!/usr/bin/python
#0904_regex_reuse_compile.py by Sujit Dhamale
#to Understanding regular expression and Reusing regular expressions with re.compile

import re

def main():
    fh=open("0902_data.txt")
    pattern=re.compile('PYTHON',re.IGNORECASE)  # This is pre-complied regular expression
    
    for line in fh:
        if re.search(pattern, line):
            print(line)
        
    
    
        
if __name__ == "__main__": main()
