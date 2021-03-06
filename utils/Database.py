import sqlite3

class Database:

    def __init__(self, remove=False):
        self.db = sqlite3.connect("data/discobandit.db");
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor();
        if remove:
            self.removeDatabase()
        self.initDatabase()
        print "Initialized tables"
        
    def initDatabase(self):
        dbCommand = "CREATE TABLE IF NOT EXISTS ListOfPetsFound (petID INTEGER, founderName TEXT, founderEmail TEXT);"
        self.cursor.execute(dbCommand)
        dbCommand = "CREATE TABLE IF NOT EXISTS ListOfPetsLost (petID INTEGER, ownerName TEXT, ownerEmail TEXT );"
        self.cursor.execute(dbCommand)
        dbCommand = "CREATE TABLE IF NOT EXISTS Pets (petID INTEGER, location TEXT, petType TEXT, color TEXT, eyeColor TEXT, img TEXT, description TEXT, dateLost TEXT, petName TEXT);"
        self.cursor.execute(dbCommand)
        self.db.commit()
        
    def removeDatabase(self):
        dbCommand = "DELETE * FROM ListOfPetsFound;"
        self.cursor.execute(dbCommand)
        dbCommand = "DELETE * FROM ListofPetsLost;"
        self.cursor.execute(dbCommand)
        self.db.commit()

    def saveDatabase(self):
        self.db.commit()
        self.db.close()
        
    def pullLostData(self, pullRequest=None, pullRequestSubsitutionSequence=None):
        defaultCommand = "SELECT * FROM Pets, ListOfPetsLost"
        if pullRequest:
            dbCommand = defaultCommand + " " + pullRequest + ";"
        else:
            dbCommand = defaultCommand + ";"
        if pullRequestSubsitutionSequence:
            self.cursor.execute(dbCommand, pullRequestSubsitutionSequence)
        else:
            self.cursor.execute(dbCommand)
        data = self.cursor.fetchall()
        return data

    def pullFoundData(self, pullRequest=None, pullRequestSubsitutionSequence=None):
        defaultCommand = "SELECT * FROM Pets, ListOfPetsFound"
        if pullRequest:
            dbCommand = defaultCommand + " " + pullRequest + ";"
        else:
            dbCommand = defaultCommand + ";"
        if pullRequestSubsitutionSequence:
            self.cursor.execute(dbCommand, pullRequestSubsitutionSequence)
        else:
            self.cursor.execute(dbCommand)
        data = self.cursor.fetchall()
        return data

    def generateNextPetID(self):
        dbCommand = "SELECT * FROM Pets ORDER BY petID DESC LIMIT 1;"        
        self.cursor.execute(dbCommand)
        lastID = self.cursor.fetchall()
        if len(lastID) != 0 :
            return lastID[0]['petID'] + 1
        else:
            return 0
    
    def addPet(self, petData, userInfo):
        '''
        petData is a dictionary with non-empty fields (fill with "" if necessary)
        Assume that petID is pre-generated
        '''
        dbCommand = "INSERT INTO Pets VALUES (%d, \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\");"%(petData['petID'], petData['location'], petData['petType'], petData['color'], petData['eyeColor'], petData['img'], petData['description'], petData['dateLost'], petData['petName'])
        self.cursor.execute(dbCommand)
        if 'ownerEmail' in userInfo:
            dbCommand = "INSERT INTO ListOfPetsLost VALUES (%d, \"%s\", \"%s\");"%(petData['petID'], userInfo['ownerName'], userInfo['ownerEmail'])
            self.cursor.execute(dbCommand)
        elif 'founderEmail' in userInfo:
            dbCommand = "INSERT INTO ListOfPetsFound VALUES (%d, \"%s\", \"%s\");"%(petData['petID'], userInfo['founderName'], userInfo['founderEmail'])
            self.cursor.execute(dbCommand)
        self.db.commit()

    def removePet( self, petID ):
        dbCommand = "DELETE * FROM Pets, ListOfPetsLost, ListOfPetsFound WHERE petID = %d;" % (petID)
        self.cursor.execute(dbCommand)
        self.db.commit()
