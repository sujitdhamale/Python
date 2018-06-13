#!/usr/bin/python
#0506_dictionaries.py by SUjit Dhamale

def main():
    print("Dictionary")

    d={'one': 1,'two':2,'three':3, 'four':4, 'five':5 }
    print(d)

    print("iterate through the dictionary by key ")
    for k in d:
        print(k,d[k])

    print("sort Dictionary ")
    for k in sorted(d.keys()):
        print(k,d[k])

    #keyword arguments are used to great advantage in defining dictionary like constructor for the class
    print("Keyword Arguments")
    d= dict(
        one=1,two=2,three=3,four=4,five='5'
        )
    for k in sorted(d.keys()):
        print(k,d[k])


    #Dictionary are mutable object so we can add new value to dictionary 
    print("Add new value to dictionary")
    d= dict(
        one=1,two=2,three=3,four=4,five='5'
        )
    d['six']=6
    print(d)

         
if __name__ == "__main__": main()
