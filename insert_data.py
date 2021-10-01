from typing import overload


def inf_init():
    nome = input("Seu nome: ")
    idade = inf_idade()
    return nome, idade


def inf_idade():
    idade = int(input("Sua idade: "))
    return idade

def inf_contato():
    print('Por favor insira seus contatos.')
    tel = input('Seu celular: ')
    email = input('insira seu email: ')
    endereco = input('Seu endereco: ')
    return tel, email, endereco
