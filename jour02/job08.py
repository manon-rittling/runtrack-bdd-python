import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="zoo"
)

class Directeur:
    def __init__(self, nom, race, id_type_cage, date_anniversaire, pays_origine, superficie, capacite):
        
        self.nom = nom
        self.race = race
        self.id_type_cage = id_type_cage
        self.date_anniversaire = date_anniversaire
        self.pays_origine = pays_origine
        self.superficie = superficie
        self.capacite = capacite
        self.id = None

    

    def createAnimal(self):
        cursor = mydb.cursor()
        ajout = "INSERT INTO animal (nom, race, id_type_cage, date_anniversaire, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        valeur = (self.nom, self.race, self.id_type_cage, self.date_anniversaire, self.pays_origine)
        cursor.execute(ajout, valeur)
        mydb.commit()

    def createCage(self):
        cursor = mydb.cursor()
        ajout = "INSERT INTO cage (superficie, capacite) VALUES (%s, %s)"
        valeur = (self.superficie, self.capacite)
        cursor.execute(ajout, valeur)
        mydb.commit()

    def updateAnimal(self, nom, race, id_type_cage, date_anniversaire, pays_origine):
        cursor = mydb.cursor()
        modifier = "UPDATE animal SET race=%s, id_type_cage=%s, date_anniversaire=%s, pays_origine=%s WHERE nom=%s"
        valeur = (race, id_type_cage, date_anniversaire, pays_origine, nom)
        cursor.execute(modifier, valeur)
        mydb.commit()

    def updateCage(self):
        cursor = mydb.cursor()
        modifier = "UPDATE cage SET superficie=%s, capacite=%s WHERE id=%s"
        valeur= (self.superficie, self.capacite, self.id)
        cursor.execute(modifier, valeur)
        mydb.commit()

    def deleteAnimal(self):
        cursor = mydb.cursor()
        supprimer = "DELETE FROM animal WHERE nom=%s"
        valeur = (self.nom,)
        cursor.execute(supprimer, valeur)
        mydb.commit()

    def deleteCage(self):
        cursor = mydb.cursor()
        supprimer = "DELETE FROM cage WHERE id=%s"
        valeur = (self.id,)
        cursor.execute(supprimer, valeur)
        mydb.commit()

    def readAnimal(self):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM animal")
        result = cursor.fetchall()
        print(result)

    def readCage(self):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM cage")
        result = cursor.fetchall()
        print(result)


    def total_superficie(self):
        cursor = mydb.cursor()
        cursor.execute("SELECT SUM(superficie) FROM cage")
        result = cursor.fetchall()[0]
        superficie_total = result[0]
        print(superficie_total)
        
        

    def afficher_animaux(self):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM animal INNER JOIN cage ON animal.id_type_cage = cage.id")
        result = cursor.fetchall()
        print(result)











    
