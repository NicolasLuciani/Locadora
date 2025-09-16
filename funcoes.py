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