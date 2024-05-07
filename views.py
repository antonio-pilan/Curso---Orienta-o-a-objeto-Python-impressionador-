import os
import conta
import agencia
import time

def criar_conta_view(agencia_virtual, agencia_comum, agencia_premium):
    nome = input("Digite seu nome completo: ")
    os.system("cls")
    cpf = input("Digite seu CPF fictício completo: ")
    os.system("cls")
    agencia = int(input("1) Agência Online\n2) Agência Comum\n3) Aplicar para Premium\nDigite sua escolha: "))
    os.system("cls")

    if agencia == 1:
        return conta.CriarConta(nome = nome, cpf = cpf, agencia = agencia_virtual)
    if agencia == 2:
        return conta.CriarConta(nome = nome, cpf = cpf, agencia = agencia_comum)
    if agencia == 3:
        patrimonio = int(input("Insira o valor do seu patrimônio (somente números): "))
        if patrimonio > 1000000:
            print("Solicitação aceita.")
            time.sleep(2)
            return conta.CriarConta(nome = nome, cpf = cpf, agencia = agencia_premium)
        else:
            print("Solicitação negada. Criando conta em Agência Virtual")
            time.sleep(2)
            return conta.CriarConta(nome = nome, cpf = cpf, agencia = agencia_virtual)
        
def menu_principal(conta):
    os.system("cls")
    print(f"Bem-Vindo ao Banco do Antonio,{conta.nome} (não clonamos cartões)")
    return int(input("1) Consultar saldo\n2) Depositar\n3) Sacar\n4) Transferir\n5) Solicitar Extrato\n6) Criar cartão de crédito\nQualquer outro número para sair\nDigite sua escolha: "))

def menu_saldo(conta):
    os.system("cls")
    conta.consultar_saldo()
    input("aperte qualquer botão para retornar ao menu principal")
    return 0

def menu_deposito(conta, agencia):
    os.system("cls")
    print(f"HEHEHE coloque seu dinheiro no nosso banco,{conta.nome}")
    valor = int(input("Qual valor deseja depositar? (somente numeros): "))
    conta.depositar(deposito = valor, agencia = agencia)
    input("aperte qualquer botão para retornar ao menu principal")
    return 0

def menu_saque(conta):
    os.system("cls")
    print(f"vai sacar? ...")
    valor = int(input("Qual valor deseja sacar? (somente numeros): "))
    conta.sacar(saque = valor)
    input("aperte qualquer botão para retornar ao menu principal")
    return 0

def menu_transferencia():
    os.system("cls")
    input("Em desenvolvimento, para essa parte do projeto preciso montar um banco de dados para conseguir consultar outras contas,\nPara proposta deste pequeno fragmento de treino, é algo que não faz sentido\n Aperte qualquer botão para voltar")
    return 0

def menu_extrato(acc):
    os.system("cls")
    print(f"Seu extrato... tá rico em pae")
    acc.solicitar_extrato()
    input("aperte qualquer botão para retornar ao menu principal")
    return 0

def menu_cartao(acc):
    os.system("cls")
    print("Seus Cartões:")
    for cartao in acc.cartoes:
        print(cartao)
        
    choice = int(input("1) Criar Cartão\n2) Voltar\nDigite sua escolha: "))

    if choice == 1:
        titular = input("titular do cartão: ")
        conta.CriarCartao(titular=titular, conta_corrente=acc)
        input("aperte qualquer botão para retornar ao menu principal")
        return 0
    else:
        return 0