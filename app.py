from flask import Flask, Response, request
from twilio.twiml.voice_response import VoiceResponse, Dial


app = Flask(__name__)


@app.route("/conference", methods=["GET", "POST"])
def conference():
    print(f"{request.form=}")
    response = VoiceResponse()
    dial = Dial()
    dial.conference(
        "Twilio Test Conference",
        status_callback="/events",
        status_callback_event="start end join leave mute hold",
    )
    response.append(dial)
    return Response(str(response), mimetype="text/xml")


@app.route("/events", methods=["POST"])
def events():
    for key, value in request.form.items():
        print(f"{key=} - {value=}")
    return "", 202
