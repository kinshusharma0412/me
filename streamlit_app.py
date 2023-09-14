import streamlit as st
from quickstart import Drive_OCR
import time
db=Drive_OCR("").google_spreadsheet_get("13Aw2HghuOauGAjnxgD5YvBYo7Ysda-TprTJ_BLHuIPA","A:N")

st.set_page_config()

ph = st.empty()
N = len(db)*30


for x in db:
	z=[]
	for y in x[1:-1]:
		if y!="":
			z.append(y)
	st.selectbox(x[0],z)
#submitted = st.form_submit_button("Submit")
#if submitted:
#st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Thanks")
for secs in range(N,0,-1):
    mm, ss = secs//60, secs%60
    ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
    time.sleep(1)
    
#import os

#os.system("python -m venv .venv & pip install streamlit")
#os.system("python aa.py")
#os.system("/home/adminuser/venv/bin/python aa.py")