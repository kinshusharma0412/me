import os,time
from fpdf import FPDF
import streamlit as st
from PIL import Image
import glob,img2pdf
from PyPDF2 import PdfWriter, PdfReader,PdfMerger, PdfReader
from random import randint

import pdfkit
import pandas as pd
import site,glob
import os

import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-features=VizDisplayCompositor")
def delete_selenium_log():
    if os.path.exists('selenium.log'):
        os.remove('selenium.log')


def show_selenium_log():
    if os.path.exists('selenium.log'):
        with open('selenium.log') as f:
            content = f.read()
            st.code(content)


def run_selenium():
    name = str()
    with webdriver.Chrome(options=options, service_log_path='selenium.log') as driver:
        url = "https://www.unibet.fr/sport/football/europa-league/europa-league-matchs"
        driver.get(url)
        xpath = '//*[@class="ui-mainview-block eventpath-wrapper"]'
        # Wait for the element to be rendered:
        element = WebDriverWait(driver, 10).until(lambda x: x.find_elements(by=By.XPATH, value=xpath))
        name = element[0].get_property('attributes')[0]['name']
    return name
   
delete_selenium_log()
st.set_page_config(page_title="Selenium Test", page_icon='✅',
    initial_sidebar_state='collapsed')
st.title('🔨 Selenium Test for Streamlit Sharing')
st.markdown('''This app is only a very simple test for **Selenium** running on **Streamlit Sharing** runtime.<br>
    The suggestion for this demo app came from a post on the Streamlit Community Forum.<br>
    <https://discuss.streamlit.io/t/issue-with-selenium-on-a-streamlit-app/11563><br>
    This is just a very very simple example and more a proof of concept.
    A link is called and waited for the existence of a specific class and read it.
    If there is no error message, the action was successful.
    Afterwards the log file of chromium is read and displayed.
    ---
    ''', unsafe_allow_html=True)

st.balloons()
if st.button('Start Selenium run'):
    st.info('Selenium is running, please wait...')
    result = run_selenium()
    st.info(f'Result -> {result}')
    st.info('Successful finished. Selenium log file is shown below...')
    show_selenium_log()
site.addsitedir(r"...pathToPDFTron\PDFNetWrappersWin32\PDFNetC\Lib")
from PDFNetPython3 import PDFDoc, Optimizer, SDFDoc
os.system("python3 -m pip install apryse-sdk --extra-index-url=https://pypi.apryse.com")
try:
	from apryse_sdk import *
except Exception as e:
	st.write(e)
on = st.empty()
bttn=st.empty()
onn= st.empty()
onon= st.empty()
onn1= st.empty()
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
		line=st.empty()
		submit_button = st.empty()
		if uploaded_files:
			name="./"+uploaded_files.name
			with open(name, "wb") as file:
				file.write(uploaded_files.getvalue())
			inputpdf = PdfReader(open(name, "rb"))
			
			pagen = line.slider('Select page number', 0, len(inputpdf.pages), 0)
	if submit_button.form_submit_button(label="Submit your choice"):
		if pagen>0:
			for i in range((len(inputpdf.pages)//pagen)):
				output = PdfWriter()
				for x in range((pagen)):
					output.add_page(inputpdf.pages[x*i])
				with open(name[2:-4]+" %s.pdf" % (i+1), "wb") as outputStream:
					output.write(outputStream)
				file = open(name[2:-4]+" %s.pdf" % (i+1),"rb")
				st.download_button(label="Download PDF",data=file.read(),file_name=name[2:-4]+" %s.pdf" % (i+1),mime="application/octet-stream")
			output = PdfWriter()
			if (len(inputpdf.pages)//pagen)*pagen!=len(inputpdf.pages):
				for i in range((len(inputpdf.pages)//pagen)*pagen,len(inputpdf.pages)):
					output.add_page(inputpdf.pages[i])
				with open(name[2:-4]+" %s.pdf" % ((len(inputpdf.pages)//pagen)+1), "wb") as outputStream:
					output.write(outputStream)
				file = open(name[2:-4]+" %s.pdf" % ((len(inputpdf.pages)//pagen)+1),"rb")
				st.download_button(label="Download PDF",data=file.read(),file_name=name[2:-4]+" %s.pdf" %str(len(inputpdf.pages)//pagen+1),mime="application/octet-stream")

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

elif onn1.toggle('PDF compressor feature un-complite now'):
# Read pdf into a list of DataFrame
	st.write("This feature can Compress your PDF file")
	place_holder=st.empty()
	with place_holder.form(key="form2"):
		uploaded_files = st.file_uploader("Choose a .PDF file (multiple files are not accepted)", accept_multiple_files=False)
		line=st.empty()
		submit_button = st.empty()
		if uploaded_files:
			name="./"+uploaded_files.name
			with open(name, "wb") as file:
				file.write(uploaded_files.getvalue())
			
	if submit_button.form_submit_button(label="Submit your choice"):
		name="./"+uploaded_files.name
		PDFNet.Initialize("demo:1695835217274:7c183fec03000000008c0a8a3abd11c6896a9c7310aa9139d5d1481dd0")
		
		doc = PDFDoc(name)
		doc.InitSecurityHandler()
		Optimizer.Optimize(doc)
		doc.Save('compressed_'+name, SDFDoc.e_linearized)
		files.download('compressed_'+name)
		doc.Close()
		st.download_button(label="Download your compress PDF",data=file.read(),file_name='compressed '+name,mime="application/octet-stream")
		
    
		
		
			
