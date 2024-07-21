import mysql.connector
import pyodbc

# create database paises_db
#use paises_db
#create table countries(
#    id int identity(1,1) primary key,
#    ISO3 VARCHAR(3),
#    CountryName VARCHAR(100),
#    Capital varchar(50),
#    CurrencyCode varchar(3)
#);


class Countries:

    def __init__(self):
        self.cnn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=DESKTOP-DN8TPKA\\SQLEXPRESS;'
                                  'Database=paises_db;'
                                  'UID=root;'
                                  'PWD=1234;'
                                  )

    def __str__(self):
        datos=self.consulta_paises()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_paises(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM countries")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_pais(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM countries WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_pais(self,ISO3, CountryName, Capital, CurrencyCode):
        cur = self.cnn.cursor()
        sql='''INSERT INTO countries (ISO3, CountryName, Capital, CurrencyCode) 
        VALUES('{}', '{}', '{}', '{}')'''.format(ISO3, CountryName, Capital, CurrencyCode)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_pais(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM countries WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_pais(self,Id, ISO3, CountryName, Capital, CurrencyCode):
        cur = self.cnn.cursor()
        sql='''UPDATE countries SET ISO3='{}', CountryName='{}', Capital='{}',
        CurrencyCode='{}' WHERE Id={}'''.format(ISO3, CountryName, Capital, CurrencyCode,Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   
