class Data:
    def __init__(self,dia,mes,ano) -> None:
        self.dia = dia
        self.mes = mes 
        self.ano = ano
    def formatarData(self,dia,mes,ano):
        print('{}/{}/{}'.format(self.dia,self.mes,self.ano))
        
