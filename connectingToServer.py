hos="localhost"
dbname="stern"
use="postgres"
pas="a12AAAAA"

import psycopg2

table_name=input()
new_name=str(input())

def ConnectingCreatingAndInserting():
    try:
        conn=psycopg2.connect(host=hos,database=dbname,user=use,
                          password=pas)
        cur=conn.cursor()
        cur.execute("""CREATE TABLE {} (id VARCHAR(20), name VARCHAR(20),course NUMERIC);
                INSERT INTO {} (id,name,course) VALUES
                ('56','Daulet',1),
                ('42','Madi',2),
                ('58','Kanat',1);""".format(table_name,table_name))
        conn.commit()
        cur.close()
        conn.close()
    except:
        print("Entered name already exists!")
        
    
ConnectingCreatingAndInserting()

def UpdatingData():
    
    conn=psycopg2.connect(host=hos,database=dbname,user=use,password=pas)
    cur=conn.cursor()
    cur.execute("""UPDATE {}
                SET name='MADI'
                WHERE course>1;""".format(table_name))
    conn.commit()
    cur.close()
    conn.close()
        
    

UpdatingData()

def QueryingData():
    try:
        conn=psycopg2.connect(host=hos,database=dbname,user=use,
                          password=pas)
        cur=conn.cursor()
        cur.execute("SELECT * FROM {}".format(table_name))
        row=cur.fetchall()
        
    
        for i in row:
            
            print("""id={}
                  name={}
                  course{}""".format(i[0],i[1],i[2]))
        conn.commit()
        cur.close()
        conn.close()
    except:
        print("Error has occured")

QueryingData()

def DeletingData():
    try:
        conn=psycopg2.connect(host=hos,database=dbname,user=use,
                          password=pas)
        cur=conn.cursor()
        cur.execute("DELETE FROM {} WHERE name='MADI'".format(table_name))
        conn.commit()
        cur.close()
        conn.close()
    except:
        print("Error has occured")
    

DeletingData()
    
    
    

    
    
    
    

