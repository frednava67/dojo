from flask import Flask, render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import datetime as dt
import re

app = Flask(__name__)
app.secret_key = "Pneumonoultramicroscopicsilicovolcanoconiosis"
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX  = re.compile('[0-9]')

SQL_MESSAGES_TO_ACCOUNT = "SELECT * FROM messages JOIN accounts ON accounts.id=messages.fromaccount_id WHERE toaccount_id = %(account_id)s ORDER BY messages.created_at DESC;"
SQL_MESSAGES_FROM_ACCOUNT = "SELECT * FROM messages JOIN accounts ON accounts.id=messages.toaccount_id WHERE fromaccount_id = %(account_id)s;"
SQL_INSERT_NEW_ACCOUNT = "INSERT INTO accounts (email, pwhashval, created_at, updated_at, first_name, last_name) VALUES (%(email)s, %(pwhash)s, NOW(), NOW(), %(first_name)s, %(last_name)s);"
SQL_ALL_USERS_EXCEPT_CURRENT_USER = "SELECT * FROM accounts WHERE id!=%(account_id)s;"

# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
ACTIVEDB = 'simplewalldb'
mysql = connectToMySQL(ACTIVEDB)
# now, we may invoke the query_db method
print("all the accounts", mysql.query_db("SELECT * FROM accounts;"))
mysql = connectToMySQL(ACTIVEDB)

def performSQLCall(query, data=None):
    mysql = connectToMySQL(ACTIVEDB)
    print(mysql)
    return mysql.query_db(query, data)

@app.route('/runonce')
def update():
    #UPDATE table_name
    #SET column1 = value1, column2 = value2, ...
    #WHERE condition;

    # badpassword1 = "abcd1234"
    # pwhash = bcrypt.generate_password_hash(badpassword1)
    # query = "UPDATE accounts SET pwhashval='%(hash)s', updated_at=NOW() WHERE first_name='Big'"
    # data =  {'hash': pwhash }
    # performSQLCall(query, data)
    # return redirect('/')

        pwd = "password"
        pwhash = bcrypt.generate_password_hash(pwd)
        query = "INSERT INTO accounts (email, pwhashval, created_at, updated_at, first_name, last_name) VALUES (%(email)s, %(pwhash)s, NOW(), NOW(), %(first_name)s, %(last_name)s);"
        print(query)
        data =  {   'email': "pig@farm.com",
                    'pwhash': pwhash,
                    'first_name': "Wilbur",
                    'last_name': "Hogg"
                }
        print(data)
        performSQLCall(query,data)    
        return redirect('/')


@app.route('/')
def index():
    print("index()")

    if 'loggedin' in session and session['loggedin'] == True:
        query = 'SELECT * FROM accounts where email=%(email)s'
        data =  {'email': session['email']}
        currentuser = performSQLCall(query,data)

        query = SQL_MESSAGES_TO_ACCOUNT
        data = {'account_id': currentuser[0]['id']}
        messagesTo = performSQLCall(query,data)

        query = SQL_ALL_USERS_EXCEPT_CURRENT_USER
        data = {'account_id': currentuser[0]['id']}
        allOtherAccounts = performSQLCall(query,data)

        query = SQL_MESSAGES_FROM_ACCOUNT
        data = {'account_id': currentuser[0]['id']}
        messagesSent = performSQLCall(query,data)
        totalMessagesSent = len(messagesSent)     

        return render_template('dashboard.html', first_name=currentuser[0]['first_name'], messageSentCount=totalMessagesSent, lenmessageList=str(len(messagesTo)), messagesToList=messagesTo, otherAccountsList=allOtherAccounts)
        
    if 'first_name' in session:
        f_name = session['first_name']
    else:
        f_name = ""

    if 'last_name' in session:
        l_name = session['last_name']
    else:
        l_name = ""

    if 'email' in session:
        eml = session['email']
    else:
        eml = ""        

    return render_template('index.html', first_name=f_name, last_name=l_name, email=eml)

@app.route('/perform_check', methods=['POST'])
def performCheck():
    print("performCheck()")

    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name'] 
    session['email'] = request.form['email']  
    session['pwd'] = request.form['password']
    session['confpwd'] = request.form['confirm_password']

    bFlashMessage = False

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
    query = "SELECT accounts.email FROM accounts WHERE email=%(email)s;"
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
        pwhash = bcrypt.generate_password_hash(pwd)
        query = SQL_INSERT_NEW_ACCOUNT
        print(query)
        data =  {   'email': email,
                    'pwhash': pwhash,
                    'first_name': f_name,
                    'last_name': l_name,
                }
        print(data)
        bSuccess = performSQLCall(query,data)
        if bSuccess:
            session['loggedin'] == True
            session['first_name'] = f_name
            session['last_name'] = l_name 
            session['email'] = email              
        else:
            flash(u"Something went wrong with the account creation attempt!", 'fname')
            bFlashMessage = True
        
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    print("login()")

    postedemail = request.form['email']
    postedpassword = request.form['password']
    
    query = "SELECT * FROM accounts WHERE email=%(email)s;"
    data =  {
                'email': postedemail,
            }
    result = performSQLCall(query,data)

    returnedhash = result[0]['pwhashval']
    hashcheck = bcrypt.check_password_hash(returnedhash, postedpassword)

    if result!=() and hashcheck:
        session['loggedin'] = True
        session['first_name'] = result[0]['first_name']
        session['last_name'] = result[0]['last_name'] 
        session['email'] = result[0]['email']
    else:
        flash(u"You were unable to login.",'login')       
    
    return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
    print("logout()")
    session.clear()
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)