def validate_password_strength(password):

    case_checker = 0

    if len(password) >= 8:
        for i in range(len(password)):
            if password[i].isupper() and case_checker == 0:
                case_checker += 1
            if password[i].islower() and case_checker == 1:
                case_checker += 1
            if password[i].isdigit() and case_checker == 2:
                case_checker += 1
    if case_checker >= 3:
        print('Strong')
    else:
        print('Weak')

validate_password_strength('trongass1S')