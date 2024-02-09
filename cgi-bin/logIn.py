#!C:/Python35/python.exe
import cgi
from pymysql import *


currentAccount=0

class Formular_einlesen:
      def __init__(self):
         self.benutzername=""
         self.password=""
         self.checkAccount=""
         
      def db(self):
         con = connect(host="localhost", user="root", passwd="")
         cur = con.cursor()
         cur.execute("use abschlusprojektq2")

         self.checkAccount = cur.execute("SELECT Passwort FROM user WHERE Benutzername='"+self.benutzername+"'")

         while 1:
            if (self.checkAccount == self.password):
                  print("Hallo User")
                  self.currentAccount = cur.execute("SELECT UserNr FROM user WHERE Benutzername=" +self.benutzername+ ", Passwort=" +self.password)
                  self.ausgabe()
            else: 
                 self.fehler()
      

         con.close()



      def fehler(self):
            print ("Content-Type: text/html")
            print()
            print('<!DOCTYPE html>\
                  <html>')
            print ('<head>\
               <title> Fehlermeldung </title>\
               <link rel="stylesheet" type="text/css" href="../Wilkommensseite.css"/>\
               </head>\
               <body>\
               <h1>Es ist ein Fehler aufgetreten:</h1>\
               <p>Bitte alle Felder ausf&uuml;llen!</p>\
               <p>\
               <input type="submit" value="Zur&uuml;ck" onclick = "history.back()" />\
               </p>\
               </body>\
               </html>')

      def auswertung(self):
            form = cgi.FieldStorage()
            if "Benutzername" in form:
                  self.benutzername = form["Benutzername"].value
            if "Passwort" in form:
                  self.password = form["password"].value
            if  (self.benutzername=="" or self.password==""):
               self.fehler()
            



      def ausgabe(self):
            self.db()
            print ("Content-Type: text/html")
            print()
            print('<!DOCTYPE html>\
                  <html>')
            print ('<head>\
                  <title>Anmeldung erfolgreich</title>\
                  <link rel="stylesheet" type="text/css" href="../Wilkommensseite.css"/>\
                  </head>\
                  <body>\
                  <h1>Herzlich willkommen, '+self.benutzername+', AccountNr: '+self.currentAccount+' !</h1>\
                  <p><div class = "text">Sie sind jetzt angemeldet!\
                  <p>\
                  <input type="submit" value="Zur&uuml;ck" onclick = "history.back()" />\
                  </p>\
                  </body>\
                  </html>')
            

objekt=Formular_einlesen()
objekt.auswertung()