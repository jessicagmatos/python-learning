saldo = 200

while True: 
    opcao = int(input("digite 1 para débito \n digite 2 para crédito \n digite 3 para saber o saldo \n 0 para sair"))
    if opcao == 0:
        break
    elif opcao == 1:
        debito = float(input("digite o valor para debito"))
        if debito <= saldo :
            print ("saldo insuficiente")
        else: 
        saldo = saldo - debito
