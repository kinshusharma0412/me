import streamlit as st
import streamlit as st
import pandas as pd
#st.set_page_config(layout="wide")
from quickstart import Drive_OCR
import time,os, string,xlsxwriter
query=st.experimental_get_query_params()

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
	
	ph = st.empty()#st.container()
	
	if query["id"][0]+query["user"][0] not in os.environ:
		os.environ[query["id"][0]+query["user"][0]]=str(N)
	
	btn2=[]	
	for x in range(len(db)):
		z=[]
		for y in db[x][1:-3]:
			if y!="":
				z.append(y)
		try:
			btn2.append(st.selectbox("Q"+str(x+1)+". "+db[x][0],z,index=int(db2[i][x+4])-1))
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
	#st.write(btn)
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
			with ph:
				styl = f"""
<h1 style="position: fixed;up: 0rem;right: 0rem;">{mm:02d}:{ss:02d}</h1>"""
				ph.markdown(styl, unsafe_allow_html=True)
				#ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
				
			#st.markdown(f'''<div class="floating">{mm:02d}:{ss:02d}</div>''', unsafe_allow_html=True)
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
	path = st.text_input(':rainbow[𝙔𝙤𝙪𝙧 𝙉𝙖𝙢𝙚]')
	if path:
		
		db2.append([path,query["user"][0],N,0])
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
		os.environ[query["id"][0]+query["user"][0]]=str(N)
		st.experimental_rerun()
elif int(sub[i])==1:
	st.write("Test submission sucessful 🥳🥳🥳")
	col1,col2 = st.columns([1,1])
	with col1:
		bt1=st.button(':rainbow[View your Answer key]')
	with col2:
		bt2=st.button(':rainbow[Rank List]')

	if bt1:
		db2[i][3]=3
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
		st.experimental_rerun()
	if bt2:
		db2[i][3]=4
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
		st.experimental_rerun()
elif int(sub[i])==3:
	if st.button(':rainbow[Rank List]'):
		db2[i][3]=4
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
		st.experimental_rerun()
	
	for x in range(len(db)):
		st.write(":red[Q"+str(x+1)+". "+db[x][0]+"]")
		tt=""
		for y in range(len(db[x][1:-3])):
			
			if y==0:
				pass
			elif db[x][y+1]=="":
				pass
			elif int(db2[i][x+4])==y+1:
				if int(db2[i][x+4])==int(db[x][-1]):
					tt+="```      ```:green["+db[x][y+1]+"]  \n"
				else:
					tt+="```      ```:red["+db[x][y+1]+"]  \n"
			elif int(y)+1==int(db[x][-1]):
				tt+="```      ```:green["+db[x][y+1]+"]  \n"
			else:
				tt+="```   ```"+db[x][y+1]+"  \n"
		st.write(tt)
		
		st.write("   :rainbow["+db[x][11]+"]")
	
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
			#st.write(mark)
		
		marks[db2[x][1]]={"Name":db2[x][0],"Marks":mark,"Time":int(db2[x][2])}
	
	new_result={}
	for key in sorted(marks, key=lambda x: (marks[x]['Time']), reverse=True):
		
		new_result[key] = marks[key]
	
	new_result2={}
	for key in sorted(new_result, key=lambda x: (new_result[x]['Marks']), reverse=True):
		
		new_result2[key] = new_result[key]
	
	
	tab=[]
	con=1
	indi=1
	for x in new_result2.keys():
		new_result2[x]["Sr."]=str(con)
		if str(x)==str(ids[i]):
			indi=con
		con+=1
	for x in new_result2.keys():
		mm, ss =(N- new_result2[x]["Time"])//60, (N-new_result2[x]["Time"])%60
		ti=f"{mm:02d}:{ss:02d}"
		tab.append([new_result2[x]["Sr."]+". ",new_result2[x]["Name"],ti,new_result2[x]["Marks"]])
	
	#st.write(new_result2)
	
	df = pd.DataFrame(tab,columns=["sr","Name","Time","Marks"])
	
	def highlight_rows(x):
		if x.sr==str(indi)+". ":
			return['background-color: rgba(0,255,0,.5)']*4
		else:
			return['background-color: rgba(0,255,0,0)']*4
			#return['background-color: black']*4


	df = df.style.hide(axis="index")
	df=df.apply(highlight_rows, axis = 1)
	st.markdown(df.to_html(), unsafe_allow_html=True)
	
	#st.table(df)
	
	
	