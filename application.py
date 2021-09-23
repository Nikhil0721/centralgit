from flask import Flask
## WSGI Application This WSGI is Standard which actually used to communicate webserver and web applicaiton to communciate
application = Flask(__name__)

@application.route("/")
def welcome():
    return "Welcome Msdhoni Captaincool MAhiii"


if __name__=='__main__':
    app.run()
