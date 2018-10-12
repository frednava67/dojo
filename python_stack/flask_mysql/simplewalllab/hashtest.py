from flask import Flask
from flask_bcrypt import Bcrypt        
app = Flask(__name__)        
bcrypt = Bcrypt(app)    # we are creating an object called bcrypt, 
                        # which is made by invoking the function Bcrypt with our app as an argument

mylist = [{'id': 1, 'email': 'pig@farm.com', 'first_name': 'Wilbur', 'last_name': 'Hogg'}, {'id': 2, 'email': 'spider@farm.com', 'first_name': 'Charlotte', 'last_name': 'Webb'}, {'id': 3, 'email': 'rooster@farm.com', 'first_name': 'Foghorn', 'last_name': 'Leghorn'}]
print(mylist)
print(len(mylist))


badpassword1 = "password"
badpassword2 = "abc123"

hash1 = bcrypt.generate_password_hash(badpassword1)
#hash2 = bcrypt.generate_password_hash(badpassword2)
print(hash1)
#print(hash2)
hash1 = bcrypt.generate_password_hash(badpassword1)
#hash2 = bcrypt.generate_password_hash(badpassword2)
print(hash1)
#print(hash2)
hash1 = bcrypt.generate_password_hash(badpassword1)
#hash2 = bcrypt.generate_password_hash(badpassword2)
print(hash1)
#print(hash2)

print(bcrypt.check_password_hash(hash1, badpassword1))
#print(bcrypt.check_password_hash(hash2, badpassword2))

#print(bcrypt.check_password_hash(hash2, badpassword1))
#print(bcrypt.check_password_hash(hash1, badpassword2))