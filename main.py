menu = """
Olá em que posso ajudar, escolha uma das opções abaixo:
Lembrando que o limite de saque é de R$ 500,00 e só pode ser efetuado 3 saques por dia.

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        vlr_deposito = int(input("Digite o valor que deseja depositar:"))
        saldo += vlr_deposito
        print(f"Seu saldo atual é de: R$ {saldo:.2f}")


    elif opcao == "s":
        vlr_saque = int(input("Digite o valor que deseja sacar: "))
        if vlr_saque <= limite and saldo:
            if numero_saques < limite_saques:
                saldo -= vlr_saque
                numero_saques += 1
                print(f"Saque de {vlr_saque} efetuado com sucesso. Seu saldo atual é de: R$ {saldo:.2f}")

            else:
                print("Limite de saques diários atingido")

        else:
            print("Valor informado é maior do que o saldo atual ou limite permitido")

    elif opcao =="e":
        print(f"Seu saldo atual é de:R$ {saldo:.2f}")

    elif opcao =="q":
        print("Programa encerrado, obrigado e tenha um ótimo dia!")
        break
