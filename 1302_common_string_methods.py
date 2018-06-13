#!/usr/bin/python
#1302_common_string_methods.py by Sujit Dhamale
#to Working with common string methods

def main():
    
    print("")
    s="this is string"
    print(s)
    print(s.capitalize())
    
    print("\nUpper and Lower ")
    s="this is string".upper()
    print(s)
    s="THIS IS STRINGS".lower()
    print(s)
    
    print("\nSwapCase")
    s="THis Is stRIng".swapcase()
    print(s)
    
        
    print("\nfind()")
    s="this is string"
    print(s.find("is"))
    
    print("\nreplace()")
    s="this is string"
    print(s.replace('this', 'that'))
    
    print("\nstrip()")
    s="    this is string     "
    print(s)
    print(s.strip())
    
    s="    this is string with new line     \n"
    print(s)
    print(s.strip())
    
    print("\nrstrip()")
    s="    this is string     "
    print(s)
    print(s.rstrip())
    
    s="    this is string  ###"
    print(s.rstrip("###"))
    
    print("\nisalnum()")
    s="this is string"
    print(s.isalnum())
    s="thisisstring2"
    print(s.isalnum())
    
    print("\nisalpha()")
    s="this is string"
    print(s.isalpha())
    s="thisisstring2"
    print(s.isalpha())
    s="thisisstring"
    print(s.isalpha())
    
    print("\nisdigit()")
    s="12345"
    print(s.isdigit())
    
    print("\nisprintable()")
    s="this is string"
    print(s.isprintable())
    
    
if __name__ == "__main__": main()



