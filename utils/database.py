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
            dbCommand = "CREATE TABLE IF NOT EXISTS Pets ( petID INTEGER, location TEXT, petType TEXT, color TEXT, eyeColor TEXT, img TEXT, description TEXT, dataLost TEXT, petName TEXT );"
            self.cursor.execute(dbCommand)
            self.db.commit()

    def pull( self ):
        
