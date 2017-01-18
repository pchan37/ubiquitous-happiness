from flask import Flask, render_template, request
from utils.Database import Database

app = Flask(__name__)

#this one will have notifications and such via javascript
@app.route("/")
def home():
    global db
    if not db:
        db = Database()
    return render_template("home.html")

@app.route("/found/")
def found():
    return render_template("found.html")

@app.route("/lost/")
def lost():
    return render_template("lost.html")

@app.route("/pet/<petID>")
def petInfo(petID):
    data = db.pullFoundData("WHERE Pets.petID = %d AND Pets.petID = ListOfPetsFound.petID" % (int(petID)))
    if not data:
        data = db.pullLostData("WHERE Pets.petID = %d AND Pets.petID = ListOfPetsLost.petID" % (int(petID)))
    if data:
        data = data[0];
        return render_template("pet.html",  location = data['location'], petType = data['petType'], color = data['color'], eyeColor = data['eyeColor'], img = data['img'], description = data['description'], dateLost = data['dateLost'], petName = data['petName'])
    else:
        return "petID not on record"

@app.route("/updateFound/")
def updateFound():
    formData = request.args();
    string = "WHERE Pets.petID = ListOfPetsFound.petID"
    if('location' in formData and formData['location'] != "" ):
        string += " AND Pets.location = %s OR Pets.location != ''"%(formData['location'].lower());
    if('petType' in formData and formData['petType'] != "" ):
        string += " AND Pets.petType = %s OR Pets.petType != ''"%(formData['petType'].lower());
    if('color' in formData and formData['color'] != "" ):
        string += " AND Pets.color = %s OR Pets.color != ''"%(formData['color'].lower());
    if('eyeColor' in formData and formData['eyeColor'] != "" ):
        string += " AND Pets.eyeColor = %s OR Pets.eyeColor != ''"%(formData['eyeColor'].lower());
    #if('img' in formData and formData['img'] != "" ):
    #    string += " AND Pets.img = %s OR Pets.img != ''"%(formData['location']);
    #if('description' in formData and formData['description'] != "" ):
    #    string += " AND Pets.location = %s OR Pets.location != ''"%(formData['location']);
    #if('dateLost' in formData and formData['dateLost'] != "" ):
    #    string += " AND Pets.location = %s OR Pets.location != ''"%(formData['location']);
    if('petName' in formData and formData['petName'] != "" ):
        string += " AND Pets.location = %s OR Pets.location != ''"%(formData['petName'].lower());
    
        
@app.route("/remove/")
def remove():
    global db
    db = Database(True)
    
    
if __name__ == "__main__":
    app.debug = True
    db = None
    app.run(host='0.0.0.0')
