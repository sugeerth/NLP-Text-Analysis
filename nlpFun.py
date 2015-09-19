from flask import Flask

from twilio import twiml


app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    response = twiml.Response()
    response.message("Hey guys - thanks for coming to my talk.")
    return str(response)


if __name__ == '__main__':
    app.debug = True
    app.run()