def encode(password):
    if len(password) != 8 or not password.isnumeric():
        return False
    encoded = ''
    for digit in password:
        encoded += str((int(digit) + 3) % 10)
    return encoded

def decode(password):
    #TODO
    return