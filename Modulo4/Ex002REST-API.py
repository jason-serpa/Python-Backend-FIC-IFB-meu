from dotenv import load_dotenv
from twilio.rest import Client
import os
load_dotenv()

account_sid = os.environ["TW_ACCOUNT_SID"]
auth_token = os.environ["TW_AUTH_TOKEN"]
client = Client(account_sid, auth_token)
mensagem = client.messages.create(
    from_="+17372508034",
    to="+5561996511231",
    body="sms_delivery_updates"
)
print(mensagem.body)