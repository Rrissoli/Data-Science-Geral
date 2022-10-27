class Conta:
    
    def __init__(self, numero, titular, saldo, limite) -> None:
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print('Saldo {} do titular {}'.format(self.__saldo,self.__titular))
    
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__limite + self.__saldo
        return valor_a_sacar <= valor_disponivel
        
    def sacar(self,valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print('o valor passou do limite de {}'.format(self.__limite))
            
    def depositar(self,valor):
        self.__saldo += valor
        
    def transferencia(self,receptor, valor):
        if(self.__pode_sacar(valor)):
            self.sacar(valor)
            receptor.depositar(valor)
            print('saiu {} do {} e foi para {}'.format(valor, self.__titular,receptor.__titular))
        else:
            print('o valor de {} ultrapassa o limite de {}'.format(valor,self.__limite))
        
    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    def get_limite(self):
        return self.__limite
    
    def get_numero(self):
        return self.__numero
    
    
    @property
    def limite(self):
        limite = self.__limite
        print('{}'.format(limite))
    
    @limite.setter
    def limite(self,valor):
        self.__limite = valor
        
    @staticmethod
    def codigo_banco():
        return "001"
            