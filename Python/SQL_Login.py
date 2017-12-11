#-*- coding: utf-8 -*-
# @author = Kornel Wojtasiak
import pymysql
import Login

connect = pymysql.connect(Login.dataLogin["host"], Login.dataLogin["user"], Login.dataLogin["pass"], Login.dataLogin["db"], use_unicode = 1, charset ="utf8")
cdb = connect.cursor()



cdb.execute("SELECT * from station_data")


#print(cdb.fetchone())  # pierwszy wpis z tabeli
print(cdb.fetchall())
#print(cdb.rowcount)   #liczba rekordów tabeli