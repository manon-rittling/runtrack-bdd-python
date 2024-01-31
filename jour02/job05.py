import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="laplateforme"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT SUM(superficie) FROM etage")

resultat = mycursor.fetchall()
superficie_totale = resultat[0][0]
message = "La superficie totale de tous les étages est de " + str(superficie_totale) + " m²."    
print(message)