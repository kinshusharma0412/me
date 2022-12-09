from flask import Flask, render_template      
import re
app = Flask(__name__)

#@app.route("/")
def home():
    return render_template("home.html")
 
@app.route('/<id>')
def success(id):
    return render_template("home.html",name=id)
    
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"

app.run()