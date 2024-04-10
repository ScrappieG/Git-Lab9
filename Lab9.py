
def main():
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        password = ''
        option = int(input("Please enter an option: "))
        if option == 1:
            password = str(input("Please enter your password to encode: "))
            password = encode(password)
            print('Your password has been encoded and stored!')
            # Encode
        elif option == 2:
            # Decode password
            print('')
        else:
            return


def encode(password):
    output = ''
    for digit in password:
        int(digit) + 3
        output += str(output)
    return output

if __name__ == '__main__':
    main()