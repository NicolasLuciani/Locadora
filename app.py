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
        print("6 - alocar item")
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
            case "6":
                alocar_item()
            case "0":
                break
            case _:
                print("Número inválido!")
        

    except Exception as e:
        print(f"Houve um erro {e} :(")