import streamlit as st
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

N = len(db)*30
if i>len(sub)-1:
	sub.append(2)
if int(sub[i])==0:
	#st.set_page_config()
	ph = st.empty()
	
	if query["id"][0]+query["user"][0] not in os.environ:
		os.environ[query["id"][0]+query["user"][0]]=str(N)
	
	btn2=[]	
	for x in range(len(db)):
		z=[]
		for y in db[x][1:-3]:
			if y!="":
				z.append(y)
		try:
			btn2.append(st.selectbox(db[x][0],z,index=int(db2[i][x+4])-1))
		except:
			btn2.append(st.selectbox(db[x][0],z))
		
	btn=[]
	for x in range(len(btn2)):
		j=0
		for y in db[x][1:-3]:
			if y==btn2[x]:
				break
			j+=1
		btn.append(j+1)
	st.write(btn)
	st.write("Thanks for Attempting Quiz")
	#st.button("Reset", type="primary")
	if st.button(':rainbow[Submit Test]'):
		db2[i][3]=1
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
		st.experimental_rerun()
		
	
	
	
	ids=[]
	for x in db2:
		ids.append(x[1])
	
	
	
		
	
	
	if query["user"][0] not in ids:
		data=[db2[i][0],query["user"][0],N,0]
		for x in btn:
			data.append(x)
		db2.append(data)
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
		#st.write(db2)
	else:
		#st.write(i)
		db2[i]=[db2[i][0],query["user"][0],int(os.environ[query["id"][0]+query["user"][0]]),0]
		for x in btn:
			db2[i].append(x)
		
		
		#st.write(db2)
		#print(str(db2))
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
				db2[i][2]=secs
				db2[i][3]=1
				Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
				st.experimental_rerun()
	else:
		ph.write(btn)

elif int(sub[i])==2:
	path = st.tt_input(':rainbow[𝙔𝙤𝙪𝙧 𝙉𝙖𝙢𝙚]')
	if path:
		
		db2.append([path,query["user"][0],N,0])
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
		os.environ[query["id"][0]+query["user"][0]]=str(N)
		st.experimental_rerun()
elif int(sub[i])==1:
	st.write("Test submission sucessful 🥳🥳🥳")
	if st.button(':rainbow[View your Answer key]'):
		db2[i][3]=3
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
		st.experimental_rerun()
elif int(sub[i])==3:
	for x in range(len(db)):
		st.write(":red["+db[x][0]+"]")
		tt=""
		for y in range(len(db[x][1:-3])):
			
			if db[x][y+1]=="":
				pass
			elif int(db2[i][x+4])==y:
				if int(db2[i][x+4])==int(db[x][-1]):
					tt+="```      ```:green["+db[x][y+1]+"]  \n"
				else:
					tt+="```      ```:red["+db[x][y+1]+"]  \n"
			elif int(y)==int(db[x][-1]):
				tt+="```      ```:red["+db[x][y+1]+"]  \n"
			else:
				tt+="```   ```"+db[x][y+1]+"  \n"
		st.write(tt)
		
		st.write("   :rainbow["+db[x][11]+"]")
	if st.button(':rainbow[Rank List]'):
		db2[i][3]=4
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
		st.experimental_rerun()
elif int(sub[i])==4:
	if st.button(':rainbow[View your Answer key]'):
		db2[i][3]=3
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
		st.experimental_rerun()	
	marks={}
	for x in range(len(db2)):
		mark=0
		for y in range(len(db2[x][-len(db):])):
			if str(db2[x][-len(db):][y]) =="":
				pass
			elif int(db2[x][-len(db):][y]) == int(db[y][-1]):
				mark+=4
			elif int(db2[x][-len(db):][y])==1:
				pass
			else:
				mark-=1
		marks[db2[x][1]]=mark
	st.write(marks)
	