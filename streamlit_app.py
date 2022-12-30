from pyrogram import Client, filters
import re, requests ,os
app = Client("my_account",
bot_token="1431722823:AAHk_VOD0WgepQ1us7eucQm3UQRYacHzmQM",
api_id="13682659",
api_hash="b984d240c5258407ea911f042c9d75f6")


@app.on_message(filters.private & filters.regex("http"))
async def hello(client, message):
    t=re.split("\n", message.text)
    url=t[0]
    try:
    	t[1]=int(t[1])
    	try:
    	    t[2]=int(t[2])
    	except:
    	    t.append(412.5)
    except:
    	t.append(810)
    	t.append(412.5)
    mess="htmlPageHeight: "+str(t[1])+"\nhtmlPageWidth: "+str(t[2])
    await app.send_message(chat_id=message.chat.id, text=mess)
    site='https://avepdf.com/en/file/load-from-http'
    null=None
    true=True
    
    data={"uri":[url],"processedContextId":null,"toolId":"355FE458-BC5C-43B7-B94C-9372637C84CD","PdfParameters":{"htmlPageHeight":t[1],"htmlPageWidth":t[2],"htmlPageMarginTop":0,"htmlPageMarginBottom":0,"htmlPageMarginLeft":0,"htmlPageMarginRight":0,"htmlEmulationMedia":3,"htmlPreferOnePage":true}}
    #print(requests.post(site,json=data).json())
    data ={"processedContextId":requests.post(site,json=data).json()["processedContextId"]}
    site='https://avepdf.com/en/tools/convert-to-pdf-action'
    file=requests.post(site,json=data)
    #print(file.url)
    #from urllib.parse import urlencode
    #print(site+"?"+urlencode(data))
    site="https://avepdf.com/en/file/downloadClient/"+file.json()["processedContextId"]+"?filename=html-to-pdf.pdf"
    print(site)
    data=requests.get(site)
    with open(os.getcwd()+"/@polls_quiz.pdf", 'wb') as s:
        s.write(data.content)
    path = os.getcwd()+"/@polls_quiz.pdf"
    await app.send_document(message.chat.id, path)


app.run()