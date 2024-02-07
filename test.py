from twilio.rest import Client

account_sid = 'AC2b350db86302846f6b12a52d4b98ec4e'
auth_token = 'b8c445efc141bc851e78811c71975b9b'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+254797245933'
)

print(message.sid)