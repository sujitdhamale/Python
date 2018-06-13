#!/usr/bin/python
#1105_generator_function.py by Sujit Dhamale
#to Understanding  Creating a sequence with a generator function


def main():
    print("")
    for i in inclusive_range(1,26,2):
        print(i,end=' ')

def inclusive_range(start,stop,step):
    i=start
    
    while i <= stop:
        yield i
        i +=step

    
if __name__ == "__main__": main()