import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="laplateforme"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT SUM(capacite) FROM salle")

resultat = mycursor.fetchall()[0]
capacite_totale = resultat[0]

message = "La capacité totale de toutes les salles est de " + str(capacite_totale) + " places."
print(message)