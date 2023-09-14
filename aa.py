

import streamlit as st
from quickstart import Drive_OCR
db=Drive_OCR("").google_spreadsheet_get("13Aw2HghuOauGAjnxgD5YvBYo7Ysda-TprTJ_BLHuIPA","A:N")

st.write(1234)
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
        