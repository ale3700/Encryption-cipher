# Função de criptografia usando a Cifra de César
def cifra_cesar(texto, chave):
    resultado = ""
    
    # Itera por cada caractere no texto
    for char in texto:
        # Aplica deslocamento apenas a letras maiúsculas e minúsculas
        if char.isalpha():
            deslocamento = ord(char) + chave
            
            # Verifica se o caractere é maiúsculo ou minúsculo
            if char.isupper():
                resultado += chr((deslocamento - ord('A')) % 26 + ord('A'))
            else:
                resultado += chr((deslocamento - ord('a')) % 26 + ord('a'))
        else:
            # Adiciona caracteres que não são letras sem alteração
            resultado += char
    return resultado

# Solicita ao usuário a mensagem e a chave
mensagem = input("Digite a mensagem a ser criptografada: ")
chave = int(input("Digite a chave (número de posições para deslocar): "))

# Criptografa a mensagem
mensagem_cifrada = cifra_cesar(mensagem, chave)
print("Mensagem Cifrada:", mensagem_cifrada)


