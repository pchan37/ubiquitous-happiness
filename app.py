from flask import Flask, render_template, request, redirect, url_for
from json import loads
from utils.utils import convertFormArrayToDict, processDatabaseResponse
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
        return redirect(url_for('home'))
    data = db.pullFoundData("WHERE Pets.petID = ListOfPetsFound.petID")
    return render_template("found.html", data = data)

@app.route("/lost/")
def lost():
    if not db:
        return redirect(url_for('home'))
    data = db.pullLostData("WHERE Pets.petID = ListOfPetsLost.petID")
    return render_template("lost.html")

@app.route("/pet/<petID>")
def petInfo(petID):
    if not db:
        return redirect(url_for('home'))
    data = db.pullFoundData("WHERE Pets.petID = ? AND Pets.petID = ListOfPetsFound.petID", [petID])
    if not data:
        data = db.pullLostData("WHERE Pets.petID = ? AND Pets.petID = ListOfPetsLost.petID", [petID])
    if data:
        data = data[0];
        return render_template("pet.html", data=data)
    else:
        return "petID not on record"

@app.route("/updateFound/", methods=['POST'])
def updateFound():
    formDataArray = loads(request.form.get('formData'))
    formDataDictionary = convertFormArrayToDict(formDataArray)
    dbCommand = "WHERE Pets.petID = ListOfPetsFound.petID"
    substitutionSequence = []
    if formDataDictionary.get('petName'):
        dbCommand += " AND (Pets.petName LIKE ? OR Pets.petName LIKE '')"
        substitutionSequence.append('%' + formDataDictionary['petName'] + '%')
    if formDataDictionary.get('location'):
        dbCommand += " AND (Pets.location LIKE ? OR Pets.location LIKE '')"
        substitutionSequence.append('%' + formDataDictionary['location'] + '%')
    if formDataDictionary.get('petType'):
        dbCommand += " AND (Pets.petType LIKE ? OR Pets.petType LIKE '')"
        substitutionSequence.append('%' + formDataDictionary['petType'] + '%')
    if formDataDictionary.get('color'):
        dbCommand += " AND (Pets.color LIKE ? OR Pets.color LIKE '')"
        substitutionSequence.append('%' + formDataDictionary['color'] + '%')
    if formDataDictionary.get('eyeColor'):
        dbCommand += " AND (Pets.eyeColor LIKE ? OR Pets.eyeColor LIKE '')"
        substitutionSequence.append('%' + formDataDictionary['eyeColor'] + '%')
    # if formDataDictionary.get('img'):
    #     dbCommand += " AND (Pets.img LIKE ? OR Pets.color LIKE '')"
    #     substitutionSequence.append('%' + formDataDictionary['img'] + '%')
    # if formDataDictionary.get('description'):
    #     dbCommand += " AND (Pets.description LIKE ? OR Pets.description LIKE '')"
    #     substitutionSequence.append('%' + formDataDictionary['description'])
    if formDataDictionary.get('dateLost'):
        dbCommand += " AND (Pets.dateLost LIKE ? OR Pets.dateLost LIKE '')"
        substitutionSequence.append('%' + formDataDictionary['dateLost'] + '%')
    data = db.pullFoundData(dbCommand, substitutionSequence)
    return processDatabaseResponse(data)

@app.route("/submitFound/", methods=['POST'])
def submitFound():
    formData = request.form
    return render_template("confirm.html", data=formData, hidden="Found")

@app.route("/addFound/", methods=['POST'])
def addFound():
    formData = request.form.get('formData')
    

@app.route("/updateLost/", methods=['POST'])
def updateLost():
    formDataArray = loads(request.form.get('formData'))
    formDataDictionary = convertFormArrayToDict(formDataArray)
    dbCommand = "WHERE Pets.petID = ListOfPetsLost.petID"
    substitutionSequence = []
    if formDataDictionary.get('petName'):
        dbCommand += " AND (Pets.petName LIKE ? OR Pets.petName LIKE '')"
        substitutionSequence.append('%' + formDataDictionary['petName'] + '%')
    if formDataDictionary.get('location'):
        dbCommand += " AND (Pets.location LIKE ? OR Pets.location LIKE '')"
        substitutionSequence.append('%' + formDataDictionary['location'] + '%')
    if formDataDictionary.get('petType'):
        dbCommand += " AND (Pets.petType LIKE ? OR Pets.petType LIKE '')"
        substitutionSequence.append('%' + formDataDictionary['petType'] + '%')
    if formDataDictionary.get('color'):
        dbCommand += " AND (Pets.color LIKE ? OR Pets.color LIKE '')"
        substitutionSequence.append('%' + formDataDictionary['color'] + '%')
    if formDataDictionary.get('eyeColor'):
        dbCommand += " AND (Pets.eyeColor LIKE ? OR Pets.eyeColor LIKE '')"
        substitutionSequence.append('%' + formDataDictionary['eyeColor'] + '%')
    # if formDataDictionary.get('img'):
    #     dbCommand += " AND (Pets.img LIKE ? OR Pets.color LIKE '')"
    #     substitutionSequence.append('%' + formDataDictionary['img'] + '%')
    # if formDataDictionary.get('description'):
    #     dbCommand += " AND (Pets.description LIKE ? OR Pets.description LIKE '')"
    #     substitutionSequence.append('%' + formDataDictionary['description'])
    if formDataDictionary.get('dateLost'):
        dbCommand += " AND (Pets.dateLost LIKE ? OR Pets.dateLost LIKE '')"
        substitutionSequence.append('%' + formDataDictionary['dateLost'] + '%')
    data = db.pullLostData(dbCommand, substitutionSequence)
    return processDatabaseResponse(data)
    
@app.route("/remove/")
def remove():
    global db
    db = Database(True)
    
if __name__ == "__main__":
    app.debug = True
    app.url_map.strict_slashes = False
    db = None
    app.run(host='0.0.0.0')
