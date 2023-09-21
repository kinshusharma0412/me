import streamlit as st
import streamlit as st
import pandas as pd
#st.set_page_config(layout="wide")
from quickstart import Drive_OCR
import time,os, string,xlsxwriter
import re as reaaa
import ast,random
query=st.experimental_get_query_params()
from  urllib.parse import unquote_plus
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
            #
            #
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
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
	
	ids=[]
	for x in db2:
		ids.append(x[1])
	
	
	btn2=[]
	
	
	def click_button(j):
		if query["user"][0]+query["id"][0] not in os.environ:
			temp3={}
		else:
			temp3=ast.literal_eval(os.environ[query["user"][0]+query["id"][0]])
		
		y=reaaa.split("\.",j)
		st.session_state["q"]=random.randint(3, 999)
		_="""st.session_state[j]=True
		for x in range(len(db[int(y[0])-1][1:-3])):
			if db[int(y[0])-1][1:-3][x]!="":
				if str(x+1)!=y[1]:
					st.session_state[y[0]+"."+str(x+1)]=False"""
		temp3[y[0]]=y[1]
		os.environ[query["user"][0]+query["id"][0]]=str(temp3)
		
	_="""if query["user"][0]+query["id"][0] in os.environ:
		#st.write(os.environ[query["user"][0]+query["id"][0]])"""
	for x in range(len(db)):
		temp=[]
		
		st.write("["+str(x+1)+"/"+str(len(db))+"] "+db[x][0])
		for y in range(len(db[x][1:-3])):
			
			if db[x][1:-3][y]!="" :
				temp2=""
				
				
				if query["user"][0]+query["id"][0] not in os.environ:
					temp2=st.button(db[x][1:-3][y],key=str(x+1)+"."+str(y+1),on_click=click_button,args=[str(x+1)+"."+str(y+1)])
					
				else:
					if str(x+1) not in ast.literal_eval(os.environ[query["user"][0]+query["id"][0]]).keys():
						temp2=st.button(db[x][1:-3][y],key=str(x+1)+"."+str(y+1),on_click=click_button,args=[str(x+1)+"."+str(y+1)])
						
					else:
						if str(ast.literal_eval(os.environ[query["user"][0]+query["id"][0]])[str(x+1)])==str(y+1):
							temp2=st.button("```      ```:green["+db[x][1:-3][y]+"]",key=str(x+1)+"."+str(y+1),on_click=click_button,args=[str(x+1)+"."+str(y+1)])
						else:
							temp2=st.button(db[x][1:-3][y],key=str(x+1)+"."+str(y+1),on_click=click_button,args=[str(x+1)+"."+str(y+1)])
				

					
		
					
					
			
				
				
					
					#st.warning(str(x+1)+"."+str(y+1)+str(e), icon="⚠️")
					#temp2=st.button(db[x][1:-3][y],key=str(x+1)+"."+str(y+1))
				temp.append(temp2)
		
		if query["user"][0]+query["id"][0]  in os.environ:
			if  str(x+1) in ast.literal_eval(os.environ[query["user"][0]+query["id"][0]]).keys():
				if  str(ast.literal_eval(os.environ[query["user"][0]+query["id"][0]])[str(x+1)])==str(0):
					temp2=st.button("```      ```:green[Skip (optional)]",key=str(x+1)+"."+str(y+1),on_click=click_button,args=[str(x+1)+"."+str(0)])
				else:
					temp2=st.button("Skip (optional)",key=str(x+1)+"."+str(y+1),on_click=click_button,args=[str(x+1)+"."+str(0)])
			else:
				temp2=st.button("Skip (optional)",key=str(x+1)+"."+str(y+1),on_click=click_button,args=[str(x+1)+"."+str(0)])
				
		else:
			temp2=st.button("Skip (optional)",key=str(x+1)+"."+str(y+1),on_click=click_button,args=[str(x+1)+"."+str(0)])
		temp.append(temp2)
		btn2.append(temp)
		
		
		
	
	
	submt=st.button(':rainbow[Submit Test]')
	st.write("Thanks for Attempting Quiz")
	#st.button("Reset", type="primary")
	if submt:
		db2[i][2]=os.environ[query["id"][0]+query["user"][0]]
		db2[i][3]=1
		
		for x in range(len(db)):
			
			
			try:
				db2[i].append(ast.literal_eval(os.environ[query["user"][0]+query["id"][0]])[str(1+x)])
			except Exception as e:
				db2[i].append("")
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
		
		st.experimental_rerun()
		
	
	
	
	
	
	
	
		
	
	
	
		
		
		
	if int(os.environ[query["id"][0]+query["user"][0]])>0:
		for secs in range(int(os.environ[query["id"][0]+query["user"][0]]),-1,-1):
			mm, ss = secs//60, secs%60
			with ph:
				styl = f"""
<h1 style="position: fixed;up: 0rem;right: 0rem;">{mm:02d}:{ss:02d}</h1>"""
				ph.markdown(styl, unsafe_allow_html=True)
				
			time.sleep(1)
			os.environ[query["id"][0]+query["user"][0]]=str(secs-1)
		
			if secs<1:
				ph.write("Times Up!!")
				
				db2[i][2]=str(secs)
				db2[i][3]=1
				for x in range(len(db)):
					try:
						db2[i].append(ast.literal_eval(os.environ[query["user"][0]+query["id"][0]])[str(1+x)])
					except Exception as e:
						db2[i].append("")
				Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
				st.experimental_rerun()
