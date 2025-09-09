********# 🎬 Sistema de Locadora

### Um sistema simples de locadora de filmes e jogos, desenvolvido em Python para praticar Programação Orientada a Objetos (POO).

---

## 🚀 Funcionalidades
- Cadastrar clientes (com nome e CPF)
- Cadastrar filmes (com título, gênero e duração)
- Cadastrar jogos (com título, plataforma e faixa etária)
- Listar clientes, filmes e jogos
- Locar e devolver itens

---

## 📂 Estrutura do Projeto

- **app.py**  
  Menu principal que chama as funções utilizando `match case`, deixando o código mais organizado.

- **classes.py**  
  Contém as classes principais do sistema:  
  - `Item` → classe base para filmes e jogos  
  - `Filme` → herda de Item e adiciona gênero e duração  
  - `Jogo` → herda de Item e adiciona plataforma e faixa etária  
  - `Cliente` → representa os clientes, com nome, CPF e itens locados  
  - `Locadora` → gerencia os clientes e os itens  

- **funcoes.py**  
  Funções auxiliares para o sistema:  
  - `cadastrar_clientes()`  
  - `cadastrar_filmes()`  
  - `cadastrar_jogos()`  
  - `cadastrar_filmes_ou_jogos()`  
  - `listar()`  
  - `listar_clientes()`  
  - `listar_filmes()`  
  - `listar_jogos()`  
---

# Código 'classes.py'

```python
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
```
# 📚 Explicação das Classes

## class Item
Classe base para todos os itens da locadora (filmes e jogos).

**Atributos**
- `__id` → código único do item
- `__titulo` → nome do item
- `__disponivel` → indica se o item está disponível (True/False)

**Métodos**
- `alugar()` → marca o item como não disponível
- `devolver()` → marca o item como disponível
- `getId()` → retorna o id do item
- `getTitulo()` → retorna o título do item
- `isDisponivel()` → retorna se o item está disponível
- `setTitulo(titulo)` → altera o título do item

---

## class Filme(Item)
Classe filha de Item, específica para filmes.

**Atributos**
- `__genero` → gênero do filme
- `__duracao` → duração do filme em minutos

**Métodos**
- `getGenero()` → retorna o gênero do filme
- `getDuracao()` → retorna a duração
- `setGenero(genero)` → altera o gênero
---

## class Jogo(Item)
Classe filha de Item, específica para jogos.

**Atributos**
- `__plataforma` → plataforma do jogo (ex: PC, PS5)
- `__faixaEtaria` → faixa etária recomendada

**Métodos**
- `getPlataforma()` → retorna a plataforma
- `getFaixaEtaria()` → retorna a faixa etária
---

## class Cliente
Representa um cliente da locadora.

**Atributos**
- `__nome` → nome do cliente
- `__cpf` → CPF do cliente
- `__itensLocados` → lista de itens alugados pelo cliente

**Métodos**
- `getNome()` → retorna o nome
- `getCpf()` → retorna o CPF
- `getItensLocados()` → retorna a lista de itens locados
- `locar(item)` → aluga um item e adiciona à lista de locados
- `devolver(item)` → devolve um item e remove da lista de locados
---

## class Locadora
Gerencia todos os clientes e itens da locadora.

**Atributos**
- `__clientes` → lista de todos os clientes cadastrados
- `__itens` → lista de todos os itens cadastrados

**Métodos**
- `cadastrarCliente(cliente)` → adiciona um cliente à lista
- `cadastrarItem(item)` → adiciona um item à lista
- `listarClientes()` → retorna todos os clientes
- `listarItens()` → retorna todos os itens
---

# Código funcoes.py
```python
****
```
