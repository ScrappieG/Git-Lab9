# Contributors - Jack Stone, Duong Nguyen
from encode import encode, decode

def main():
    encoded_password, decoded_password = '', ''
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        option = int(input("Please enter an option: "))
        if option == 1:
            given_password = str(input("Please enter your password to encode: "))
            encoded_password = encode(given_password)

            if encoded_password == False:
                print("Invalid password!\n")

            else:
                print('Your password has been encoded and stored!\n')


        elif option == 2:
            # Decode password
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}\n.")
            print('')
        else:
            return

if __name__ == '__main__':
    main()