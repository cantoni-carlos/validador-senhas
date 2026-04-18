print("===SISTEMA DE CRIAÇÃO DE SENHA===")

senha_valida = False

while not senha_valida:

    senha = input("Digite a senha: ")

    tem_numero = False
    tem_maiuscula = False
    tem_minuscula = False
    tem_simbolo = False

    for letra in senha:
        if letra.isdigit():
            tem_numero = True

        if letra.isupper():
            tem_maiuscula = True

        if letra.islower():
            tem_minuscula = True

        if not letra.isalnum():
            tem_simbolo = True

    if len(senha) >= 8 and tem_numero and tem_maiuscula and tem_minuscula and tem_simbolo:
        print("Senha cadastrada com sucesso!")
        senha_valida = True
    else:
        print("Senha inválida:")

        if len(senha) < 8:
            print("- A senha deve ter pelo menos 8 caracteres")

        if not tem_numero:
            print("- A senha deve ter pelo menos um número")

        if not tem_maiuscula:
            print("- A senha deve ter pelo menos uma letra maiúscula")

        if not tem_minuscula:
            print("- A senha deve ter pelo menos uma letra minúscula")

        if not tem_simbolo:
            print("A senha deve ter pelo menos um caractere especial")