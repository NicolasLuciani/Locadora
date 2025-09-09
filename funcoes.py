from classes import *
import os

Locadora = Locadora()

def cadastrar_cliente():
    print("Vamos cadastrar o cliente!")
    print("")
    try:
        nome_cliente = input("Digite o nome\n--->")
        if nome_cliente == "":
            ValueError("Digite algo para a validação!")

        cpf = input("Digite o CPF\n--->")
        if cpf == "":
            ValueError("Digite o CPF corretamente")
        
        if len(cpf) != 11:
            ValueError("CPF possui exatamente 11 números!")

        cliente = Cliente(nome_cliente, cpf)
        Locadora.cadastrarCliente(cliente)
        print("Cadastro realizado com sucesso!")
    
    except Exception as e:
        print(f"Ocorreu um erro ineperado {e}")

#-------------------------------------------------------------------------------------------------------
def cadstrar_filme():
    print("Vamos cadastrar seu filme")
    print("")
    try:
        titulo = input("Digite o titulo do filme\n--->")
        if titulo == "":
            ValueError("Digite algo para a validação")

        genero = input("Digite o gênero do filme\n--->")
        if genero == "":
            ValueError("Digite algo para a validação")

        print("Duração do filme:")
        h = input("Quantas horas possui o filme\n--->")
        if h == "":
            ValueError("Digite algo para a validação")
        h = int(h)

        m = input("Quantos minutos possui o filme\n--->")
        if m == "":
            ValueError("Digite algo para a validação")
        m = int(m)

        print(f"|Título: {titulo}|Gênero: {genero}|Duração:{h}/{m}")
        filme = Filme(titulo, genero, h, m)
        Locadora.cadastrarItens(filme)

    except Exception as e:
        print(f"Ocorreu um erro ineperado {e}")


def cadstrar_jogo():
    print("Vamos cadastrar seu jogo")
    print("")
    try:
        titulo = input("Digite o titulo do jogo\n--->")
        if titulo == "":
            ValueError("Digite algo para a validação")

        plataforma = input("Digite a plataforma do jogo\n--->")
        if plataforma == "":
            ValueError("Digite algo para a validação")

        fixaetaria = input("Digite a faixaEtaria do jogo\n--->")
        if fixaetaria ==  "":
            ValueError("Digite algo para a validação")

        jogo = Jogo(titulo, plataforma, fixaetaria)
        Locadora.cadastrarItens(jogo)
    
    except Exception as e:
        print(f"Ocorreu um erro ineperado {e}")

def cadastrar_filme_jogo():
    while True:
        try:
            print("Vamos cadastrar o filme ou um jogo")
            print("")
            print("1 - Jogo")
            print("2 - Filme")
            print("0 - sair")
            escolha = input("--->")

            match escolha:
                case 1:
                    cadstrar_jogo()
                case 2:
                    cadstrar_filme()
                case 0:
                    break
                case _:
                    print("Número inválido, uma opção válida por favor!")
            
        except Exception as e:
            print(f"Ocorreu um erro ineperado {e}")


#-------------------------------------------------------------------------------------------------------
def listar_clientes():
    print("--- CLIENTES ---")
    print("")
    if not Locadora.listarClientes:
        print("Nenhum cliente cadastrado")

    for id, cliente in enumerate(Locadora.cliente, start=1):
        print(f"{id} - Nome: {cliente.nome} | CPF: {cliente.cpf}")

def listar_filme():
    print("--- FILMES ---")
    print("")
    if not Locadora.cadastrarItens:
        print("Nenhum filme cadastrado")
    
    for id, filme in enumerate(Locadora.filme, start=1):
        print(f"{id} - Nome {filme.nome} | {filme.genero}")

def listar_jogo():
    print("--- JOGOS ---")
    print("")
    if not Locadora.cadastrarItens:
        print("Nenhum jogo cadastrado")
    
    for id, jogo in enumerate(Locadora.filme, start=1):
        print(f"{id} - Nome {jogo.nome} | {jogo.genero}")

def listar():
    while True:
        try:
            print("Vamos para a listagem")
            print("")
            print("1 - Listar clientes")
            print("2 - Listar filmes")
            print("3 - Listar jogos")
            print("0 - sair")
            escolha = int(input("--->"))

            match escolha:
                case 1:
                    listar_clientes()
                case 2:
                    listar_filme()
                case 3:
                    listar_jogo()
                case 0:
                    break
                case _:
                    print("Digite uma opção válida!")
        
        except Exception as e:
            print(f"Ocorreu um erro ineperado {e}")


