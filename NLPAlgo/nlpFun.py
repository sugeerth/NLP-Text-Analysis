from flask import Flask, request, redirect, session, jsonify, render_template
import requests
from twilio import twiml
from textblob import TextBlob
from NLPStuff import NLPStuff

import mechanize
from bs4 import BeautifulSoup
import re
import datetime
import argparse
import sys
import ConfigParser
import time

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

callers = {
        "+15303413085": "Sugeerth" 
        }

def recognizeNumbers(fromNumber):
    """Requires Authentications from True caller"""
    url ='https://api.opencnam.com/v2/phone/'+str(8882378289)
    r = requests.get(url).json
    print r
    return r

def salutationToCaller(message, fromNumber, myNumber, counter): 
    name =""   
    if fromNumber in callers:
            name = callers[fromNumber]
            message += "Hello "+str(name)+ " The path to enlightenment is often difficult to see.\nGreetings. I sense your mind is troubled. Tell me of your troubles.\nAsk the question you have come to ask.\nHello. Do you seek englightenment?\n\n"
    return message

def storeCookies(blob):
    counter = session.get('counter',0)
    counter += 1
    session['counter'] = counter
    return counter

@app.route("/", methods=['GET','POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    resp = twiml.Response()
    message=""
    name=""

    fromNumber = request.values.get('From',None)
    myNumber = request.values.get('To',None)
    
    body = request.values.get('Body')
    body = body.decode("ascii", errors="ignore")
    blob = TextBlob(body)


    NLPObject = NLPStuff(resp, blob, message)

    counter = storeCookies(blob)
    message+= salutationToCaller(message, fromNumber, myNumber, counter) 

    if "help" in blob.lower():
       message="This is an information HELP message please tell me what to do"

    return setMessage(message, name, myNumber, counter, body, blob, resp)

def setMessage(message, name, myNumber, counter, body, blob, resp):
    # message+= "".join([name, " has messaged ", myNumber," ",str(counter), " times."])
    # with resp.message(message+" \n") as m: 
        # m.media("")
    resp.message(message+" \n")
    app.logger.info("Received: {}\nSent: '{}'".format(body, resp.verbs[0].verbs[0].body))
    return str(resp)

if __name__ == '__main__':
    app.debug = True
    app.run()