import os 

os.system("cls || clear")

class Endereco: 
    def __init__(self, logradouro: str, numero: int) -> None:
        self.logradouro = logradouro
        self.numero = numero
    
    def exibir_endereco(self) -> str:
        return f"\nLogradouro: {self.logradouro} \nNúmero: {self.numero}"

class aluno: 
    # nome , idade
    # construtor
    def __init__(self, nome : str, idade: int, endereco: Endereco ) -> None:
        #Atributos 
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade} \n=== Endereço === {self.endereco.exibir_endereco()}"


    
aluno1 = aluno("Andrei",18, Endereco("Rua B", 142))
aluno2 = aluno("Mariana",15, Endereco("Nova Brasilia ", 33))


print(f"== Exibindo Dados ==")
print(aluno1.exibir_dados())

print(f"\n== Exibindo Dados ==")
print(aluno2.exibir_dados())
