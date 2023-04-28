class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass


def is_good_password(string):
    if len(string) < 9:
        raise LengthError
    if any(map(str.isalpha, string)) or string.islower() or string.isupper():
        raise LetterError
    if not any(map(str.isdigit, string)):
        raise DigitError
    return True

try:
    print(is_good_password('Short712'))
except Exception as err:
    print(type(err))



from sys import stdin


class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass


def is_good_password(string):
    if len(string) < 9:
        raise LengthError("LengthError")
    if not any(map(str.isalpha, string)) or string.islower() or string.isupper():
        raise LetterError("LetterError")
    if not any(map(str.isdigit, string)):
        raise DigitError("DigitError")
    return True


for password in stdin:
    try:
        if is_good_password(password.strip()):
            print("Success!")
            break
    except PasswordError as err:
        print(err)
        continue
