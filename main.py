from flask import Flask, request, redirect, render_template
import cgi
import os
import re


app = Flask(__name__)
app.config['DEBUG'] = True

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
    encoded_error = request.args.get("error")
    return render_template('form.html',emadd = emadd, user = user, error=encoded_error and cgi.escape(encoded_error, quote=True))

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

    if (not username) or (not password) or (not passconf):
        error = "Please fill in this portion."
        return redirect("/?error=" + error)

    if (' ' in username) or (len(username)<3):
        error = "Username be at least 3 characters long and contain only alphanumeric characters and punctuation."
        return redirect("/?error=" + error)

    if password != passconf:
        error = "Your passwords do not match."
        return redirect("/?error=" + error)

    if (len(emailadd)<3) or (len(emailadd)>20) or invalid_email(emailadd):
        error = "Please enter a valid email address."
        return redirect("/?error=" + error)

    return render_template('confirmation.html',username=username)


app.run()