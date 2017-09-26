from flask import Flask, request, redirect, render_template
import cgi
import os
import re


app = Flask(__name__)
app.config['DEBUG'] = True
emadd=''
user=''

def invalid_email(address):
    if ("@" not in address) or ("." not in address):
        return True

    elif " " in address:
        return True

    elif (address.find("@")!=address.rfind("@")) or (address.find(".")!=address.rfind(".")) or (address.find("@")>address.find(".")):
        return True

    else:
        return False



@app.route("/")
def index():
    usererror = request.args.get("usererror")
    passerror = request.args.get("passerror")
    conferror = request.args.get("conferror")
    emailerror = request.args.get("emailerror")
    return render_template('form.html',emadd = emadd, user = user, usererror=usererror and cgi.escape(usererror, quote=True), passerror=passerror and cgi.escape(passerror, quote=True), conferror=conferror and cgi.escape(conferror, quote=True), emailerror=emailerror and cgi.escape(emailerror, quote=True))

@app.route("/sign-up", methods=['POST'])
def sign_up():
    username = cgi.escape(request.form['username'])
    password = cgi.escape(request.form['password'])
    passconf = cgi.escape(request.form['passconf'])
    emailadd = cgi.escape(request.form['emailadd'])

    global user
    user = username

    global emadd
    emadd = emailadd

    usererror = ''
    passerror = ''
    conferror = ''
    emailerror = ''

    error = False
    if (' ' in username) or (len(username)<3) or (len(username)>20) or (not username):
        usererror = "Username be at least 3 characters long and contain only alphanumeric characters and punctuation."
        error = True

    if (' ' in password) or (len(password)<3) or (len(password)>20) or (not password):
        passerror = "This is not a valid password."
        error = True

    if password != passconf:
        conferror = "Your passwords do not match."
        error = True
    
    if emailadd:
        if (len(emailadd)<3) or (len(emailadd)>20) or invalid_email(emailadd):
            emailerror = "Please enter a valid email address."
            error = True
        
    if error:    
        return redirect("/?usererror=" + usererror + '&' + "passerror=" + passerror +'&' + "conferror=" + conferror +'&' + "emailerror=" + emailerror)

    return render_template('confirmation.html',username=username)


app.run()