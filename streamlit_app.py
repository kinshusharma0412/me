import streamlit as st
from quickstart import Drive_OCR
import time,os, string,xlsxwriter
query=st.experimental_get_query_params()
#db=Drive_OCR("").google_spreadsheet_get("13Aw2HghuOauGAjnxgD5YvBYo7Ysda-TprTJ_BLHuIPA","A:N")
print(query)
db=Drive_OCR("").google_spreadsheet_get(query["id"][0],"Sheet1!A:N")
 
cell2=xlsxwriter.utility.xl_col_to_name(len(db)+3)

st.set_page_config()


ph = st.empty()
N = len(db)*30
if query["id"][0]+query["user"][0] not in os.environ:
	os.environ[query["id"][0]+query["user"][0]]=str(N)

btn=[]	
for x in db:
	z=[]
	for y in x[1:-3]:
		if y!="":
			z.append(y)
	
	btn.append(st.selectbox(x[0],z))

st.write("Thanks")


db2=Drive_OCR("").google_spreadsheet_get(query["id"][0],"Sheet2!A:"+cell2)
ids=[]
for x in db2:
	ids.append(x[1])

data=["Name",query["user"][0],N]
for x in btn:
	data.append(x)

db2.append(data)
if query["user"][0] not in ids:
	Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
else:
	i=0
	for x in ids:
		if str(query["user"][0]) ==str(x):
			break
		i+=1
	st.write(i)
	db2[i]=["Name",query["user"][0],int(os.environ[query["id"][0]+query["user"][0]])].extend(btn)
	
	st.write(db2)
	print(str(db2))
	Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
	
	
	
	
if int(os.environ[query["id"][0]+query["user"][0]])>0:
	for secs in range(int(os.environ[query["id"][0]+query["user"][0]]),-1,-1):
		mm, ss = secs//60, secs%60
		ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
		time.sleep(1)
		os.environ[query["id"][0]+query["user"][0]]=str(secs-2)
		if secs<1:
			ph.write("Times Up!!")
			ph.write(btn)
else:
	ph.write(btn)
		

    
