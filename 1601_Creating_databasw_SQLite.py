#!/usr/bin/python
#1601_Creating_databasw_SQLite.py by Sujit Dhamale
#to understand Creating a database with SQLite 3

import sqlite3

def main():
    db=sqlite3.connect('1601_SQlite.db')
    db.execute('drop table if exists test')
    db.execute('create table test(t1 text,i1 int)')
    db.execute('insert into test(t1,i1) values (?,?)',('one',1))
    db.execute('insert into test(t1,i1) values (?,?)',('two',2))
    db.execute('insert into test(t1,i1) values (?,?)',('Three',3))
    db.execute('insert into test(t1,i1) values (?,?)',('Four',4))
    db.execute('insert into test(t1,i1) values (?,?)',('Five',5))
    db.commit()
    
    cursor=db.execute('select * from test order by i1')
    for row in cursor:
        print(row)
       
    
    
if __name__ == "__main__": main()



