
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "WhatsApp bot is running!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    msg = request.form.get('Body').lower()
    response = MessagingResponse()

    if 'sallama' in msg:
        response.message("Taya zan taimaka maka?")
    elif 'nhis' in msg:
        response.message("NHIS a AKTH yana bada sabis ga ma’aikata da iyalansu.")
    else:
        response.message("Na fahimci tambayarka ba sosai ba. Zan turawa ma’aikaci.")

    return str(response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True, port=port, host="0.0.0.0")

