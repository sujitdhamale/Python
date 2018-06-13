#!/usr/bin/python
#0505_Aggregating_lists_and_tuples.py by SUjit Dhamale

def main():
    print("Tuple ") #tuple is immutable  object. we cannot insert, append, delete in tuple

    x=(1,2,3,4)
    print(type(x),x)

    print("List") # list is mutable object
    x=[1,2,3,4]
    print(type(x),x)

    #list is mutable object so we can insert, append, delete in list
    x.append(5)
    print(type(x),x)

    x.insert(2,6)
    print(type(x),x)

    print("String ")
    x='string'
    print(type(x),x[2])
    print(type(x),x[2:4])   # this is slices


    #these sequence type can be used as iterators
    print("these sequence type can be used as iterators")
    x=(1,2,3,4)
    for i in x:
        print(i)

    x=[1,2,3,4]
    for i in x:
        print(i)
        
    x='string'
    for i in x:
        print(i)


    
if __name__ == "__main__": main()
