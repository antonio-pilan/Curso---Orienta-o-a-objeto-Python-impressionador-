import conta
from random import randint

#Ag. Genérica
class _CriarAgencia:
    
    def __init__(self, num ,cnpj, caixa_inicial,contato) -> None:
        self.agencia = num
        self.cnpj = cnpj
        self.contato = contato
        self.caixa = caixa_inicial
        self.clientes = []
        self.emprestimos = []
    
    def warning_caixa(self):
        if self.caixa < 1000000:
            print(f"Cuidado, caixa abaixo do recomendado: R${self.caixa:.2f}")
            return False
        else:
            return True

#Ag. Virtual
class AgenciaVirtual(_CriarAgencia):
    def __init__(self, cnpj, contato,site) -> None:
        self.site = site
        super().__init__(1, cnpj, 1500000, contato)

#Ag. Comum
class AgenciaComum(_CriarAgencia):
    def __init__(self, cnpj, contato) -> None:
        super().__init__(randint(1000,9999), cnpj, 1500000, contato)

#Ag. Premium
class AgenciaPremium(_CriarAgencia):
    def __init__(self, cnpj, contato) -> None:
        super().__init__(randint(10,100), cnpj, 10000000, contato)