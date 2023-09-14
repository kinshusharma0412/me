import streamlit as st
from quickstart import Drive_OCR
import time
query=st.experimental_get_query_params()
db=Drive_OCR("").google_spreadsheet_get("13Aw2HghuOauGAjnxgD5YvBYo7Ysda-TprTJ_BLHuIPA","A:N")
print(query)
#db=Drive_OCR("").google_spreadsheet_get(query["id"],"A:N")

st.set_page_config()


ph = st.empty()
N = len(db)*30
if query["id"]+query["user"] not in st.session_state:
	st.session_state[query["id"]+query["user"]]=N

	
for x in db:
	z=[]
	for y in x[1:-3]:
		if y!="":
			z.append(y)
	st.selectbox(x[0],z)

st.write("Thanks")
st.write(query)
if st.session_state[query["id"]+query["user"]]>0:
	for secs in range(st.session_state[query["id"]+query["user"]],-1,-1):
		mm, ss = secs//60, secs%60
		ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
		time.sleep(1)
		st.session_state[query["id"]+query["user"]]=secs-2
		if secs<1:
			ph.metric("Times Up!!")


    
