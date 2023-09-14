import streamlit as st
from quickstart import Drive_OCR
import time
db=Drive_OCR("").google_spreadsheet_get("13Aw2HghuOauGAjnxgD5YvBYo7Ysda-TprTJ_BLHuIPA","A:N")

st.set_page_config()

ph = st.empty()
N = len(db)*30
if ["timer"] not in st.session_state:
	st.session_state["timer"]=N

	
for x in db:
	z=[]
	for y in x[1:-3]:
		if y!="":
			z.append(y)
	st.selectbox(x[0],z)

st.write("Thanks")
@st.experimental_memo
def timer(M):
	for secs in range(N,0,-1):
		mm, ss = secs//60, secs%60
		ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
		time.sleep(1)
		st.session_state["timer"]=N

timer(st.session_state["timer"])
    
