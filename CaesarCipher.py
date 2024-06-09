print('-=' * 25)
print("\t\033[3;35mWelcome to Caesar Cipher Decryptor\033[m")
print('-=' * 25)


def encrypt(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    print(f"\033[30m{result}\033[m")
    print('Bye!!!!')


def decrypt(text, key):
    result = ''
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            result += char
    print(result)
    print('Bye!!!!')


print('''\033[1mChoose an option\033[m
\033[34m[1] - Encrypt
[2] - Decrypt\033[m''')
option = int(input("Choose one: "))
if option == 1:
    text = input("Write the text to encrypt: ")
    key = int(input("Put the key to encrypt: "))
    encrypt(text, key)
elif option == 2:
    text = input("Write the text to decrypt: ")
    key = int(input("Put the key to decrypt: "))
    decrypt(text, key)
else:
    print('Wrong option!!!')
