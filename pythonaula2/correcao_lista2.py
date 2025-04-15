#exercicio 4 
def classificarnumeros():
    positivos = 0
    negativos = 0
    zeros = 0

    for i in range (6):
        numero = float(input("Digite o número: "))
        if numero >0:
            positivos +=1
        elif numero<0:
            negativos +=1
        else:
            zeros += 1

    print(f"Positivos: {positivos}\n")
    print(f"Negativos: {negativos}\n")
    print(f"Zeros: {zeros}\n")

#exercicio 5 
def nome_com_a():
    for i in range(5):
        nome = input("Digite o nome")
        if nome.lower().startswith("a"):
            print(f"O nome {nome} começa com a letra A")

#exercicio 8
def senha_loop():
    while True:
        senha = input("Digite a senha: \n")
        if senha == "senac123":
            print("Acesso liberado!")
            break
        else:
            print("Senha incorreta. Tente novamente.\n")

#exercicio 10
def tabuada():
    while True:
        numero = int(input("Digite um numero para calcular a tabuada"))
        print(f"Segue a tabuada do número {numero}")
        for i in range(1,11):
            print(f"{numero} x {i} = {numero * i}")

        repetir = input("Deseja ver outra tabuada? (S/N)")
        if repetir.lower() != "s":
            print("Encerrando")
            break

        