#!/usr/bin/python
#1403_dictionarie.py by Sujit Dhamale
#to understand how to Organizing data with dictionaries


def main():
    #Dictionaries
    d={'one': 1, 'two': 2, 'three':3}
    print(d) 
    print(type(d))
    d= dict(one=1, two= 2, three=3)
    print(d)
    print(type(d))
    
    
    #initialize one dictionary from another using two asterisk 
    print("\n\ninitialize one dictionary from another using two asterisk")
    x=dict(four=4,five=5)
    d= dict(one=1, two= 2, three=3,**x)
    print(d)
    
    for k in d:
        print(k)
        
    for k,v in d.items():
        print(k,v)
        d.get(k)
    
    print(d.get('one'))
    print(d.get('one','not found'))
    print(x.get('one','not found'))
    
    print(d)
    del d['three']
    print(d)
    d.pop('two')
    print(d)
    
if __name__ == "__main__": main()



