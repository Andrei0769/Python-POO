from abc import ABC, abstractmethod
import os 

os.system("cçs || clear")

class Endereco:
    def __init__(self, logradouro: str, numero: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade

    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}"
                f"Numero: {self.numero}"
                f"Cidade: {self.cidade}")
class Funcionario:
    def __init__(self, nome: str, email: str, salario: str, endereco:Endereco) -> None:
        self.nome = nome 
        self.email = email 
        self.salario = salario 
        self.endereco = endereco

    def __str__(self) -> str:
        return (f"Nome: {self.nome}"
                f"Email: {self.email}"
                f"Salario: {self.salario}"
                f"Endereço: {self.endereco}") 
class motoboy(Funcionario):
    def __init__(self, nome: str, email: str, salario: str, endereco: Endereco, cnh: str) -> None:
        super().__init__(nome, email, salario, endereco)
        self.cnh = cnh
        