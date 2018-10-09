from flask import Flask, render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import datetime as dt
import re

app = Flask(__name__)
app.secret_key = "Pneumonoultramicroscopicsilicovolcanoconiosis"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX  = re.compile('[0-9]')

# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('registerdb')
# now, we may invoke the query_db method
print("all the emails", mysql.query_db("SELECT * FROM accounts;"))
mysql = connectToMySQL('registerdb')
res = mysql.query_db("SELECT * FROM accounts WHERE id=100;")
if res == ():
    print("blank")

def performSQLCall(query, data=None)
    mysql = connectToMySQL('registerdb')


@app.route('/')
def index():

    if 'newentry' in session:
        return redirect('/success')
    

    return render_template('index.html')

@app.route('/perform_check', methods=['POST'])
def performCheck():

    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name'] 
    session['email'] = request.form['email']  
    session['pwd'] = request.form['password']
    session['confpwd'] = request.form['confirm_password']

    #1. First Name - letters only, at least 2 characters and that it was submitted

    f_name = request.form['first_name']
    if len(f_name) < 2 or NAME_REGEX.search(f_name):
        flash(u"First Name can only contain letters and be at least 2 characters", 'fname')
        bFlashMessage = True

    #2. Last Name - letters only, at least 2 characters and that it was submitted

    l_name = request.form['last_name']
    if len(l_name) < 2 or NAME_REGEX.search(l_name):
        flash(u"Last Name can only contain letters and be at least 2 characters", 'lname')
        bFlashMessage = True

    #3. Email - valid Email format, does not already exist in the database, and that it was submitted

    email = request.form['email']
    if len(email) < 1:
        flash(u"Email Address cannot be blank!", 'emailaddress')
        bFlashMessage = True

    # Email should be a valid email
    if not EMAIL_REGEX.match(email):
        flash(u"Invalid Email Address!", 'emailaddress')
        bFlashMessage = True        

    #Email shouldn't be in database already
    mysql = connectToMySQL('registerdb')
    query = "SELECT accounts.emailaddress FROM accounts WHERE emailaddress=%(email)s;"
    data =  { 'email': email }
    query_result = performSQLCall(query, data)
    if query_result != ():
        flash(u"Email Address already registered!", 'emailaddress')
        bFlashMessage = True  

    pwd = request.form['password']
    confpwd = request.form['confirm_password']

    # Password should be more than 8 characters
    if len(pwd) < 8:
        flash(u"Password must be at least 8 characters in length.",'pwd')
        bFlashMessage = True

    # Password and Password Confirmation should match
    if pwd != confpwd:
        flash(u"Password fields do not match!", 'pwd')
        bFlashMessage = True

    if bFlashMessage:
        return redirect('/')
    else:
        # INSERT STATEMENT
        # session('newentry') = f_name

@app.route('/success')
def displaySummary():
    if session('loggedin') == True:
        return render_template('success.html')
    else:
        return redirect('/')

@app.route('/login')
def login():


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)