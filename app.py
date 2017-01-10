from flask import Flask, render_template

app = Flask(__name__)

#this one will have notifications and such via javascript
@app.route("/")
def home():
	return render_template("home.html")

@app.route("/found")
def found():
	return render_template("found.html")

@app.route("/lost")
def lost():
	return render_template("lost.html")

if __name__ == "__main__":
	app.debug = True
	app.run()
