# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = "AC7c4bd51fdfeacbf553a52f682ab6c6b5"
auth_token = "44654a8cf5b93e283e50162055a4a236"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+12316851234", from_="+15303413085",
                                     body="Hello there!")