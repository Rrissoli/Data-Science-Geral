class Funcionario:
    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Globo(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class GE(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'
        
class Junior(GE):
    pass
class Pleno(Globo,GE):
    pass
class Senior(Globo,GE,Hipster):
    pass


jose = Junior()
luan = Pleno()
luan.busca_cursos_do_mes()
luan.busca_perguntas_sem_resposta()
jose.busca_perguntas_sem_resposta()
jean = Senior('jean')
print(jean)




# herança multipla, luan é da Globo e GE pois ele é pleno e plenos sao de duas subclasses maes filhas da classe funcionarios
# ordem de escolha quando o metodo é comum para duas superclassesde herança MRO do python:
# Pleno > Globo > Funcionario > GE > Funcionario