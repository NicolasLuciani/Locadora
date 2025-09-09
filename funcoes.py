from classes import *
import os

def cadastrar_cliente(locadora):
    print("Vamos cadastrar o cliente!")
    print("")
    try:
        nome_cliente = input("Digite o nome\n--->")
        if not nome_cliente:
            ValueError("Digite algo para a validação!")

        cpf = input("Digite o CPF\n--->")
        if not cpf:
            ValueError("Digite o CPF corretamente")
        
        if len(cpf) != 11:
            ValueError("CPF possui exatamente 11 números!")


        cliente = Cliente(nome_cliente, cpf)
        locadora.cadastrarCliente(cliente)
        print("Cadastro realizado com sucesso!")



def cadastrar_filme_jogo():
    pass

#-------------------------------------------------------------------------------------------------------
def listar():
    pass

def listar_filme():
    pass

def listar_jogo():
    pass