class Programa():
    def __init__(self,nome,ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    @property
    def likes(self):
        return self._likes    
        
    def dar_like(self):
        self._likes += 1
        
    @property
    def nome(self):
        return self._nome  
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title() 





class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0
        
        
class Serie(Programa): 
    def __init__(self,nome,ano,temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0
    
           
            
        
vingadores = Filme('vingadores', 2018 , 160)
barbaros = Serie('barbaros', 2022, 5)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
barbaros.dar_like()
print(f'nome: {barbaros.nome} Ano: {barbaros.ano} temporadas: {barbaros.temporadas} likes: {barbaros.likes}')
print(f'nome: {vingadores.nome} Ano: {vingadores.ano} duracao: {vingadores.duracao} likes: {vingadores.likes}')