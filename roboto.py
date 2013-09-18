from twilio.rest import TwilioRestClient
from settings import SID, TOKEN, TO_NUMBER

account_sid = SID
auth_token = TOKEN
client = TwilioRestClient(account_sid, auth_token)
# Make the call
call = client.calls.create(to=TO_NUMBER, # Any phone number
from_= '+15005550006', # twilio provided test number
url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient") 

print call.sid