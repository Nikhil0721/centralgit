from flask import Flask
## WSGI Application This WSGI is Standard which actually used to communicate webserver and web applicaiton to communciate
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome Msdhoni Captaincool"


if __name__=='__main__':
    app.run()
