from flask import Flask, render_template, request, redirect, url_for
import json
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
    if not db:
        return redirect( url_for('home'))
    data = db.pullFoundData("WHERE Pets.petID = ListOfPetsFound.petID")
    return render_template("found.html", data = data)

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

@app.route("/updateFound/", methods=['POST'])
def updateFound():
    formData = json.loads(request.form.get('formData'))
    print formData
    result = {}
    for item in formData:
        result[item['name']] = item['value']
    string = "WHERE Pets.petID = ListOfPetsFound.petID"
    if('location' in result and result['location'] != "" ):
        string += " AND Pets.location = %s OR Pets.location = ''"%(result['location'].lower());
    if('petType' in result and result['petType'] != "" ):
        string += " AND Pets.petType = %s OR Pets.petType = ''"%(result['petType'].lower());
    if('color' in result and result['color'] != "" ):
        string += " AND Pets.color = %s OR Pets.color = ''"%(result['color'].lower());
    if('eyeColor' in result and result['eyeColor'] != "" ):
        string += " AND Pets.eyeColor = %s OR Pets.eyeColor = ''"%(result['eyeColor'].lower());
    #if('img' in result and result['img'] != "" ):
    #    string += " AND Pets.img = %s OR Pets.img != ''"%(result['location']);
    #if('description' in result and result['description'] != "" ):
    #    string += " AND Pets.location = %s OR Pets.location != ''"%(result['location']);
    #if('dateLost' in result and result['dateLost'] != "" ):
    #    string += " AND Pets.location = %s OR Pets.location != ''"%(result['location']);
    if('petName' in result and result['petName'] != "" ):
        string += " AND Pets.petName = %s OR Pets.petName = ''"%(result['petName'].lower());
    print string
    data = db.pullFoundData(string);
    print data
    print "\n\n\n\n\n"
    return render_template("found.html", data = data, temp = result);
    
        
@app.route("/remove/")
def remove():
    global db
    db = Database(True)
    
    
if __name__ == "__main__":
    app.debug = True
    app.url_map.strict_slashes = False
    db = None
    app.run(host='0.0.0.0')
