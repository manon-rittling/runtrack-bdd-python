import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="colab"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM employe WHERE salaire > 3000")

resultat = mycursor.fetchall()
print(resultat)

cursor = mydb.cursor()
cursor.execute ("SELECT employe.nom,prenom, service.nom FROM employe INNER JOIN service ON employe.id_service = service.id ")
resultat2 = mycursor.fetchall()
message = "voici le service de chaque employe" + str(resultat2)
print(message)

class salarie:
    def __init__(self, nom, prenom, salaire, id_service):
        
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.id_service = id_service

    def create(self):
        cursor = mydb.cursor()
        sql = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        val = (self.nom, self.prenom, self.salaire, self.id_service)
        cursor.execute(sql, val)
        mydb.commit()

    def read(self):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM employe")
        result = cursor.fetchall()
        print(result)

    def update(self, nom, prenom, salaire, id_service):
        cursor = mydb.cursor()
        cursor.execute("UPDATE employe SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE nom = %s", (nom, prenom, salaire, id_service, self.nom))
        mydb.commit()

    def delete(self):
        cursor = mydb.cursor()
        cursor.execute("DELETE FROM employe WHERE nom = %s", (self.nom,))
        mydb.commit() 


employe = salarie("Renoul", "Jean", 3150.75, 2)

employe.read()
employe.update("Renoul", "Jean", 3350.75, 2)
employe.read()
