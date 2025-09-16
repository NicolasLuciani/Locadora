# 🎬 Sistema de Locadora

### Um sistema simples de locadora de filmes e jogos.

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
from classes import *

locadora = Locadora()
# funcoes
#------------------------------------------------------------------------------------------#
# cadastrar_clientes
def cadastrar_clientes():
    try:
        print("=== CADASTRO DE CLIENTES ===")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        if len(cpf) != 11:
            print("O CPF possui apenas 11 dígitos")
        cliente = Cliente(nome, cpf)
        locadora.cadastrarCliente(cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")

    except Exception as e:
        print(f"Houve um erro {e} :(")
#------------------------------------------------------------------------------------------#
# cadastrar_filmes
def cadastar_filmes():
    try:
        print("=== CADASTRO DE FILMES ===")
        id = len(locadora.listarItens()) + 1
        titulo = input("Título: ")
        genero = input("Gênero: ")
        duracao = input("Duração do filme (ex: 2h 23m):")
        filme = Filme(id, titulo, genero, duracao)
        locadora.cadastrarItem(filme)
        print(f"Filme {titulo} cadastrado com sucesso!")

    except Exception as e:
        print(f"Houve um erro {e} :(")
#------------------------------------------------------------------------------------------#
# cadastar_jogos
def cadastrar_jogo():
    try:
        print("=== CADASTRAR DE JOGOS ===")
        id = len(locadora.listarItens()) + 1
        titulo = input("Título: ")
        plataforma = input("Plataforma: ")
        faixaEtaria = input("FaixaEtaria: ")
        jogo = Jogo(id, titulo, plataforma, faixaEtaria)
        locadora.cadastrarItem(jogo)
        print(f"Jogo {titulo} cadsatrado com sucesso!")

    except Exception as e:
        print(f"Houve um erro {e} :(")
#------------------------------------------------------------------------------------------#
# listar_clientes
def listar_clientes():
    try:
        print("=== LISTA DE CLIENTES ===")
        clientes = locadora.listarClientes()

        if not clientes:
            print("Nenhum cliente cadastrado")
        
        for cliente in clientes:
            print(f"Nome: {cliente.getNome()}| CPF: {cliente.getCpf()}")

    except Exception as e:
        print(f"Houve um erro {e} :(")
#------------------------------------------------------------------------------------------#
# listar_filmes
def listar_filmes():
    try:
        print("=== LISTA DE FILMES ===")
        itens = locadora.listarItens()
        filmes = False

        if not itens:
            print("Não há nenhum filme cadastrado!")
            return
        
        for item in itens:
            if item.isDisponivel():
                status = "Disponível"
            
            else:
                status = "Alugado"
            
            print(f"{item.getId()} - Filme: {item.getTitulo()}| Gênero: {item.getGenero()}| Duração: {item.getDuracao()}min| {status}")
            filmes = True

    except Exception as e:
        print(f"Houve um erro {e} :(")
#------------------------------------------------------------------------------------------#
# listar_jogos
def listar_jogos():
    try:
        print("=== LISTA DE JOGOS ===")
        itens = locadora.listarItens()
        jogos_existem = False

        if not itens:
            print("Não há nenhum jogo cadastrado!")
            return

        for item in itens:
            try:
                if item.isDisponivel():
                    status = "Disponível"
                else:
                    status = "Alugado"

                print(f"{item.getId()} - Jogo: {item.getTitulo()} | Plataforma: {item.getPlataforma()} | Faixa Etária: {item.getFaixaEtaria()}+ | {status}")
                jogos_existem = True
            except AttributeError:
                continue  

        if not jogos_existem:
            print("Não há nenhum jogo cadastrado!")

    except Exception as e:
        print(f"Houve um erro {e} :(")
#------------------------------------------------------------------------------------------#
# listar_itens(filmes ou jogos)
def listar_itens():
    escolha = 1
    while escolha != 0:
        try:
            print("=== LISTAGEM ===")
            print("")
            print("1 - Listar filmes")
            print("2 - Listar jogos")
            print("0 - sair")
            escolha = input("---> ")

            match escolha:
                case "1":
                    listar_filmes()
                case "2":
                    listar_jogos()
                case "0":
                    break
                case _:
                    print("Número inválido")
                    

        except Exception as e:
            print(f"Houve um erro {e} :(")
```
## 📝 Funções de Cadastro

### `cadastrar_cliente()`
- Solicita nome e CPF.
- Valida o CPF (11 dígitos).
- Cria objeto `Cliente` e adiciona à locadora.

### `cadastrar_filme()`
- Solicita título, gênero e duração.
- Gera ID automaticamente.
- Cria objeto `Filme` e adiciona à locadora.

### `cadastrar_jogo()`
- Solicita título, plataforma e faixa etária.
- Gera ID automaticamente.
- Cria objeto `Jogo` e adiciona à locadora.

### `cadastrar_filme_jogo()`
- Menu interativo para escolher cadastrar filme ou jogo.
- Usa `match/case` para tratar opções do usuário.

---

## 📝 Funções de Listagem

### `listar_clientes()`
- Lista todos os clientes cadastrados com nome e CPF.
- Exibe mensagem caso não haja clientes.

### `listar_filmes()`
- Filtra apenas os objetos `Filme`.
- Mostra ID, título, gênero, duração e status (Disponível/Alugado).

### `listar_jogos()`
- Filtra apenas os objetos `Jogo`.
- Mostra ID, título, plataforma, faixa etária e status.

### `listar()`
- Menu interativo para listar clientes, filmes ou jogos.
- Usa `match/case` e `while True` para permitir navegação contínua.
---
# App.py
```python
from classes import *
from funcoes import *


escolha = 1
while escolha != 0:
    try:
        print("=== LOCADORA ===")
        print("")
        print("1 - Cadastrar clientes")
        print("2 - Cadastrar filmes")
        print("3 - Cadastrar jogos")
        print("4 - Listar clientes")
        print("5 - Listar itens (filme ou jogo)")
        print("0 - sair")
        escolha = input("---> ")
        match escolha:
            case "1":
                cadastrar_clientes()
            case "2":
                cadastar_filmes()
            case "3":
                cadastrar_jogo()
            case "4":
                listar_clientes()
            case "5":
                listar_itens()
            case "0":
                break
            case _:
                print("Número inválido!")
        

    except Exception as e:
        print("Houve um erro {e} :(")
```
#### O menu utiliza as funções definidas em **funcoes.py**, que por sua vez manipulam os objetos das classes definidas em **classes.py**. Em vez de usar estruturas tradicionais `if/else`, utilizamos `match/case`, tudo dentro de um bloco `try/except` para melhorar a validação e tratar possíveis erros de entrada.
