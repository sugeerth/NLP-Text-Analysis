from flask import Flask
from flask import request
from twilio import twiml

from textblob import TextBlob

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def sms():
    response = twiml.Response()

    body = request.form['body']
    blob = TextBlob(body)

    response.message("Hey this is Fake Cortana lol, you sent me {} words".format(len(blob.words)))

    # with response.message("This is where you live Creepy hahah") as m: 
    #     m.media("http://photonet.hotpads.com/search/listingPhoto/EquityResidential/3089/0001_2146702751_medium.jpg")
    return str(response)


# @app.route("/", methods=['GET', 'POST'])
# def hello_monkey():
#     """Respond to incoming calls with a simple text message."""
 
#     resp = twilio.twiml.Response()
#     with resp.message("Hello, Mobile Monkey") as m:
#         m.media("https://demo.twilio.com/owl.png")
#     return str(resp)
 

# @app.route("/", methods=['GET','POST'])
# def hello_monkey():
#     """Respond to incoming calls with a simple text message."""
 
#     resp = twiml.Response()
#     resp.message("Hello, Mobile Monkey")
#     return str(resp)

if __name__ == '__main__':
    app.debug = True
    app.run()