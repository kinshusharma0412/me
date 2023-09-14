import streamlit as st
from quickstart import Drive_OCR
db=Drive_OCR("").google_spreadsheet_get("13Aw2HghuOauGAjnxgD5YvBYo7Ysda-TprTJ_BLHuIPA","A:N")
print(db)
for x in db:
	
