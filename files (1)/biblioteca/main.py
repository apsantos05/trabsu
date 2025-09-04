from aluno import Aluno
from professor import Professor
from livro import Livro
from servicos import emprestar_livro, devolver_livro

def gerar_relatorio(usuarios):
    print("Relatório de Livros Emprestados:")
    for usuario in usuarios:
        for emprestimo in usuario.emprestimos:
            print(f"{emprestimo.livro.titulo} emprestado para {usuario.nome} ({usuario.matricula})")

# Simulação
aluno1 = Aluno("Maria", "A123")
prof1 = Professor("Dr. João", "P456")
livro1 = Livro("POO na Prática", "S. Alencar")
livro2 = Livro("UML Descomplicada", "A. Lima")

usuarios = [aluno1, prof1]
livros = [livro1, livro2]

# Empréstimos válidos
emprestar_livro(aluno1, livro1)
emprestar_livro(prof1, livro2)

# Testando limites
try:
    for i in range(4):
        emprestar_livro(aluno1, Livro(f"Livro {i}", "Autor X"))
except Exception as e:
    print(e)  # Deve recusar o 4º empréstimo do aluno

# Devolução
devolver_livro(aluno1, livro1)

# Relatório
gerar_relatorio(usuarios)