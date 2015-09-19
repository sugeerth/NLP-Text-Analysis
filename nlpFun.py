from flask import Flask

from twilio import twiml

from textblob import TextBlob 


app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    response = twiml.Response()
    body = request.form['Body']

    blob = TextBlob(body)

    response.message("Hey guys this message has {} words.".format(len(blob.words)))

    app.logger.info("Received: '{}'\nSent: '{}'".format(body,response.verbs[0].verbs[0].body))

    return str(response)


if __name__ == '__main__':
    app.debug = True
    app.run()