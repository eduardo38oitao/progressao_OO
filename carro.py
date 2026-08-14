# Classe mãe / Superclasse
class Veiculos:
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
    
    # Ação (método) para dar like/curtir o carro
    def curtir(self):
        self._curtidas += 1

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self._curtidas} Curtida(s)"


# Subclasse para carros Esportivos
class Esportivos(Veiculos):
    def __init__(self, nome, ano, velocidade_maxima):
        # Chama o construtor da classe mãe
        super().__init__(nome, ano)
        self.velocidade_maxima = velocidade_maxima

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.velocidade_maxima} km/h - {self._curtidas} Curtida(s)"


# Subclasse para carros SUV
class SUVs(Veiculos):
    def __init__(self, nome, ano, lugares):
        # Chama o construtor da classe mãe
        super().__init__(nome, ano)
        self.lugares = lugares

    def __str__(self):
        return f"{self.nome} - {self.ano} - {self.lugares} Lugares - {self._curtidas} Curtida(s)"


# Classe contêiner (semelhante à Playlist)
class Garagem:
    def __init__(self, nome_garagem, elementos):
        self.nome_garagem = nome_garagem
        self._elementos = elementos

    # Métodos mágicos (dunder methods) para permitir o uso de len(), 'in' e loop 'for'
    def __getitem__(self, item):
        return self._elementos[item]

    def __len__(self):
        return len(self._elementos)

    @property
    def listagem(self):
        return self._elementos
    
    @property
    def tamanho(self):
        return len(self._elementos)


# Criando os objetos dos carros esportivos
ferrari = Esportivos("ferrari f8 tributo", 2022, 340)
porsche = Esportivos("porsche 911 gt3", 2023, 318)

# Adicionando curtidas
ferrari.curtir()  
porsche.curtir()

# Criando os objetos dos SUVs
sw4 = SUVs("toyota sw4", 2023, 7)
pajero = SUVs("mitsubishi pajero sport", 2022, 7)

# Adicionando curtidas
sw4.curtir() 
pajero.curtir()

# Criando a lista de carros e a Garagem
lista_carros = [ferrari, sw4, porsche, pajero]
garagem_dos_sonhos = Garagem("Garagem dos Sonhos", lista_carros)

# Testes de execução
print(f"Tamanho da garagem: {len(garagem_dos_sonhos)}")
print(f"Está na garagem? {ferrari in garagem_dos_sonhos}\n")

# Iterando sobre os itens da Garagem
for carro in garagem_dos_sonhos:
    print(carro)