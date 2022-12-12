import pyotp
	
Class MFA(object)

	self.totp = pyotp.TOTP("base32secret3232")
	print("Your OTP is ", totp.now())
	
	#enter your OTP
	r = input("enter your OTP here")
	if totp.verify(r) == True:
	    print("Successful Login")
	
	else:
	    print("UnSuccessful")