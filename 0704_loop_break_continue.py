#!/usr/bin/python
#0704_loop_break_continue by Sujit Dhamale
#to Understanding for Controlling loop flow with break continue and else

def main():
    
    #code to skip "S" from string
    s="this is a string"
    for c in s:
        if c == 's':
            continue
        print(c,end='')   
    
    #code to terminate loop if when get first "S" from string
    print("\n")
    s="this is a string"
    for c in s:
        if c == 's':
            break
        print(c,end='')   
        
if __name__ == "__main__": main()