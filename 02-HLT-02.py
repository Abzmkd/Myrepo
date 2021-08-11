
BRACKETS = ["[", "(", ")", "[", "]", "{", "}"]

def check_username(username):
    if len(username) < 6 or len(username) > 15:
        print("Username incorrect length")
        return False
    return True


def check_password(password, username):
    if len(password) < 8 or len(password) > 256:
        print("Password incorrect length")
        return False


    num_of_lowers = 0
    num_of_uppers = 0
    num_of_digits = 0
    num_of_spaces = 0
    num_of_brackets = 0

    for a_characer in password:
        if a_characer.islower():
            num_of_lowers += 1
        elif a_characer.isupper():
            num_of_uppers += 1
        elif a_characer.isdigit():
            num_of_digits += 1
        elif a_characer == " ":
            num_of_spaces += 1
        elif a_characer in BRACKETS:
            num_of_brackets += 1

    if (num_of_lowers == 0
        or num_of_uppers == 0
        or num_of_digits == 0
        or num_of_spaces == 0
        or num_of_brackets == 0):
        print("A lowercase, uppercase, digit, space or bracket missing")
        return False

    
    if username in password:
        print("Username found")
        return False

    return True


username = input("Enter username: ")
password1 = input("Enter password: ")
password2 = input("Re-enter password: ")

all_valid = True

username_is_valid = check_username(username)

if not username_is_valid:
    all_valid = False
    print("Username is invalid")

password_is_valid = check_password(password1, username)

if not password_is_valid or password1 != password2:
    all_valid = False
    print("Password is invalid")

if all_valid:
    print("Welcome.")