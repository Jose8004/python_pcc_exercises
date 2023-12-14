from pathlib import Path

def validate_config(string):
    #lines = Path(file_name).read_text().splitlines()
    words = string.split()
    print(f"This is the words list: {words}")
    key_checker = 0
    for word in words:
        print(f"This is a word: {word}")
        
        if word == 'id:':
            key_checker += 1
        elif word == 'name:':
            key_checker += 1
        elif word == 'value:':
            key_checker += 1

        print(f"This is the key count: {key_checker}")

    if key_checker == 3:
        return True
    else:
        return False
        
    
        
validate_config("id: 1\nname: Test\nvalue: 123\n")

