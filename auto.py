#!/usr/bin/python
import csv
import os
import re
def main():
    typeofObject=["source","target","transformation","mapplet","mapping","session","workflow","sources","targets","transformations","mapplets","mappings","sessions","workflows"]
    out = open("objects_input.env", 'w')
    f = open("input.txt", 'rt')
    reader = csv.reader(f,delimiter='\t')
    for row in reader:
        #print("\n\n2")
        #print("Length ==",len(row))
        #print("row ==",row)
        #print("objectType ==",row[1].lower().strip())
        #print(row[3].lower().strip())
        if (len(row)==9 and row[1].lower().strip() in typeofObject and 'refresh' not in row[4].lower().strip()):
            objectType=row[1].lower().strip()
            if(objectType[len(objectType)-1]=='s'):
                objectType=objectType[:-1]
            objectName=row[0].strip()
            location=re.sub(r'.*:',r'',row[6].strip())
            #print("location==",location)
            #print("objectType==",objectType)
            print("objectName==",objectName)
            #print("row[3].lower().strip()==",row[3].lower().strip())
            devDomainName=location.split('.')[0]
            devFolderName=location.split('.')[1]
            #print("\n\n Location length",len(location.split('.')))
            #print("objectType={0},objectName={1},location={2},devDomainName={3},devFolderName='{4}".format(objectType,objectName,location,devDomainName,devFolderName))
            if((objectType=="source" or objectType=="sources") and len(location.split('.'))==4):
                objectName=r"{0}.{1}".format(location.split('.')[3],objectName)
                #print("objectName",objectName)
            location=re.sub(r'.*:',r'',row[8].lower().strip())
            prodDomainName=location.split('.')[0]
            testDomainName=prodDomainName.replace('prod','test')
            prodFolderName=location.split('.')[1]

            data ="{0}|{1}|{2}|{3}|{4}|{5}".format(objectName,objectType,devDomainName,devFolderName,testDomainName,prodFolderName)
            #print(data)
            out.write(data+"\n")
            
        elif ('refresh' in row[4].lower().strip()):
        	objectName=row[0].strip()
        	objectType=row[1].lower().strip()
        	devDomainName=location.split('.')[0]
        	devFolderName=location.split('.')[1]
        	testDomainName=prodDomainName.replace('prod','test')
        	prodFolderName=location.split('.')[1]
        	print(objectName,objectType,devDomainName,devFolderName,testDomainName,prodFolderName)
        	
        	
        	
        	
        	
        	
        	      


        else :
            continue



                #print("%s==> %s ==devDomainName> %s  ==devFolderName> %s" %(objectName,location,devDomainName,devFolderName))
                #print("%s==> %s " %(objectName,location))
                #print(location)
                #print("data==",data)
                #out.write(data+"\n")



    out.close()
    f.close()

if __name__ =="__main__" : main()
