# Implement a Simple Conference Call with Twilio and Flask 

Full tutorial can be found here: 

This code configures a simple conference call using Twilio Twiml
and Flask.

## Getting Started

This includes some of the basics for running the application however
you will need to make use of the Twilio console. You can follow the
article linked above to get up and running.

### Installing

```
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

### Running locally

Run the flask development server
```
(venv) $ flask run
```

Run ngrok
```
(venv) $ ngrok http 5000
```

## Built With

* [Flask](https://flask.palletsprojects.com/)
* [Twilio Python](https://github.com/twilio/twilio-python)
* [pyngrok](https://pyngrok.readthedocs.io/en/latest/index.html)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
