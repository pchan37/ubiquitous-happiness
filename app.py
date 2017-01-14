from flask import Flask, render_template
from utils.Database import Database

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
def petInfo(petID):
    db = Database()
    data = db.pullFoundData("WHERE Pets.petID = %d AND Pets.petID = ListOfPetsFound.petID"%(int(petID)))
    if (not any(data)):
        data = db.pullLostData("WHERE Pets.petID = %d AND Pets.petID = ListOfPetsLost.petID"%(int(petID)))
    if( data != [] ):
        data = data[0];
        return render_template("pet.html",  location = data['location'], petType = data['petType'], color = data['color'], eyeColor = data['eyeColor'], img = data['img'], description = data['description'], dateLost = data['dateLost'], petName = data['petName'] )
    else:
        return "petID not on record"
@app.route("/petTest/")
def petTest( ):
    return render_tempate("pet.html")

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
