#!/usr/bin/python
#1502_Reading_and_writing_text_files.py by Sujit Dhamale
#to understand how to Reading and writing text files 


def main():
    #Simple way to Write file 
    infile=open('1500_file.txt','r')
    outfile=open('1500_newfile.txt','w')  
    for line in infile:
        print(line,file=outfile,end='')
    print("Done  --")
    
    #processing big file in buffred mode
    buffersize=5000                        #this is 5000 bytes
    infile=open('1502_bigfile.txt','r')
    outfile=open('1502_bigfile_out.txt','w')    
    
    buffer=infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print("# ",end=" ")
        buffer=infile.read(buffersize)
        
    print("\nDone")
    
    
    
    
if __name__ == "__main__": main()



