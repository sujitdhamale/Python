#!/usr/bin/python
#1207_decorators.py by Sujit Dhamale
#to understand Using decorators

class inclusive_rnage:
    def __init__(self,*args):
        numargs=len(args)
        
        if numargs < 1 : raise TypeError("required at list one parameter ")
        elif numargs ==1:
            self.stop=args[0]
            self.start=0
            self.step=1
        elif numargs ==2 :
            self.start,self.stop=args
            self.step=1
        elif numargs ==3:
            self.start,self.stop,self.step=args
        else: raise TypeError("expected at most 3  parameters ")
        
    def __iter__(self):
        i=self.start
        while i <= self.stop:
            yield i
            i +=self.step

def main():
    o = inclusive_rnage(2,10,2)
    for i in o :
        print(i,end=' ')

if __name__ == "__main__": main()