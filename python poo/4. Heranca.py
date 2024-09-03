from abc import ABC, abstractmethod
import os 

os.system("cls || clear ")


class funcionario:
    # nosso Contrutor  
    def __init__(self, nome: str, idade: int, salario: float) -> None:
        self.nome = nome 
        self.idade = idade 
        self.salario = salario
    
    # abstractmethod é para funcionar o ABC abstratto
    @abstractmethod
    def calcular_salario (self) -> float:
        pass
        
class Gerente(funcionario):
    def calcular_salario(self) -> float:
        # BONIFICAÇÃO DE 12% 
        BONIFICACAO = 1.2
        salario_final = self.salario * BONIFICACAO
        return salario_final

class mototoboy(funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario,)
        self.cnh = cnh
        
    def calcular_salario(self) -> float:
        # BONIFICAÇÃO DE 10% 
        BONIFICACAO = 1.1
        salario_final = self.salario * BONIFICACAO
        return salario_final


# EXIBINDO GERENTE
gerente1 = Gerente ("Andrei", 18, 1000.0)
print(f"\n=== DADOS DO GERENTE ===")
print(f"Nome: {gerente1.nome}")
print(f"Salario: {gerente1.calcular_salario()}")

# EXIBINDO MOTOBOY
motoboy1 = mototoboy ("josé", 20, 1000.0, "1234567")
print(f"\n=== DADOS DO MOTOBOY ===")
print(f"Nome: {motoboy1.nome}")
print(f"CNH: {motoboy1.cnh}")
print(f"Salario: {motoboy1.calcular_salario()}")
