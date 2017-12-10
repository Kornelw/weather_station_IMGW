#-*- coding: utf-8 -*-
# @author = Kornel Wojtasiak
import pymysql
import Login

connect = pymysql.connect(Login.dataLogin["host"], Login.dataLogin["user"], Login.dataLogin["pass"], Login.dataLogin["db"], use_unicode = 1, charset ="utf8")

c = connect.cursor()
c.execute("SELECT * from station_data")
print(c.fetchone())  # pierwszy wpis z tabeli
print(c.fetchone())
print(c.rowcount)   #liczba rekordów tabeli