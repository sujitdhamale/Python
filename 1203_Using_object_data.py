#!/usr/bin/python
#1203_Using_object_data.py.py by Sujit Dhamale
#for Using object data

class indian:
    
    def __init__(self,val):
        self.v=val           #self.v is attached to the object
        print("Inside of constructor")
        
        
    def bjp(self):
        print("Acche Din ane wale hai ",self.v)
    def congress(self):
        print("Kattar soch nahi, yuva josh ",self.v)
        
    def setVal(self,val):
        self.v=val
    
    def getVal(self):
        return self.v

def main():
    
    #encapsulation 
    sujit = indian(100)
    sagar = indian(50)
    sujit.bjp()
    sujit.congress()
    
    #set the data 
    sujit.v=500
    sujit.bjp()
    sujit.congress()
        
    sagar.bjp()
    sagar.congress()
    
    #ste and Get method 
    sujit.setVal(200)
    print("Get value is ",sujit.getVal())
    


if __name__ == "__main__": main()