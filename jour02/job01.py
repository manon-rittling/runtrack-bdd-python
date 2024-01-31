import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="laplateforme"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM etudiant")

etudiants = mycursor.fetchall()
print(etudiants)