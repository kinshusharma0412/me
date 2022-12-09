from flask import Flask, render_template, url_for, request,Response
from pymongo import MongoClient
import json,os,re
#import dns
#from markupsafe import escape

print(os.getcwd())

import dns.resolver

dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)

dns.resolver.default_resolver.nameservers=['8.8.8.8'] # this is a google public dns server,  use whatever dns server you like here

# as a test, dns.resolver.query('www.google.com') should return an answer, not an exception

cm=MongoClient("mongodb+srv://soojhboojh01bot:Kinbin%40247@cluster0.uo8sfvz.mongodb.net/?retryWrites=true&w=majority")

#col=cm["Quiz"]["QuizData"]
#col.update_one({"testing":{"questions": [],"result":{}}})
#data=col.find_one(myquery1)["data"]
#		    		data.append({qname:qdata})
#		    		newvalues1 = { "$set": { "data":data} }
#		    		col.update_one(myquery1,newvalues1)
app = Flask(__name__)

@app.route("/<testname>/test",methods = ['POST', 'GET'])
def index(testname):
    print(testname)
    data=(request.form.to_dict())
    if len(data)>0:
        print(data)
    #print(data)
    return  render_template("index.html",np={"aname":"Stop_Test","test":testname})
    #print("########"+xyy)

@app.route('/login/<testname>',methods = ['POST', 'GET'])
def login(testname):
   
   use = request.args["fname"]
   
   pas = request.args["passw"]
   
   col=cm["Quiz"]["QuizData"]
   print(col.find_one({testname:{"$type":"object"}}))
   questions=col.find_one({testname:{"$type":"object"}})[testname]["questions"]
   print(questions)
   for x in questions:
       x["question"]=(re.sub("\n","<br>",(x["question"])))
   print(questions)
   questions="let questions ="+ str(questions)+";"
   f = open("./static/questions.js", "w")
   f.write(questions)
   f.close()
   
   
   return render_template("index.html",np=({"aname":"Start_Test","pass":pas,"name":use,"questions":questions}))
   #print("*******"+xyy)  

@app.route('/user_data1/<testname>',methods = ['POST', 'GET'])
def login3(testname):
   
   data=(request.form.to_dict())
   if len(data)>0:
      print(data)
      col=cm["Quiz"]["QuizData"]
      result=col.find_one({testname:{"$type":"object"}})[testname]["result"]
      result[data["name"]]=data
      
      full=(col.find_one({testname:{"$type":"object"}}))
      
      full2=full
      full2[testname]["result"][data["name"]+data["pass"]]=result[data["name"]+data["pass"]]
      if data["name"]+data["pass"] in list(full[testname]["result"].keys()):
          print(full)
      else:
          col.update_one(full,full2)
         
          
           #data=col.find_one(myquery1)["data"]
#		    		data.append({qname:qdata})
#		    		newvalues1 = { "$set": { "data":data} }
#		    		col.update_one(myquery1,newvalues1) 
   return  render_template("tee.html",data=data)



if __name__ == '__main__':
    app.run(host="0.0.0.0")
    #site="https://dev.to/curiouspaul1/building-a-quizgenerator-with-flask-and-fauna-257p"