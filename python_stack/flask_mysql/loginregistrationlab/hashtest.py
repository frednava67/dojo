from flask import Flask
from flask_bcrypt import Bcrypt        
app = Flask(__name__)        
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                         # which is made by invoking the function Bcrypt with our app as an argument

badpassword1 = "password"
badpassword2 = "abc123"

hash1 = bcrypt.generate_password_hash(badpassword1)
hash2 = bcrypt.generate_password_hash(badpassword2)

fakehash="b'$2b$12$pguzHoD9npUUCVekKYKzt.x7VMHGnOnbSYNsWW4SS66Y3x1ZWy2gi'"

print(hash1)
print(hash2)

print(bcrypt.check_password_hash(hash1, badpassword1))
print(bcrypt.check_password_hash(hash2, badpassword2))

print(bcrypt.check_password_hash(hash2, badpassword1))
print(bcrypt.check_password_hash(hash1, badpassword2))