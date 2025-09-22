from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(_name_)

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
        response.message("NHIS a AKTH yana bada sabis ga ma’aikata da >")
    else:
        response.message("Na fahimci tambayarka ba sosai ba. Zan turaw>")

    return str(response)

if _name_ == "_main_":
    app.run(debug=True, port=8000)



