# Classe mãe/principal
# Super Classe
class Programas:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._curtidas = 0

    @property
    def curtidas(self):
        return self._curtidas

    @property
    def nome(self):
        return self._nome
    
    # Removido o @property, pois curtir é uma ação (método)
    def curtir(self):
        self._curtidas += 1

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self._curtidas} Curtida"

class Filmes(Programas):
    def __init__(self, nome, ano, duracao):
        # Chama o construtor da classe mãe para criar o nome e as curtidas
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.duracao } Minutos - {self._curtidas} Curtidas"

class Series(Programas):
    def __init__(self, nome, ano, temporadas):
        # Chama o construtor da classe mãe para criar o nome e as curtidas
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.temporadas} Temporadas - {self._curtidas} Curtidas"


class Playlist():
    #nomePL é o nome da playlist
    def __init__(self,nomePL, elementos):
        self.nomePL = nomePL
        self._elementos = elementos
    
    @property
    def listagem(self):
        return self._elementos
    
    

    def __getitem__ (self,item):
        return  self._elementos[item]

    def __len__(self):
        return len(self._elementos)

# Criando os objetos do filme
avatar = Filmes("avatar o caminho da água", 2022, 192)
tmep6 = Filmes("Todo mundo em panico 6", 2023, 140)
#curtida
avatar.curtir()  
tmep6.curtir()
#series
serie1 = Series("heartbreak high", 2022, 3)
serie2 = Series("mentalista", 2022, 7)
#curtida 
serie1.curtir() 
serie2.curtir()


filmes_series = [avatar, serie1, tmep6, serie2]
plFim_de_semana = Playlist("Fim de semana",filmes_series)

#print(f"Tamanho da list: {len(plFim_de_semana)}")
print(f"Está na lista?{avatar in plFim_de_semana}")
print(f"Posição: {plFim_de_semana[2]}")

#for programas in plFim_de_semana:
#    print(programas)

#Python data model
#inicialização:__init__
#Representação:__str__,__repr__
#Container/Sequencia:__contains__,__iter__,__len__,__getitem__
#numericas:__add__,__sub__,__mul__,__mod__


#Python data model, exemplo
#inicialização:Novo()
#Representação:print(obj),str(obj),repr(obj)
#Container/Sequencia:len(obj),item in obj, foi in obj, obj[2,3]
#numericas:obj+outro_obj, obj*obj