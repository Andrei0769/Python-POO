from enum import Enum
import os

os.system("cls || clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"
    BISSEXUAL = "Bissexual"
    HOMOSEXXUAL = "Homossexual"

class Pessoa:
    def __init__(self, nome: str, telefone: int, cpf: str, idade: int, sexo: Sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.telefone = telefone
        self.cpf = cpf

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSexo: {self.sexo.value}"
                f"\nTelefone: {self.telefone}"
                f"\nCPF: {self.cpf}")
    
pessoa1 = Pessoa ("Brenda Maria", 7198422243, "0419.806.234.10", 20, Sexo.BISSEXUAL)
print(pessoa1)