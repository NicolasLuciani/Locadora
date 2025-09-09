class Iten:
    def __init__(self, id: int, titulo: str):
        self.__id = id
        self.__titulo = titulo
        self.__disponibilidade = True
    
#------------------------------ métodos ------------------------------------------------
    def alugar(self):
        if self.__disponibilidade:
            self.__disponibilidade = False
    
    def devolver(self):
        if not self.__disponibilidade:
            self.__disponibilidade = True
    
    def getId(self):
        return self.__id
    
    def getTitulo(self):
        return self.__titulo

    def setTitulo(self, titulo):
        self.__titulo = titulo

#------------------------------ class filme ------------------------------------------------
class Filme(Iten):
    def genero(self):
        return self.__genero


    def duracao(self):
        return self.__duracao

    def __init__(self, id, titulo, genero, duracao):
        self.__id = id
        self.__titulo = titulo
        self.__genero = genero
        self.__duracao = duracao

        return None

    def getId(self):
        return self.__id
    
    def getTitulo (self):
        return self.__titulo
    
    def getGenero(self):
        return self.__genero
    
    def getDuracao(self):
        return self.__duracao
    
    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setGenero(self, genero):
        self.__genero = genero

#------------------------------ class jogo -------------------------------------------------
class Jogo(Iten):
    def __init__(self, plataforma, faixaEtaria):
        self.__plataforma = plataforma
        self.__faixaEtaria = faixaEtaria

    def plataforma(self):
        return self.__plataforma
    
    def faixaEtaria(self):
        return self.__faixaEtaria
#------------------------------ class cliente ------------------------------------------------
class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__itensLocados = []

        return None

    def getNome(self):
        return self.__nome
    
    def getCpf(self):
        return self.__cpf
    
    def getItensLocados(self):
        return self.__itenslocados

#------------------------------ métodos ------------------------------------------------
    def locar(self, disponibilidade):
        self.__disponibilidade == disponibilidade

        if self.__disponibilidade:
            self.__disponibilidade = False
        
    def devolver(self, disponibilidade):
        self.__disponibilidade == disponibilidade

        if not self.__disponibilidade:
            self.__disponibilidade = True
#------------------------------ class locadora ------------------------------------------------

class Locadora:
    def __init__(self):
        self.__cliente = []
        self.__itens = []
    
    def cadastrarCliente(self, cliente: Cliente):
        self.__cliente.append(cliente)

    def cadastrarItens(self, itens: Iten):
        self.__itens.append(itens)

    def listarClientes(self):
        return self.__cliente

    def listarItens(self):
        return self.__itens