elif int(sub[i])==2:
	if "name" in query.keys():
		path=unquote_plus(query["name"][0])
		db2.append([path,query["user"][0],N,0])
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
		os.environ[query["id"][0]+query["user"][0]]=str(N)
		st.experimental_rerun()
	else:
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
		st.write(":blue[Q"+str(x+1)+". "+db[x][0]+"]")
		tt=""
		
		for y in range(len(db[x][1:-3])):
			if db[x][y+1]=="":
				pass
			elif str(db2[i][x+4])=="":
				if int(y)+1==int(db[x][-1]):
					tt+="```      ```:green["+db[x][y+1]+"]  \n"
				else:
					tt+="```   ```"+db[x][y+1]+"  \n"
			elif str(db2[i][x+4])==str(y+1):
				if str(db2[i][x+4])==str(db[x][-1]):
					tt+="```      ```:green["+db[x][y+1]+"]```      ```+4  \n"
				else:
					tt+="```      ```:red["+db[x][y+1]+"]```      ```-1  \n"
			elif int(y)+1==int(db[x][-1]):
				tt+="```      ```:green["+db[x][y+1]+"]  \n"
			else:
				tt+="```   ```"+db[x][y+1]+"  \n"
		if str(db2[i][x+4])==str(0) or str(db2[i][x+4])=="":
			tt+="```      ```:red[Skip]  \n"
		st.write(tt)
		
		st.write("   :rainbow["+db[x][11]+"]")
	
elif int(sub[i])==4:
	if st.button(':rainbow[View your Answer key]'):
		db2[i][3]=3
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
		st.experimental_rerun()	
	elif st.button(':rainbow[Review]'):
		db2[i][3]=5
		Drive_OCR("").google_spreadsheet_update(query["id"][0],"Sheet2!A:"+cell2, "USER_ENTERED",db2)
		st.experimental_rerun()	
	marks={}
	for x in range(len(db2)):
		mark=0
		#st.write(db2[x])
		for y in range(len(db2[x][-len(db):])):
			try:
				
				if str(db2[x][-len(db):][y]) =="":
					pass
				elif str(db2[x][-len(db):][y]) == str(db[y][-1]):
					mark+=4
				elif str(db2[x][-len(db):][y])=="0":
					pass
				else:
					mark-=1
			except Exception as e:
				st.write("line215"+str(e))
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
	
elif int(sub[i])==5:
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

	marsk={}
	mark=0
	useR=[]
	
	for y in range(len(db2)):
		mask1=[]
		mark=0
		for x in range(len(db[4:-1])):
			try:
				if str(db2[y][x+4])=="" or str(db2[y][x+4])=="0" :
					pass
				elif str(db2[y][x+4])==str(db[x][-1]):
					mark+=4
				else:
					mark-=1
			except:
				pass	
			if str(y)==str(i):
				
				useR.append(mark)
				
				
			
			mask1.append(mark)
			
		marsk[db2[y][1]]=mask1
	av=[]
	for y in range(len(db[4:-1])):
		yy=0
		for x in marsk.keys():
			yy+=marsk[x][y]
			
		
		av.append(yy/len(db2))
	data=[]
	
	for x in range(len(av)):
		
		data.append([av[x],useR[x]])
	st.write(str((av),(useR)))
	chart_data = pd.DataFrame(data,columns=["Average Graph",str(db2[i][0])])
	st.line_chart(chart_data,use_container_width=True)

	
	
		
	
	
	
	
	
	
	
	