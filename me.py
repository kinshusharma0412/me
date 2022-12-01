from flask import Flask, render_template      
import streamlit as st
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"

st.write(app.run())