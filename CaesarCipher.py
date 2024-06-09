print('-=' * 25)
print("\t\033[3;35mBem-vindo ao Decifrador de Cifra de César\033[m")
print('-=' * 25)


def encrypt(texto, chave):
    resultado = ''
    for char in texto:
        if char.isalpha():
            deslocamento = chave % 26
            if char.islower():
                resultado += chr((ord(char) - ord('a') + deslocamento) % 26 + ord('a'))
            elif char.isupper():
                resultado += chr((ord(char) - ord('A') + deslocamento) % 26 + ord('A'))
        else:
            resultado += char
    return resultado


def decrypt(texto, chave):
    resultado = ''
    for char in texto:
        if char.isalpha():
            deslocamento = chave % 26
            if char.islower():
                resultado += chr((ord(char) - ord('a') - deslocamento) % 26 + ord('a'))
            elif char.isupper():
                resultado += chr((ord(char) - ord('A') - deslocamento) % 26 + ord('A'))
        else:
            resultado += char
    return resultado


print('''\033[1mEscolha uma opção\033[m
\033[34m[1] - Criptografar
[2] - Descriptografar\033[m''')
opcao = int(input("Escolha uma: "))
if opcao == 1:
    texto = input("Digite o texto para criptografar: ")
    chave = int(input("Digite a chave para criptografar: "))
    criptografado = encrypt(texto, chave)
    print(f"\033[30m{criptografado}\033[m")
    print('Tchau!!!!')
elif opcao == 2:
    texto = input("Digite o texto para descriptografar: ")
    chave = int(input("Digite a chave para descriptografar: "))
    descriptografado = decrypt(texto, chave)
    print(descriptografado)
    print('Tchau!!!!')
else:
    print('Opção errada!!!')
