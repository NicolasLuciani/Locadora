from funcoes import *
import os

while True:
    try:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n=== Locadora ===")
        print("1 - Cadastrar Cliente")
        print("2 - Cadastrar Filme ou Jogo")
        print("3 - Listar")
        print("0 - Sair")
        escolha = int(input("---> "))

        match escolha:
            case 1:
                cadastrar_cliente()
            case 2:
                cadastrar_filme_jogo()
            case 3:
                listar()
            case 0:
                break
            case _:
                print("Opção inválida!")

        input("\nPressione Enter para continuar...")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")