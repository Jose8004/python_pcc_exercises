import string

def validate_password(password):
    
    uppercase = False
    lowercase = False
    digit = False
    special_character = False
    length = False

    flag = True
    while flag:
        if len(password) >= 8:
            length = True
        for character in password:
            if character in string.punctuation:
                special_character = True
            if character.isdigit():
                digit = True
            if character.isupper():
                uppercase = True
            if character.islower():
                lowercase = True
            print("One iteration")
        flag = False

        print(f"upper is: {uppercase}, lowercase is: {lowercase},")
        print(f"digit is: {digit}, special character is: {special_character}, ")
        print(f"length is: {length}")

    if uppercase and lowercase and digit and special_character and length:
        return True
    else:
        return False


print(validate_password('A1b2C3d4!'))
            
