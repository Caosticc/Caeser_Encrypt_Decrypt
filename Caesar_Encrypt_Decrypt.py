print('-='*25)
print("\t\033[3;35mWelcome to Caesar Cipher Decryptor\033[m")
print('-='*25)
def encrypt(text,key):
    for char in text: #get the characters from the text
        uni_transform = ord(char) + key #transform characters into unicode table codes and sum with key
        encrypt = chr(uni_transform) # transforms new unicode table values ​​into character
        print(f"\033[30m{encrypt}\033[m", end='')
    print('\nBye!!!!') 
def decrypt(text,key):
    for char in text: #get the characters from the text
        transform_uni = ord(char) - key #transform characters into unicode table codes and substracts with the key
        decrypt = chr(transform_uni)# transforms the unicode table values into the decrypted message
        print(decrypt, end='')
    print("\nBye!!!!")

print('''\033[1mChoose an option\033[m
\033[34m[1] - Encrypt
[2] - Decrypt\033[m''')
option = int(input("Choose one: "))
if option == 1:
    text = input("Write the text to encrypt: ")
    key = int(input("Put the key to encrypt: "))
    encrypt(text,key)
elif option == 2:
    text = input("White the text to decrypt: ")
    key = int(input("Put the key to decrypt: "))
    decrypt(text,key)
else:
    print('Wrong option!!!')