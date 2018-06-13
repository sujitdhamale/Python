#!/usr/bin/python
#0407_objects.py by Sujit Dhamale

class bird:
    def __init__(self,name="Duck"):
        self.name=name

    def birdname(self):
        return self.name

def main():
    duck=bird()
    crow = bird('crow')

    print("duck ==>",duck.birdname())
    print("crow ==>",crow.birdname())

    
if __name__ == "__main__": main()
