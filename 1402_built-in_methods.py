#!/usr/bin/python
#1402_built-in_methods.py by Sujit Dhamale
#to understand how to Operating on sequences with built-in methods


def main():
    t=tuple(range(20))
    print(t)
    print(type(t))
    print(10 in t)
    print(50 in t)
    print(50 not in t)
    
    #identify value by specifying position  
    print(t[5])
    
    #Tuple are iterator
    for i in t:
        print(i,end=" ")
        
    #List 
    print("\n\nList")
    t=list(range(20))
    print(t)
    print(type(t))
    print(10 in t)
    print(50 in t)
    print(50 not in t)
    
    #identify value by specifying position  
    print(t[5])
    
    #List are iterator
    for i in t:
        print(i,end=" ")
    
    
    
    print("\n\nCOunt ")
    t=tuple(range(0,100,10))
    print(t)
    print(t.count(50))
    
    
    print("\n Method used in List")
    x=list(range(0,100,10))
    print(x)
    x.append(200)
    print(x)
    x.extend(range(5,10))
    print(x)
    x.insert(1, 50)
    print(x)
    x.remove(50)
    print(x)
    del x[1]
    print(x)
    print(x.pop())
    print(x)
    print(x.pop(0))
    print(x)
    print(x.pop(2))
    print(x)
    
if __name__ == "__main__": main()



