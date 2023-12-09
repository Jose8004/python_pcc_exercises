def generate_squares(num):
    squares_dict = {}
    for number in range(1, num+1):
        squares_dict[number] = number ** 2
    print(squares_dict)
    return squares_dict

generate_squares(5)