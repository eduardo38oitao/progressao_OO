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

# Criando os objetos
avatar = Filmes("avatar o caminho da água", 2022, 192)
avatar.curtir()  # Agora funciona corretamente

serie1 = Series("heartbreak high", 2022, 3)
serie1.curtir()  # Agora funciona corretamente

filmes_series = [avatar, serie1]

for programas in filmes_series:
    print(programas)