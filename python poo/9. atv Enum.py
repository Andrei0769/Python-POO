from abc import ABC, abstractmethod
from enum import Enum
import os 

os.system("cls || clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos Humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"


class Funcionario: 
    def __init__(self, nome: str,idade: int, salario: float,setor: Setor, id:int, sexo: Sexo) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.Setor = setor
        self.sexo = sexo

    def __str__(self) -> str:
        return (f"\nDados do Funcionario: "
                f"\nNome: {self.nome}"
                f"\nidade: {self.idade}"
                f"\nSalario: {self.salario:.2f}"
                f"\nSetor: {self.Setor.value}"
                f"\nSexo: {self.sexo.value}")
    
Funcionario1 = Funcionario ("Andreei", 18, 2500, Setor.VENDAS, 4564, Sexo.MASCULINO)

print(Funcionario1)
