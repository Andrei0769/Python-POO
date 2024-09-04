from abc import ABC, abstractmethod
import os

os.system("cls || clear")  # Limpa o terminal para uma visualização mais limpa dos resultados

class Endereco:
    def __init__(self, logradouro: str, numero: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade

    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}"
                f"\nNumero: {self.numero}"
                f"\nCidade: {self.cidade}")
        #### Retorna uma string formatada com as informações do endereço

class Funcionario:
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = nome
        self.email = email
        self.salario = salario
        self.endereco = endereco

    def __str__(self) -> str:
        return (f"\nDados do Funcionario: "
                f"\nNome: {self.nome}"
                f"\nEmail: {self.email}"
                f"\nSalario: {self.salario:.2f}"
                f"\n=== Endereço === {self.endereco}")
        #### Retorna uma string formatada com as informações do funcionário, incluindo o endereço

class motoboy(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco, cnh: str) -> None:
        if salario > 500:
            raise ValueError("O salário do motoboy não pode exceder R$500,00")
        super().__init__(nome, email, salario, endereco)  # Chama o construtor da classe base Funcionario
        self.cnh = cnh  # Adiciona um atributo específico para a classe motoboy

class gerente(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco) -> None:
        if salario > 6500:
            raise ValueError("O salário do gerente não pode exceder R$6500,00")
        super().__init__(nome, email, salario, endereco)  # Chama o construtor da classe base Funcionario

# Testando as classes
try:
    motoboy1 = motoboy("Josué", "Josué123@gmail.com", 500.0, # cria uma instância de motoboy
                       Endereco("Rua B", "420", "Salvador"), "4510.025")
    print(motoboy1)
except ValueError as error:
    print(error)

try:
    gerente1 = gerente("Carvalho", "JoséCaravlho@gmail.com", 6000.0, # cria uma instância de gerente
                       Endereco("Rua", "450 E", "Salvador"))
    print(gerente1)
except ValueError as error:
    print(error)
