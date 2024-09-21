import os 
os.system("cls || clear ")

# Criando sua própia exceção
class SaldoInsuficienteError(Exception):
    pass
class ValorNegativoerror(Exception):
    pass

class Conta:
    def __init__(self, numero_conta: int, agencia: int) -> None:
        self.numero_conta = numero_conta
        self .agencia = agencia
        self._saldo = 0 # Atributo protegido

    @property 
    def saldo(self): # Para não precisar dos parantêses ()
        return self._saldo 

# FUNÇÃO DE SAQUE E # VERIFICAÇÃO DE TRY E EXCEPT
    def sacar(self, valor) -> float:
        try: 
            self.__verificar_saque(valor)
        except SaldoInsuficienteError as error:
            return f"Error: {error}" 

        self._saldo -= valor
        return self._saldo 
    
    def __verificar_saque(self,valor): #Metodo privado ////// # função para verificaar o saque 
        if valor > self.saldo: # isto é uma validação
            raise SaldoInsuficienteError(f"Saldo Insuficiente") # Capturando a excessão

    # FUNÇÃO DE DEPOSITAR
    def depositar (self, valor):
        # VERIFICAÇÃO DE TRY E EXCEPT
        try:
            self.__verificar_Deposito(valor)
        except ValorNegativoerror as error:
            return f"Error: {error}"
        
        self._saldo = valor 
        return self._saldo
    
    # PUXANDO A VERIFICAÇÃO QUE FOI FEITA PELO TRY - EXCEPT
    def __verificar_Deposito(self,valor):
        if valor <0:
            raise ValorNegativoerror("Não é possivel depositar valor negativo.")

class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

# instaciando classes. 
conta_corrente = ContaCorrente(222,333)
conta_poupanca = ContaPoupanca(444,666)

# Apresentado as variáveis do Codigo 
print (conta_corrente.saldo)
print(conta_corrente.sacar(100))
print(conta_corrente.depositar(-100))