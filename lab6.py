# Kysa Mesa
# Christopher Kostas

def user_encode(user_data):
    # encode data
    result = ''
    for i in user_data:
        result += str(int(i)+3)
    return result

def user_decode(data):
    decoded_data = ''
    # decode data
    for i in data:
        decoded_data += str(int(i) - 3)
    return decoded_data


if __name__=="__main__":
    running=True
    data= []
    # print menu
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print(" ")
    # prompt user to enter an option
    print("Please enter an option:")
    choice = int(input())
    while running:
        if choice == 1:
            # getting password
            print("Please enter your password to encode:")
            user_data = input()
            encode = user_encode(user_data)
            print("Your password has been encoded and stored!")
            print(" ")
            # reprint the menu
            print("Menu")
            print("-------------")
            print("1. Encode")
            print("2. Decode")
            print("3. Quit")
            print(" ")
            print("Please enter an option:")
            choice = int(input())
        elif choice ==2:
            # decoding password
            print(f"The encoded password is", encode, ", and the original password is", user_data)
            decode=user_decode(data)
            # reprint the menu
            print(" ")
            print("Menu")
            print("-------------")
            print("1. Encode")
            print("2. Decode")
            print("3. Quit")
            print(" ")
            print("Please enter an option:")
            choice = int(input())
        elif choice == 3:
            # break the loop
            False


