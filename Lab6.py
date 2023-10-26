#Jaehyun Woo


def encode_pass(encode_num):
    encode = ""
    for num in encode_num:
        add_digit = (int(num) + 3) % 10
        encode += str(add_digit)

    return encode

def main():

    program_continue = True
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

        if menu_option == "1":
            password_encoded = encode_pass(password)

        if menu_option == "2":
            print(f"The encoded password is {password_encoded}, and the original password is {password}")

        else:
            menu_option == "3"
            break

if __name__ == '__main__':
    main()
