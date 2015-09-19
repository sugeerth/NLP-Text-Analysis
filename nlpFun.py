from flask import Flask, request, redirect

from twilio import twiml

from textblob import TextBlob

app = Flask(__name__)


callers = {
		"+15307509848": "Aakshi",
		"+15303413085": "Sugeerth" }





# @app.route("/", methods=['GET','POST'])
# def sms():
#     response = twiml.Response()

#     body = request.form['body']

#     blob = TextBlob(body)

#     # response.message("Hey this is Fake Cortana lol, you sent me words")
#     # app.logger.info("Received: '{}'\nSent: '{}'".format(body,response.verbs[0].verbs[0].body))


#     with response.message("This is where you live Creepy hahah"+str(len("asdas"))) as m: 
#         m.media("http://photonet.hotpads.com/search/listingPhoto/EquityResidential/3089/0001_2146702751_medium.jpg")

#     return str(response)


@app.route("/", methods=['GET','POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    resp = twiml.Response()

    fromNumber = request.values.get('From',None)
    if fromNumber in callers:
		message = callers[fromNumber] + "OyeKaisa Hain bhe"
	else: 
		message = "Monkey!!!"

    # body = request.form['']
    # print body

    # blob = TextBlob(body)

    with resp.message(message+"This is where you live Creepy hahah"+str(len("asdas"))) as m: 
        m.media("http://photonet.hotpads.com/search/listingPhoto/EquityResidential/3089/0001_2146702751_medium.jpg")

    app.logger.info("Received: \nSent: '{}'".format(
                    resp.verbs[0].verbs[0].body))

    return str(resp)
 

# @app.route("/", methods=['GET','POST'])
# def hello_monkey():
#     """Respond to incoming calls with a simple text message."""
 
#     resp = twiml.Response()
#     resp.message("Hello, Mobile Monkey")
#     return str(resp)

if __name__ == '__main__':
    app.debug = True
    app.run()