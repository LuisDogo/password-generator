import string
import secrets


def rand():
    print("\n\nPlease select which of the following characters\nyou want to include in your password")
    print("\nSelect between [y/n] to include a set of characters")
    alphabet = ""
    if(input("\nnumbers?\n>")=="y"):
        alphabet += string.digits
    if(input("\nlower case?\n>")=="y"):
        alphabet += string.ascii_lowercase
    if(input("\nuppercase?\n>")=="y"):
        alphabet += string.ascii_uppercase
    if(input("\nspecial characters?\n>")=="y"):
        alphabet += string.punctuation
    return ''.join(secrets.choice(alphabet) for i in range(length))


print("\n\n¡Welcome to the password generator!\n")
length = int(input("\nChoose the length for your password\n>"))
print("\n\nNow is time to choose how the password will be made:")
mode = input("\n[random]\n>")
chosen_mode = False
while chosen_mode==False:
    if(mode == "random"):
        password = rand()
        chosen_mode=True
    else:
        print("please select a valid mode option")
        mode = input("\n[random/word based]\n>")

print("\nyour password is:  " + password)
print("\n\nThanks 4 using this password generator\ncreated by LuisDogo")