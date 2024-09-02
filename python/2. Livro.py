import os 

os.system("cls || clear")

class livro: 

    def __init__(self,titulo:str,autor: str,numeroDePaginas: int,preco: float):
        self.titulo = titulo
        self.autor = autor
        self.numeroDePaginas = numeroDePaginas
        self.preco = preco


    def exibir_Resultado(self) -> str:
        return f"Titulo: {self.titulo} \nAutor: {self.autor} \nNumero de Paginas: {self.numeroDePaginas} \nPreço: {self.preco} "
    
Primeiro_Livro = livro ("Pequeno Principe", "Silvão do Corte", 22, 25.62)

print(f"===Exibindo Dados===")
print(Primeiro_Livro.exibir_Resultado())