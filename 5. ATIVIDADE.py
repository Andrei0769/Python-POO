from abc import ABC, abstractmethod
import os 

os.system("cls || clear ")

class Endereco: 
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep

class funcionario:
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    #abstractmethod é para funcionar o ABC abstratto
    @abstractmethod
    def calcular_salario (self) -> float:
        pass
        
class Engengeiro(funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea 

    def calcular_salario(self) -> float:
        # BONIFICAÇÃO DE 12% 
        BONIFICACAO = 1.2
        salario_final = self.salario * BONIFICACAO
        return salario_final
    
class Medico(funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm

    def calcular_salario(self) -> float:
        # BONIFICAÇÃO DE 12% 
        BONIFICACAO = 1.2
        salario_final = self.salario * BONIFICACAO
        return salario_final

