from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
import datetime as dt
import re

app = Flask(__name__)
app.secret_key = "Pneumonoultramicroscopicsilicovolcanoconiosis"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('emailval')
# now, we may invoke the query_db method
print("all the emails", mysql.query_db("SELECT * FROM validatedemails;"))

@app.route('/')
def index():
    alertdiv = ""
    if 'newemail' in session:
        return redirect('/success')
    
    if 'alerted' not in session:
        alertdiv="hiddendiv"
    else:
        alertdiv=""

    return render_template('index.html', alertclass=alertdiv)

@app.route('/perform_check', methods=['POST'])
def performCheck():
    email = request.form['emailaddress']

    # Email should be a valid email
    if not EMAIL_REGEX.match(email):
        flash("Email is not valid!")
        session['alerted'] = True
    else: # valid email to INSERT
        session['newemail'] = email
        mysql = connectToMySQL("emailval")
        query = "INSERT INTO validatedemails (emailaddress, created_date) VALUES (%(email)s, NOW());"
        data =  {   'email': email }
        new_email_id = mysql.query_db(query, data)

    return redirect('/')

@app.route('/success')
def displaySummary():
    newemailaddress = session['newemail']
    session.clear()
    mysql = connectToMySQL("emailval")
    all_emails = mysql.query_db("SELECT * FROM validatedemails")

    return render_template('summary.html', newemail=newemailaddress , emailslist=all_emails)

if __name__ =="__main__":
    app.run(debug=True)