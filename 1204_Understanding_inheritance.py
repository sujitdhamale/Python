#!/usr/bin/python
#1204_Understanding_inheritance.py by Sujit Dhamale
#for  Understanding inheritance

class india:
    def citizen(self):
        print("I am Indian citizen")
    def language(self):
        print("i speak Hindi")

class maharashta(india):
    def state(self):
        print("i am Maharashtrain ")
    def language(self):
        print("i speak marathi") 

class gugrat(india):
    def state(self):
        print("i am gugrati ")
    def language(self):
        print("i speak gugrati")
        
class madhyapradesh(india):
    def state(self):
        print("i am Bhopali/Indori ")
    def language(self):
        super().language()       #Super is function use for access the parent class property
        print("i speak Bhopali , indori and Hindi")

def main():
    print("Sujit ")
    sujit = maharashta()
    sujit.state()   
    sujit.language()
    sujit.citizen()    #inherite property of india
    
    print("\nShrayas ")
    Shrayas = madhyapradesh()
    Shrayas.state()   
    Shrayas.language()
    Shrayas.citizen() 


if __name__ == "__main__": main()