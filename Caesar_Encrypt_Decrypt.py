print('-='*25)
print("\t\033[35mWelcome to Caesar Cipher Decryptor\033[m")
print('-='*25)
print('''Choose an option
\033[34m[1] - Encrypt
[2] - Decrypt\033[m''')
option = int(input("Choose one: "))
if option == 1:
    #under creation
    text = input("Write the text to encrypt: ")
    key = int(input("Put the key to encrypt: "))
    for char in text:
        uni_transform = ord(char) + key
        encrypt = chr(uni_transform)
        print(encrypt, end='')
    print('\nBye!!!!')
elif option == 2:
    #under creation
    x=0 #i will remove later
else:
    print('Wrong option!!!')