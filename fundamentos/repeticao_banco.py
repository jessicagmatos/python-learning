saldo = 200
while True: 
    opcao = int(input("Digite 1 para débito \nDigite 2 para crédito \nDigite 3 para saldo \nDigite 0 para sair \n"))
    if opcao == 0:
        break
    elif opcao == 1:        
        debito = float(input("Digite o valor para débito: \n"))
        if debito <= 0 :
            print(f"Valor inválido")
        elif debito > saldo :
            print(f"Saldo insuficiente")
        else:
            saldo -= debito
            print(f"Débito realizado com sucesso! O saldo atual é de R$ {saldo:.2f} \n")
    elif opcao == 2:
        credito = float(input("Digite o valor para crédito: \n"))
        if credito <= 0:
            print(f"Valor inválido")
        else:
            saldo += credito
            print(f"Crédito realizado com sucesso! O saldo atual é de R$ {saldo:.2f} \n")
    elif opcao == 3:
        print(f"O saldo atual é de R$ {saldo:.2f} \n")


