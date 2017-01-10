import sqlite3

class database:

    def __init__(self):
        self.db = sqlite3.connect("data/discobandit.db");
        self.cursor = self.db.cursor;
        
    def clone(self, remove=False):
        if remove:
            dbCommand = "DELETE * FROM ListOfPetsFound;"
            self.cursor.execute(dbCommand)
            dbCommand = "DELETE * FROM ListofPetsLost;"
            self.cursor.execute(dbCommand)
            self.db.commit()
        else:
            dbCommand = "CREATE TABLE IF NOT EXISTS ListOfPetsFound ( petID INTEGER, founderEmail TEXT );"
            self.cursor.execute(dbCommand)
            dbCommand = "CREATE TABLE IF NOT EXISTS ListOfPetsLost ( petID INTEGER, ownerEmail TEXT );"
            self.cursor.execute(dbCommand)
            dbCommand = "CREATE TABLE IF NOT EXISTS Pets ( petID INTEGER, location TEXT, petType TEXT, color TEXT, eyeColor TEXT, img TEXT, description TEXT, dateLost TEXT, petName TEXT );"
            self.cursor.execute(dbCommand)
            self.db.commit()

    def pull( self, flag ):
        if( flag == "-l"):
            dbCommand = "SELECT * FROM Pets, ListOfPetsLost WHERE Pets.petID = ListOfPetsLost.petID;"
            data = self.cursor.execute(dbCommand)
            return data
        elif( flag == "-f"):
            dbCommand = "SELECT * FROM Pets, ListOfPetsFound WHERE Pets.petID = ListOfPetsFound.petID;"
            data = self.cursor.execute(dbCommand)
            return data
        else:
            print("Flag not found")

    def add( self, petData, userInfo): #petData is a dictionary
        #Assume that all fields are filled in, with "" if necessary
        #Assume petID is generated beforehand
        dbCommand = "INSERT INTO Pets VALUES (%d, %s, %s, %s, %s, %s, %s, %s, %s)"%(petData['petID'], petData['location'], petData['petType'], petData['color'], petData['eyeColor'], petData['img'], petData['description'], petData['dateLost'], petData['petName'])
        self.cursor.execute(dbCommand)
        if( 'ownerEmail' in userInfo):
            dbCommand = "INSERT INTO ListOfPetsLost VALUES (%d, %s)"%(petData['petID'], userInfo['ownerEmail'])
            self.cursor.execute(dbCommand)
        elif( 'founderEmail' in userInfo):
            dbCommand = "INSERT INTO ListOfPetsFound VALUES (%d, %s)"%(petData['petID'], userInfo['foundEmail'])
            self.cursor.execute(dbCommand)
        self.db.commit()

    def remove( self, petID ):
        dbCommand = "DELETE * FROM Pets, ListOfPetsLost, ListOfPetsFound WHERE petID = %d"%(petID)
        self.cursor.execute(dbCommand)
        self.db.commit()

    def push(self):
        self.db.commit()
        self.db.close()
