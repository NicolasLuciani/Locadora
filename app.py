from classes import *
from funcoes import *
import os

while True:
    try:
        os.system("cls")
        print("Bem-Vindo a locadora")
        os.system("pause")
        print("Escolha sua opção:")
        print("1 - Cadstrar cliente")
        print("2 - Cadastrar filme ou jogo")
        print("3 - Listar")
        print("0 - sair")
        escolha = int(input("--->"))

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
                print("Digite uma opção válida")
            
    except Exception as e:
        print(f"Ocorreu um erro ineperado {e}")
