#!/usr/bin/python
#0805_slice.py by Sujit Dhamale
#to Understanding Operating on parts of a container with the slice operator 
def main():
    print("")
    list = [1,2,3,4,5,6,7,8,9,10]
    print(list)
    print(list[0])
    print(list[1])
    
    #slice of first 5 item 
    print("\nSlice of first 5 item ")
    print(list[0:5])   #Ranges  in python are non inclusive , so 5th element will not print
    
    #Ranges  in python are non inclusive
    print("\nRanges  in python are non inclusive")
    for i in range(0, 10): 
        print(i,end=" ")
    
    list[:]=range(100)
    print(list)
    
    #first argument 
    print("First argument : list[25] :",list[25])
    #Second argument in range in the slice is a range 
    print("Second argument : list[25:50] :",list[25:50])
    #third argument will step 
    print("third argument : list[25:50:5] :",list[25:50:5])
    
    print("We can assign value to slice")
    list[25:50:5]=(99, 99, 99, 99, 99)
    print("List : ",list)
    
    
    
        
if __name__ == "__main__": main()
