import streamlit as st
import time,os

if "sc" not in os.environ:
	os.environ["sc"]="0"
con=os.environ["sc"]
os.environ["sc"]=str(int(con)+1)
st.write(os.environ["sc"])

st.button("Reset", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
    st.rerun()	
else:
    st.write('Goodbye')
    
time.sleep(5)
st.write("sleep for 5 sec")
    