class CheckPWD(object):
    # class constructor
    def __init__(self, password =''):
      self.password = password

    # Private method to check lowercase
    def _lower(self):
        lower = any(c.islower() for c in self.password)
        return lower

    # Private method to check uppercase
    def _upper(self):
        upper = any(c.islower() for c in self.password)
        return upper

    # Private method to check number
    def _digit(self):
        digit = any(c.isdigit() for c in self.password)
        return digit

    # Public method for password validation
    def validate(self):
        lower = self._lower()
        upper = self._upper()
        digit = self._digit()

        # check password is containing minium 8 charactors
        length = len(self,password)
        r = lower and upper and digit and length >= 8

        if r:
            print("OK")
            return True
        elif not lower:
            print("Your password should have a lower case letter")
            return False
        elif not upper:
            print("Your password should have a upper case letter")
            return False
        elif not digit:
            print("Your password should have a number")
            return False
        else:
            pass


