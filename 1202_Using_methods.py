#!/usr/bin/python
#1105_generator_function.py by Sujit Dhamale
#to  Creating a sequence with a generator function

class indian:
    
    def __init__(self,val):
        self.v=val           #self.v is attached to the object
        print("Inside of constructor")
        
        
    def bjp(self):
        print("Acche Din ane wale hai ",self.v)
    def congress(self):
        print("Kattar soch nahi, yuva josh ",self.v)

def main():
    
    #encapsulation 
    sujit = indian(100)
    sagar = indian(50)
    sujit.bjp()
    sujit.congress()
    sagar.bjp()
    sagar.congress()


if __name__ == "__main__": main()