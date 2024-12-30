#Importing the Libraries
import numpy as np
from flask import Flask, render_template,request,make_response
import mysql.connector
from mysql.connector import Error
from random import randint
#from scilearn import compute
import json  #json request
import pandas as pd
import flask
import os
from predictor import processor


#Loading Flask and assigning the model variable
app = Flask(__name__)
app=flask.Flask(__name__,template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def index1():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dataloader')
def dataloader():
    return render_template('dataloader.html')




@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')






@app.route('/preprocess')
def emotion_detection():
    os.system('python F:/house-price-prediction-master/housesales.py')
    return render_template('dashboard.html')


""" REGISTER CODE  """

@app.route('/regdata', methods =  ['GET','POST'])
def regdata():
    connection = mysql.connector.connect(host='localhost',database='flaskhouseprice',user='root',password='')
    uname = request.args['uname']
    name = request.args['name']
    pswd = request.args['pswd']
    email = request.args['email']
    phone = request.args['phone']
    addr = request.args['addr']
    value = randint(123, 99999)
    uid="User"+str(value)
    print(addr)
        
    cursor = connection.cursor()
    sql_Query = "insert into userdata values('"+uid+"','"+uname+"','"+name+"','"+pswd+"','"+email+"','"+phone+"','"+addr+"')"
        
    cursor.execute(sql_Query)
    connection.commit() 
    connection.close()
    cursor.close()
    msg="Data saved successfully"
    #msg = json.dumps(msg)
    resp = make_response(json.dumps(msg))
    
    print(msg, flush=True)
    #return render_template('register.html',data=msg)
    return resp




"""LOGIN CODE """

@app.route('/logdata', methods =  ['GET','POST'])
def logdata():
    connection=mysql.connector.connect(host='localhost',database='flaskhouseprice',user='root',password='')
    lgemail=request.args['email']
    lgpssword=request.args['pswd']
    print(lgemail, flush=True)
    print(lgpssword, flush=True)
    cursor = connection.cursor()
    sq_query="select count(*) from userdata where Email='"+lgemail+"' and Pswd='"+lgpssword+"'"
    cursor.execute(sq_query)
    data = cursor.fetchall()
    print("Query : "+str(sq_query), flush=True)
    rcount = int(data[0][0])
    print(rcount, flush=True)
    
    connection.commit() 
    connection.close()
    cursor.close()
    
    if rcount>0:
        msg="Success"
        resp = make_response(json.dumps(msg))
        return resp
    else:
        msg="Failure"
        resp = make_response(json.dumps(msg))
        return resp

@app.route('/houseprice', methods =  ['GET','POST'])
def flaskhouseprice():
    location=request.args['loct']
    malls=request.args['malls']
    schools=request.args['schools']
    hospitals=request.args['hospitals']
    len=request.args['len']
    floors=request.args['floors']
    builtyear=request.args['builtyear']
    facility=request.args['facility']
    breadths=request.args['breadths']
    housetype=request.args['housetype']
    bedroom=request.args['bedroom']
    garea=request.args['garea']
    spool=request.args['spool']
    road=request.args['road']
    locality=location
    print(locality)
    tval=int(len)
    print("Total sqft is : "+str(tval))
    if housetype=="1":
        isconst="yes"
    else:
        isconst="no"
    print(isconst)
    numbed=bedroom
    from predictor import processor
    print(type(locality))
    print(tval)
    print(isconst)
    print(numbed)
    print(floors)
    print('-------------')
    print(malls)
    print(schools)
    print(hospitals)
    pval=processor.predict(locality,tval,isconst,numbed,floors,malls,schools,hospitals)
    print(pval)
    if int(builtyear)<1980:
        pval=pval-(pval%0.1)
    resp = make_response(json.dumps(pval))
    return resp
    
   


    
if __name__=="__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)
