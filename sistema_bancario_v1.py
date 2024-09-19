# DESAFIO SISTEMA BANCÁRIO COM PYTHON

# Nesse desafio, terei que seguir algumas premissas básicas:
    # Menu de opções deve ter 3 opções: depósito, saque e extrato.
    # Deve conter apenas um usuário nessa primeira versão.
    
    # DEPÓSITOS:
        # Apenas valores inteiros.
        # Armazenados em uma variável para serem exibidos em extrato.
    # SAQUES:
        # Apenas 3 saques diários.
        # Limite de R$500.00 por saque.
        # Caso não tenha saldo, exibir mensagem de erro.
        # Armazenados em uma variável para serem exibidos em extrato.
    # EXTRATOS:
        # Lista todos os depósitos e saques realizados.
        #Valores tem que ser exibidos no formato "R$xxxx.xx"
    # Obs: nesse exemplo, essa conta bancária terá um saldo incial de R$1000.00.

limite_diário_saque = 3
limite_por_saque = 500
saldo = 1000

lista_saques = []
lista_depósitos = []

print("     ### Seja bem-vindo ao Sistema Bancário v1! ###      \n")

while True:
    print('''Selecione uma opção digitando o número correspondente:
        
        1 - DEPÓSITO
        2 - SAQUE
        3 - EXTRATO
        9 - SAIR
        ''')

    opção = input("Insira aqui a opção: ")

    if opção == "1":
        depósito = int(input("\nQuanto deseja depositar? "))
        if depósito <= 0:
            print("\nErro! Valor inválido\nValores de saque têm que ser números inteiros maiores que 0.\n")
        else:
            print(f"\nValor de R${depósito}.00 depositado com sucesso e já disponível em sua conta!")
            saldo += depósito
            lista_depósitos.append(depósito)
            print(f"\nSeu saldo atual é de R${saldo}.00\n")
    
    elif opção == "2":
        if limite_diário_saque <= 0:
            print("\nErro! Limite diário de saques excedido!\n")
        else:
            saque = int(input("\nQuanto deseja sacar? "))
            if saque > saldo:
                print("\nErro! Saldo insuficiente!\n\nFavor, consultar seu extrato.\n")
            else:
                print(f"\nValor de R${saque}.00 sacado com sucesso e já debitado de sua conta corrente.")
                saldo -= saque
                limite_diário_saque = limite_diário_saque - 1
                lista_saques.append(saque)
                print(f"\nSeu saldo atual é de R${saldo}.00\n")
    
    elif opção == "3":
        print(f"\nSaldo atual: R${saldo}.00")
        print(f"Depósitos realizados: {lista_depósitos}")
        print(f"Saques realizados: {lista_saques}\n")
    
    elif opção == "9":
        print("\nObrigado por utilizar nosso sistema!\n")
        break
    
    else:
        print("\nOpção inválida!\n")