import os 

os.system("cls || clear")


class Aluno: 
    # nome , idade
    # construtor
    def __init__(self, nome : str, idade: int ) -> None:
        #Atributos 
        self.nome = nome
        self.idade = idade
    
    def exibir_dados(self) -> str:
        return f"Nome: {self.nome} \nIdade: {self.idade} "


# Instanciar classes
aluno = Aluno ("Marta", 22)


print(aluno.exibir_dados())