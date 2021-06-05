from flask import Flask, Response, request
from twilio.twiml.voice_response import Dial, Gather, VoiceResponse


app = Flask(__name__)


@app.route("/conference", methods=["POST"])
def conference():
    print(f"{request.form=}")
    response = VoiceResponse()
    pin_code = request.form.get("Digits")
    if pin_code and pin_code == "12345":
        dial = Dial()
        dial.conference(
            "Twilio Test Conference",
            status_callback="/events",
            status_callback_event="start end join leave mute hold",
        )
        response.append(dial)
    else:
        gather = Gather(action="/conference")
        gather.say("Please enter your conference pin,\nfollowed by the pound sign")
        response.append(gather)
    return Response(str(response), mimetype="text/xml")


@app.route("/events", methods=["POST"])
def events():
    for key, value in request.form.items():
        print(f"{key=} - {value=}")
    return "", 200
