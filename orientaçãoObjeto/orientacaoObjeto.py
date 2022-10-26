from conta import Conta

conta = Conta(123, 'bob', 100, 159)
print(conta.titular)

def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero , "titular":titular, "saldo":saldo, "limite":limite}
    return conta

def deposita(conta,valor):
    conta["saldo"] += valor
    
def saque(conta,valor):
    conta["saldo"] -= valor
def extrato(conta):
    print("saldo é: {} ".format(conta["saldo"]))        