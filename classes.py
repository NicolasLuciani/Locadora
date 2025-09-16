class Item:
    def __init__(self, id: int, titulo: str):
        self.__id = id
        self.__titulo = titulo
        self.__disponivel = True

    def alugar(self):
        if self.__disponivel:
            self.__disponivel = False
            return True
        return False

    def devolver(self):
        if not self.__disponivel:
            self.__disponivel = True
            return True
        return False

    def getId(self):
        return self.__id

    def getTitulo(self):
        return self.__titulo

    def isDisponivel(self):
        return self.__disponivel

    def setTitulo(self, titulo):
        self.__titulo = titulo


class Filme(Item):
    def __init__(self, id, titulo, genero, duracao):
        super().__init__(id, titulo)
        self.__genero = genero
        self.__duracao = duracao
    
    def getId(self):
        return self.__id
    
    def getTitulo(self):
        return self.__titulo

    def getGenero(self):
        return self.__genero

    def getDuracao(self):
        return self.__duracao

    def setGenero(self, genero):
        self.__genero = genero


class Jogo(Item):
    def __init__(self, id, titulo, plataforma, faixaEtaria):
        super().__init__(id, titulo)
        self.__plataforma = plataforma
        self.__faixaEtaria = faixaEtaria

    def getPlataforma(self):
        return self.__plataforma

    def getFaixaEtaria(self):
        return self.__faixaEtaria


class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__itensLocados = []

    def getNome(self):
        return self.__nome

    def getCpf(self):
        return self.__cpf

    def getItensLocados(self):
        return self.__itensLocados

    def locar(self, item: Item):
        if item.alugar():
            self.__itensLocados.append(item)
            return True
        return False

    def devolver(self, item: Item):
        if item in self.__itensLocados and item.devolver():
            self.__itensLocados.remove(item)
            return True
        return False


class Locadora:
    def __init__(self):
        self.__clientes = []
        self.__itens = []

    def cadastrarCliente(self, cliente: Cliente):
        self.__clientes.append(cliente)

    def cadastrarItem(self, item: Item):
        self.__itens.append(item)

    def listarClientes(self):
        return self.__clientes

    def listarItens(self):
        return self.__itens