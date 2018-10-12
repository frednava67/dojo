from flask import Flask
app = Flask(__name__)
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL

# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('productsdb')
# now, we may invoke the query_db method
print("all the users", mysql.query_db("SELECT * FROM customers;"))
if __name__ =="__main__":
    app.run(debug=True)