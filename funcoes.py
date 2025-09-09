from classes import *

locadora = Locadora()


def cadastrar_cliente():
    print("Cadastro de Cliente")
    nome = input("Nome: ")
    cpf = input("CPF (11 dígitos): ")
    if len(cpf) != 11:
        print("CPF inválido!")
        return
    cliente = Cliente(nome, cpf)
    locadora.cadastrarCliente(cliente)
    print(f"Cliente {nome} cadastrado com sucesso!")


def cadastrar_filme():
    print("Cadastro de Filme")
    id = len(locadora.listarItens()) + 1
    titulo = input("Título: ")
    genero = input("Gênero: ")
    duracao = int(input("Duração (minutos): "))
    filme = Filme(id, titulo, genero, duracao)
    locadora.cadastrarItem(filme)
    print(f"Filme {titulo} cadastrado!")


def cadastrar_jogo():
    print("Cadastro de Jogo")
    id = len(locadora.listarItens()) + 1
    titulo = input("Título: ")
    plataforma = input("Plataforma: ")
    faixa = int(input("Faixa etária: "))
    jogo = Jogo(id, titulo, plataforma, faixa)
    locadora.cadastrarItem(jogo)
    print(f"Jogo {titulo} cadastrado!")


def cadastrar_filme_jogo():
    while True:
        print("1 - Cadastrar Filme")
        print("2 - Cadastrar Jogo")
        print("0 - Voltar")
        escolha = input("---> ")
        if escolha == "1":
            cadastrar_filme()
        elif escolha == "2":
            cadastrar_jogo()
        elif escolha == "0":
            break
        else:
            print("Opção inválida!")


def listar_clientes():
    clientes = locadora.listarClientes()
    if not clientes:
        print("Nenhum cliente cadastrado")
        return
    print("Clientes cadastrados:")
    print(f"{clientes.getNome()} | CPF: {clientes.getCpf()}")


def listar_filmes():
    itens = [i for i in locadora.listarItens() if isinstance(i, Filme)]
    if not itens:
        print("Nenhum filme cadastrado")
        return
    print("Filmes cadastrados:")
    if itens.isDisponivel():
        status = "Disponível" 
    else:
        "Alugado"
    print(f"{itens.getId()} - {itens.getTitulo()} | {itens.getGenero()} | {itens.getDuracao()} min | {status}")


def listar_jogos():
    itens = [i for i in locadora.listarItens() if isinstance(i, Jogo)]
    if not itens:
        print("Nenhum jogo cadastrado")
        return
    print("Jogos cadastrados:")
    if itens.isDisponivel():
        status = "Disponível" 
    else:
        "Alugado"
    print(f"{itens.getId()} - {itens.getTitulo()} | {itens.getPlataforma()} | {itens.getFaixaEtaria()}+ | {status}")


def listar():
    while True:
        try:
            print("1 - Listar Clientes")
            print("2 - Listar Filmes")
            print("3 - Listar Jogos")
            print("0 - Voltar")
            escolha = input("---> ")
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