from flask import Flask, render_template
from utils import database

app = Flask(__name__)

#this one will have notifications and such via javascript
@app.route("/")
def home():
	return render_template("home.html")

@app.route("/found/")
def found():
	return render_template("found.html")

@app.route("/lost/")
def lost():
	return render_template("lost.html")

@app.route("/pet/<petID>")
def petInfo( petID ):
        db = database.__init__( __name__ )
        data = database.pullFoundData(db, "WHERE Pets.petID = %d AND Pets.petID = ListOfPetsFound.petID"%(petID));
        if ( not any(data) ):
                data = database.pullLostData(db, "WHERE Pets.petID = %d AND Pets.petID = ListOfPetsLost.petID"%(petID))
        return render_template("pet.html",  location = data['location'], petType = data['petType'], color = data['color'], eyeColor = data['eyeColor'], img = data['img'], description = data['description'], dateLost = data['dateLost'], petName = data['petName'] )


@app.route("/petTest/")
def petTest( ):
        return render_tempate("pet.html")
        
if __name__ == "__main__":
        app.debug = True
	app.run()
