#!/usr/bin/python
#1701_Using_standard_library_modules.py by Sujit Dhamale
#to understand Using standard library modules

import sys

def main():
    print("python version : {}.{}.{}".format(*sys.version_info))
    print("Current OS Service :",sys.platform)

    
    import os
    print("OS name :",os.name)
    print("Environment Variable PATH :",os.getenv('PATH'))
    print("current Working dir ",os.getcwd())
    print(os.__file__)
     
#     import urllib.request
#     page=urllib.request.urlopen('http://www.python.org')
#     print(page)
#     for line in page:
#         #print(line)
#         print(str(line,encoding='utf_8'),end=' ')
    
    import datetime
    now=datetime.datetime.now()
    print(now)
    print(now.year,now.month,now.day,now.hour,now.minute,now.second,now.microsecond)
    print(datetime.__file__)
    
    
if __name__ == "__main__": main()



