from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = ''
auth_token = ''#inseert authroken
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body="I can't believe this works!",
                              from_='+12052458750',
                              to='+2348056679806'
                          )

print(message.sid)
