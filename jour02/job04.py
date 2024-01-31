import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="laplateforme"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT Nom,capacite FROM salle" )

resultat = mycursor.fetchall()
print(resultat)

mycursor.close()
mydb.close()