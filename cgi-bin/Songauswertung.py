import cgi
from pymysql import *
from logIn import currentAccount

AccountNum = currentAccount

class Auswertung():
    def setListenedTimes():
        

        if AccountNum == 0:
            return 0
        elif AccountNum > 0:
            con = connect(host="localhost", user="root", passwd="")
            cur = con.cursor()
            cur.execute("use abschlusprojektq2")

            i =1
            while i <= cur.execute("SELECT COUNT (*) FROM songs"):
                timesListened2Song = cur.execute("SELECT COUNT (*) FROM listened WHERE UserNr='" +AccountNum+ "' AND SongNr='"+i+ "'")
                try:
                    cur.execute("UPDATE hoert SET" +i+ "='" +timesListened2Song+ "'")
                    con.commit
                    print(i + "-->")
                    i = i+1
                    print(i)
                except:
                    cur.execute("ALTER TABLE hoert ADD" +i+ " int")
                    continue


      

            con.close()
            object.setFavoriteStuff


    def setFavoriteStuff():
        con = connect(host="localhost", user="root", passwd="")
        cur = con.cursor()
        cur.execute("use abschlusprojektq2")


#Favorite Song
        i=1
        while i < cur.execute("SELECT COUNT (*) FROM songs"):
            j=i+1
            while cur.execute("SELECT COUNT (*) FROM listened WHERE UserNr='" +AccountNum+ "' AND SongNr='"+i+ "'") > cur.execute("SELECT COUNT (*) FROM listened WHERE UserNr='" +AccountNum+ "' AND SongNr='"+i+ "'"):
                j = j+1
                favoriteSong = cur.execute("SELECT Titel FROM songs WHERE SongNr='"+i+ "'")
                cur.execute("UPDATE user SET favoriteSong='" +favoriteSong+ "' WHERE UserNr='" +AccountNum+ "'")
                con.commit()

            i=j

        i=1
#Favorite Band 
        # - Make a list of all Bands
        while i < cur.execute("SELECT COUNT (*) FROM songs"):
            bandsName = cur.execute("SELECT Interpred FROM srongs WHERE SongNr ='" +i+ "'")
            ListOfBands = []
            k = 0
            while ListOfBands[k] != bandsName:
                k=k+1
                if k == len(ListOfBands)+1:
                    ListOfBands.append(bandsName)
                    break
            i=i+1


        # - Sort out favorite Band
        k=0
        while i < cur.execute("SELECT COUNT (*) FROM songs"):
            l=k+1
            while cur.execute("SELECT COUNT listened.SongNr FROM listened, songs WHERE =' listened.UserNr='" +AccountNum+ "', listened.SongNr=songs.SongNr, songs.Interpret='"+ListOfBands[k]+ "'") > cur.execute("SELECT COUNT listened.SongNr FROM listened, songs WHERE =' listened.UserNr='" +AccountNum+ "', listened.SongNr=songs.SongNr, songs.Interpret='"+ListOfBands[l]+ "'"):
                l+1
                if k==len(ListOfBands):
                    favoriteBand = ListOfBands[k]
                    cur.execute("UPDATE user SET favoriteBand='" +favoriteBand+ "' WHERE UserNr='" +AccountNum+ "'")
                    con.commit()
            i=i+1
            k=l

#Favorite Musik
            

            




    
        








object=Auswertung()
object.setListenedTimes
