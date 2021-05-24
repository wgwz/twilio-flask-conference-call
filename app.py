from logging import basicConfig
from flask import Flask, Response, request
from twilio.twiml.voice_response import VoiceResponse, Dial


basicConfig(level="INFO")
app = Flask(__name__)


@app.route("/conference", methods=["GET", "POST"])
def conference():
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
    for key, value in request.values.items():
        app.logger.info("%s - %s", key, value)
    return "", 202
