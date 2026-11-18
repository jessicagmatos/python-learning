debito = float(input("qual o valor a ser debitado"))
saldo = 200

if debito <= 0 :
    print(f"valor invalido") 
elif debito > saldo :
    print(f"saldo insuficiente")
else: 
    saldo = saldo - debito
    #saldo -= debito
    print(f"o novo saldo é {saldo}")
