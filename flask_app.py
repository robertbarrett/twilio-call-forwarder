from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

callers = {
    "+11234567890": "+11231231230", # if 11234567890 calls the twilio number, the script forwards the call to 11231231230
    "+12345678901": "+14564564560" # if 12345678901 calls the twilio number, the script forwards the call to 14564564560
}

@app.route("/", methods=['GET', 'POST'])
def forward():
    resp = twilio.twiml.Response()
    from_number = request.values.get('From', None)

    if from_number in callers:
        to_num = callers[from_number]
        resp = twilio.twiml.Response()
        resp.dial(to_num)
    else:
        resp.say("Number not recognised")
        for letter in from_number:
            resp.say(letter)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
