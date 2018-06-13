#!/usr/bin/python
#1503_Reading_and_writing_binary_files.py by Sujit Dhamale
#to understand how to Reading and writing binary files

def main():
    #Simple way to read inary file 
    infile=open('python.png','rb')
    outfile=open('python2.png','wb') 
    for line in infile:
        outfile.write(line)
        #print(line)
    print("Done  --")
    
    #processing binary file in buffred mode
    buffersize=5000                        #this is 50000 bytes
    infile=open('python.png','rb')
    outfile=open('python1.png','wb')      
       
    buffer=infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print("# ",end=" ")
        buffer=infile.read(buffersize)
           
    print("\nDone")
       
       
    
    
if __name__ == "__main__": main()



