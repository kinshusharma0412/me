from flask import Flask, render_template      
from multiprocessing import Process
import streamlit as st
import SessionState
import time
import os
import signal

st.sidebar.title("Controls")
start = st.sidebar.button("Start")
stop = st.sidebar.button("Stop")

state = SessionState.get(pid=None)


def job():
    for _ in range(100):
        print("In progress")
        time.sleep(1)


if start:
    p = Process(target=job)
    p.start()
    state.pid = p.pid
    st.write("Started process with pid:", state.pid)

if stop:
    os.kill(state.pid, signal.SIGKILL)
    st.write("Stopped process with pid:", state.pid)
    state.pid = None


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"

app.run(port=8887)