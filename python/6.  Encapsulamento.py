import os 
os.system("cls || clear ")

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self .agencia = agencia
        self._saldo = 0 # Atributo protegido

    @property 
    def saldo(self): # Para não precisar dos parantêses ()
        return self._saldo 
    
# função que faxz parte da classe se chama METODO
    def sacar(self, valor):
        if valor > self.saldo: # isto é uma validação
            return f"Saldo Insuficiente"
        self._saldo -= valor
        return self._saldo # retornando o valor após a validação do If 
    
    def depositar (self, valor):
        if valor < 0:
            return f"saldo invalido para depostitar"
        self._saldo = valor 
        return self._saldo

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

# instaciando classes. 
conta_corrente = ContaCorrente(222,333)
conta_poupanca = ContaPoupanca(444,666)

print (conta_corrente.saldo)
# print(conta_corrente.sacar(200))
print(conta_corrente.depositar(-200))