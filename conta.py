from datetime import datetime
from random import randint
import agencia

class CriarConta:
    
    @staticmethod #métodos internos
    def horario_agora():
        return datetime.today().strftime('%d-%m-%Y %H:%M:%S')
    
    
    def __init__(self,nome, cpf, agencia) -> None:
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0.0
        self._cheque_especial = None
        self._score = 1000
        self._transacoes = []
        self.cartoes = []
        self.agencia = agencia
        self.num_conta = randint(1000, 9999)
        agencia.clientes.append(self)

    def consultar_saldo(self):
        print(f"Seu saldo é de R${self._saldo:.2f}")

    def _limite(self): #underline == método não público
        self._cheque_especial = -self._score
        return self._cheque_especial

    def depositar(self, deposito, agencia):
        self._saldo += deposito
        #Colocando na lista de transações
        dict_deposit = {
            "Tipo": "Depósito",
            "Data": datetime.today().strftime('%Y-%m-%d %H:%M:%S'),
            "Valor depositado": deposito,
            "Saldo final": self._saldo
        }
        self._transacoes.append(dict_deposit)
        #####
        agencia.caixa += deposito
        print("Depósito realizado com sucesso")

    def sacar(self, saque):
        if self._saldo - saque >= self._limite():
            self._saldo -= saque
            #Colocando na lista de transações
            dict_saque = {
                "Tipo": "Saque",
                "Data": datetime.today().strftime('%d-%m-%Y %H:%M:%S'),
                "Valor sacado": saque,
                "Saldo final": self._saldo
        }
            self._transacoes.append(dict_saque)
            #####
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente")
            
    def solicitar_extrato(self):
        for transacao in self._transacoes:
            print(transacao)
            
    def transferir(self, valor ,conta_destino):
        if self._saldo - valor >= self._limite():
            self.agencia.caixa -= valor
            self._saldo -= valor
            
            conta_destino.agencia.caixa +=valor
            conta_destino._saldo += valor
            
            #Colocando na lista de transações
            dict_transf = {
                "Tipo": "Transferência",
                "Data": self.horario_agora(),
                "Valor transferido": valor,
                "Saldo final": self._saldo
        }
            dict_transf_recebida = {
                "Tipo": "Transferência Recebida",
                "Data": self.horario_agora(),
                "Valor transferido": valor,
                "Saldo final": conta_destino._saldo
        }
            self._transacoes.append(dict_transf)
            conta_destino._transacoes.append(dict_transf_recebida)
            #####
            
            print("Transferência realizada com sucesso")
        else:
            print("Saldo insuficiente")


class CriarCartao:
    
    def __init__(self, titular, conta_corrente) -> None:
        self.titular = titular
        self.numero = randint(1000000000000000, 9999999999999999)
        self.validade = f"{datetime.now().month}/{datetime.now().year + 4}"
        self.cv = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}"
        self.limite = None
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)
        self._senha = 1234
        
    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self,valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print("Nova senha inválida")
            