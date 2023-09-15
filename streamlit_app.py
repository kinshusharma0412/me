import streamlit as st
#st.set_page_config()
from quickstart import Drive_OCR
import time,os, string,xlsxwriter
query=st.experimental_get_query_params()
#db=Drive_OCR("").google_spreadsheet_get("13Aw2HghuOauGAjnxgD5YvBYo7Ysda-TprTJ_BLHuIPA","A:N")
print(query)
db=Drive_OCR("").google_spreadsheet_get(query["id"][0],"Sheet1!A:N")
cell2=xlsxwriter.utility.xl_col_to_name(len(db)+3)
db2=Drive_OCR("").google_spreadsheet_get(query["id"][0],"Sheet2!A:"+cell2)
ids=[]
sub=[]

for x in db2:
	ids.append(x[1])
	sub.append(x[3])	
i=0
for x in ids:
	if str(query["user"][0]) ==str(x):
		break
	i+=1
st.write(sub)
N = len(db)*30
if i>len(sub)-1:
	sub.append(2)
if int(sub[i])==0:
	#st.set_page_config()
	ph = st.empty()
	
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
	#st.button("Reset", type="primary")
	if st.button('Submit'):
		db2[i][3]=1
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
		
	
	
	
	ids=[]
	for x in db2:
		ids.append(x[1])
	
	
	
		
	
	
	if query["user"][0] not in ids:
		data=[db2[i][0],query["user"][0],N,0]
		for x in btn:
			data.append(x)
		db2.append(data)
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
		st.write(db2)
	else:
		st.write(i)
		db2[i]=[db2[i][0],query["user"][0],int(os.environ[query["id"][0]+query["user"][0]]),0]
		for x in btn:
			db2[i].append(x)
		
		
		st.write(db2)
		print(str(db2))
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
		
		
		
		
	if int(os.environ[query["id"][0]+query["user"][0]])>0:
		for secs in range(int(os.environ[query["id"][0]+query["user"][0]]),-1,-1):
			mm, ss = secs//60, secs%60
			ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
			time.sleep(1)
			if secs>0:
				os.environ[query["id"][0]+query["user"][0]]=str(secs-2)
			if secs<1:
				ph.write("Times Up!!")
				time.sleep(5)
				db2[i][3]=1
				Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
	else:
		ph.write(btn)
elif int(sub[i])==1:
	st.write("attempt sucessful")
elif int(sub[i])==2:
	path = st.text_input(':rainbow[𝙔𝙤𝙪𝙧 𝙉𝙖𝙢𝙚]')
	if path:
		db2.append([path,query["user"][0],N,0])
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)

    
