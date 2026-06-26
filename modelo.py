#Filmes e séries tem as seguintes características;

#Filme: Nome, Ano, Duração, curir
#Séries: Nome, Ano, Temporadas, curtir

class Filmes:
    def __init__(self,nome,ano,duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__curtir =  0

    @property
    def valor_curtir(self):
        return self.__curtir
    
    @property
    def valor_nome(self):
        return self.__nome

    def curtida(self):
        self.curtir += 1 



class Series:
    def __init__(self,nome,ano,temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.curtir =  0

    @property
    def valor_curtir(self):
        return self.__curtir
    
    @property
    def valor_nome(self):
        return self.__nome

    
    def curtida(self):
        self.curtir += 1 




heartbreak_high = Series("Heartbreak High", 2022, 3)
heartbreak_high.curtida()

print(f"Nome: {heartbreak_high.nome} - Ano: {heartbreak_high.ano} - Temporada: {heartbreak_high.temporadas} - {heartbreak_high.curtir}")


avatar = Filmes("Avatar", 2009, 177)
avatar.curtida()
print(f"Nome: {avatar.nome} - Ano: {avatar.ano} - Duracao: {avatar.duracao} - {avatar.curtir}")