import random
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
        super().__init__(nome,ano)
        self.duracao = duracao
    
    
    def __str__(self):
        duracaoRound = round(self.duracao/60)
        return f'{self.nome} - {self.ano} -  {duracaoRound} horas - {self.likes} Likes'  
        
class Serie(Programa): 
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas
    
    def __str__(self):    
        return f'{self.nome} - {self.ano} -  {self.temporadas} temporadas - {self.likes} Likes'
    
class Playlist:
    def __init__(self,nome,programas):
        self.nome = nome
        self.programas = programas
    
    
    def tamanho(self):
        return len(self.programas)

                       
    
           
            
        
vingadores = Filme('vingadores', 2018 , 160)
barbaros = Serie('barbaros', 2022, 5)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor',2018, 2)


demolidor.dar_like()
vingadores.dar_like()
demolidor.dar_like()
demolidor.dar_like()
vingadores.dar_like()
vingadores.dar_like()
barbaros.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()

filmes_e_series = [vingadores,barbaros,demolidor,tmep]

plys_fim_de_semana = Playlist('fim de semana' , filmes_e_series)

for i in plys_fim_de_semana.programas:
    print(i)