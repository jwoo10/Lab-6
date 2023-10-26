#Jaehyun Woo
def decode_pass(passcode_encoded):
    decode = ""

    for i in range(len(passcode_encoded)):
        add_digit = (10 + int(passcode_encoded[i]) - 3) % 10
        decode += str(add_digit)

    return decode

def encode_pass(encode_num):
    encode = ""
    # shift digit by 3
    for num in encode_num:
        add_digit = (int(num) + 3) % 10
        encode += str(add_digit)

    return encode

def main():

    program_continue = True
    password_encoded = ""
    # prints menu option
    while program_continue:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")

        menu_option = input("Please enter an option: ")
        password = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!")
        print("")

        # 1. Encode
        if menu_option == "1":
            password_encoded = encode_pass(password)

        # 2. Decode
        if menu_option == "2":
            password = decode_pass(password_encoded)
            print(f"The encoded password is {password_encoded}, and the original password is {password}")

        # 3. Quit
        else:
            menu_option == "3"
            break

if __name__ == '__main__':
    main()
