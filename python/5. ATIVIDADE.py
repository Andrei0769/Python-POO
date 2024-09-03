from abc import ABC, abstractmethod  # Importa a classe base para definir classes abstratas
import os  

os.system("cls || clear")

class Endereco: 
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade 
    def exibir_ende(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero} \nComplemento: {self.complemento} \nCEP: {self.cep} \nCidade: {self.cidade}"
    

class Funcionario(ABC):  # Classe funcionario ABC (abstraact)
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
    def exibir_dados(self) -> str: 
        return f"Nome: {self.nome} \nTelefone: {self.telefone} \nEmail: {self.email} \nSalario: {self.salario} \n=== Endereço === {self.endereco.exibir_ende()}"
    
        
class Engenheiro(Funcionario):  # Classe de Engenheiro atribuido a classe de funcionario
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crea: str, salario: float) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea
        self.salario = salario  # chamando a função salario

   
class Medico(Funcionario): # Classe de Medico atribuido a classe de funcionario
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm: str, salario: float) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm
        self.salario = salario # chamando a função salario
    

# Criando um objeto da classe Engenheiro
engenheiro1 = Engenheiro("Andrei", "(71) 9 8811-2455", "andreil@gmail.com", 
                         Endereco("Rua B", "450 E", "Avenida", "4564.6641-020", "Salvador"), "4546.555", 2500.0)

print("== DADOS ENGENHEIRO ==")
print(engenheiro1.exibir_dados())
