# inherit CheckPWD class
import CheckPWD

postData = _POST
username = postData["username"]
password = postData["password"]

#tested credentials going to use in absence of a DB, 
TestUserName = "test"
TestPassword = "Abc123456"

#validate the password using class file
c = CheckPWD(password)
c.validation()

if(username == TestUserName and c == TestPassword ):
  print("OK")
else:
  print("Invalid")