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


class Playlist(list):
    def __init__(self,nomePL, elementos):
        self.nomePL = nomePL
        super().__init__(elementos)
#nomePL é o nome da playlist

    

# Criando os objetos do filme
avatar = Filmes("avatar o caminho da água", 2022, 192)
tmep6 = Filmes("Todo mundo em panico 6", 2023, 140)
#curtida
avatar.curtir()  # Agora funciona corretamente
tmep6.curtir()
#series
serie1 = Series("heartbreak high", 2022, 3)
serie2 = Series("mentalista", 2022, 7)
#curtida 
serie1.curtir() 
serie2.curtir()
 # Agora funciona corretamente

filmes_series = [avatar, serie1, tmep6, serie2]
plFim_de_semana = Playlist("Fim de semana",filmes_series)

print(f"Tamanho da list: {len(plFim_de_semana)}")
print(f"Está na lista?{avatar in plFim_de_semana}")

for programas in plFim_de_semana:
    print(programas)