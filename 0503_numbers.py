#!/usr/bin/python
#0503numbers.py by Sujit Dhamale

def main():
    num=12
    print(type(num),num)

    num=12.2
    print(type(num),num)

    num=12/7
    print(type(num),num)

    num=12/2
    print(type(num),num)

    #to get integer division use "//" but it will not rounded up
    num=12//7
    print(type(num),num)

    #to get  rounded up  use function  round
    num=round(12/7)
    print(type(num),num)

    
    #specify number of digit to be rounded up by adding one more paramter
    num=round(12/7,4)
    print(type(num),num)


    #to get remainder (Modulo)  use "%"
    num=12%7
    print(type(num),num)

    #to convert data type from  float to integer use function int()
    num=int(12.6)
    print(type(num),num)

    #to convert data type from  integer to float use function float()
    num=float(12)
    print(type(num),num)

   
if __name__ == "__main__": main()
