from flask import Flask, request, redirect, render_template
import cgi
import os
import re


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('form.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

@app.route("/sign-up", methods=['POST'])
def sign_up():
    username = request.form['username']
    password = request.form['password']
    passconf = request.form['passconf']
    emailadd = request.form['emailadd']





    return render_template('confirmation.html',username=username)


app.run()