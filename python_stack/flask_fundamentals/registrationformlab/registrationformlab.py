from flask import Flask, render_template, request, redirect, flash
import re

app = Flask(__name__)       
app.secret_key = "ThisIsSecret!"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX  = re.compile(r'^[^0-9]+$')

@app.route('/')
def showForm():
    return render_template('index.html')      

@app.route('/process_form', methods=["POST"])
def processForm():

    bFlashMessage = False

    # All fields are required and must not be blank
    email = request.form['emailaddress']
    if len(email) < 1:
        flash("Email Address cannot be blank!")
        bFlashMessage = True

    f_name = request.form['first_name']
    if len(f_name) < 1:
        flash("First Name cannot be blank!")
        bFlashMessage = True

    l_name = request.form['last_name']
    if len(l_name) < 1:
        flash("Last Name cannot be blank!")
        bFlashMessage = True

    pwd = request.form['password']
    if len(pwd) < 1:
        flash("Password cannot be blank!")
        bFlashMessage = True

    confpwd = request.form['confirm_password']
    if len(confpwd) < 1:
        flash("Confirm Password cannot be blank!")
        bFlashMessage = True

    # First and Last Name cannot contain any numbers
    if NAME_REGEX.match(f_name):
        flash("First Name cannot contain numbers.")
        bFlashMessage = True

    if NAME_REGEX.match(l_name):
        flash("Last Name cannot contain numbers.")
        bFlashMessage = True

    # Password should be more than 8 characters
    if len(pwd) <= 8:
        flash("Password must be more than 8 characters.")
        bFlashMessage = True

    # Email should be a valid email
    if not EMAIL_REGEX.match(email):
        flash("Invalid Email Address!")
        bFlashMessage = True

    # Password and Password Confirmation should match
    if pwd != confpwd:
        flash("Password fields do not match!")
        bFlashMessage = True
    
    if bFlashMessage:
        return redirect('/')

    return render_template("display_info.html", full_name=full_name, loc=loc, fav_lang=fav_lang, remarks=remarks)    

if __name__=="__main__":
    app.run(debug=True)                   # Run the app in debug mode.