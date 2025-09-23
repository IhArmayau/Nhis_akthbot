from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def home():
    return "AI WhatsApp bot yana aiki!"

@app.route("/sms", methods=["POST"])
def sms_reply():
    msg = request.form.get("Body")
    response = MessagingResponse()

    try:
        system_prompt = {
            "role": "system",
            "content": (
                "Kai kwararren mataimaki ne na lafiya da ke amsawa da harshen Hausa. "
                "Ka taimaka da shawarwari game da lafiya, amma ka guji bada magani kai tsaye. "
                "Idan tambaya ta fi karfinka, ka bada shawara a ga likita."
            )
        }

        reply = openai.ChatCompletion.create(model="gpt-3.5-turbo",
            messages=[system_prompt, {"role": "user", "content": msg}],
            max_tokens=300,
            temperature=0.7
        )

        bot_response = reply.choices[0].message.content.strip()
        response.message(bot_response)

    except Exception as e:
        print(f"Kuskure: {e}")
        response.message("An samu matsala wajen amsawa. Ka sake gwadawa daga baya.")

    return str(response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
