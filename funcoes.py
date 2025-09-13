from classes import *

locadora = Locadora()


def cadastrar_cliente():
    try:
        print("Cadastro de Cliente")
        nome = input("Nome: ")
        cpf = input("CPF (11 dígitos): ")
        if len(cpf) != 11:
            print("CPF inválido!")
            return
        cliente = Cliente(nome, cpf)
        locadora.cadastrarCliente(cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")
        
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def cadastrar_filme():
    try:
        print("Cadastro de Filme")
        id = len(locadora.listarItens()) + 1
        titulo = input("Título: ")
        genero = input("Gênero: ")
        duracao = int(input("Duração (minutos): "))
        filme = Filme(id, titulo, genero, duracao)
        locadora.cadastrarItem(filme)
        print(f"Filme {titulo} cadastrado!")
        
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


def cadastrar_jogo():
    try:
        print("Cadastro de Jogo")
        id = len(locadora.listarItens()) + 1
        titulo = input("Título: ")
        plataforma = input("Plataforma: ")
        faixa = int(input("Faixa etária: "))
        jogo = Jogo(id, titulo, plataforma, faixa)
        locadora.cadastrarItem(jogo)
        print(f"Jogo {titulo} cadastrado!")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


def cadastrar_filme_jogo():
    try:
        while True:
            print("1 - Cadastrar Filme")
            print("2 - Cadastrar Jogo")
            print("0 - Voltar")
            escolha = input("---> ")
            match escolha:
                case "1":
                    cadastrar_filme()
                case "2":
                    cadastrar_jogo()
                case "0":
                    break
                case _:
                    print("Opção inválida!")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


def listar_clientes():
    try:
        clientes = locadora.listarClientes()
        if not clientes:
            print("Nenhum cliente cadastrado")
            return
        print("Clientes cadastrados:")
        print(f"{clientes.getNome()} | CPF: {clientes.getCpf()}")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def listar_filmes():
    try:
        if not itens:
            print("Nenhum filme cadastrado")
            return
        print("Filmes cadastrados:")
        if itens.isDisponivel():
            status = "Disponível" 
        else:
            "Alugado"
        print(f"{itens.getId()} - {itens.getTitulo()} | {itens.getGenero()} | {itens.getDuracao()} min | {status}")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


def listar_jogos():
    try:
        if not itens:
            print("Nenhum jogo cadastrado")
            return
        print("Jogos cadastrados:")
        if itens.isDisponivel():
            status = "Disponível" 
        else:
            "Alugado"
        print(f"{itens.getId()} - {itens.getTitulo()} | {itens.getPlataforma()} | {itens.getFaixaEtaria()}+ | {status}")

    except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


def listar():
    while True:
        try:
            print("1 - Listar Clientes")
            print("2 - Listar Filmes")
            print("3 - Listar Jogos")
            print("0 - Voltar")
            escolha = int(input("---> "))
            match escolha:
                case 1:
                    listar_clientes()
                case 2:
                    listar_filmes()
                case 3:
                    listar_jogos()
                case 0:
                    break
                case _:
                    print("Opção inválida!")

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
