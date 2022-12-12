import bcrypt

postData = _POST
username = postData["username"]
password = postData["password"]

hased = bcrypt.hashpw(password, bcrypt.gensalt())

if bcrypt.checkpw(password, hashed):
print ("OK")

else:
print ("didn't match")
