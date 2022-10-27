class Cliente:
    def __init__(self, nome):
        self.__nome = nome
        
    @property
    def nome(self):
        nome = self.__nome.title()
        print('{}'.format(nome))
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    
