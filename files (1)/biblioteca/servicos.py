from emprestimo import Emprestimo

def emprestar_livro(usuario, livro, prazo=7):
    if not usuario.pode_emprestar():
        raise Exception("Usuário atingiu o limite de empréstimos.")
    if not livro.disponivel:
        raise Exception("Livro indisponível para empréstimo.")
    emprestimo = Emprestimo(usuario, livro, prazo)
    usuario.registrar_emprestimo(emprestimo)
    livro.emprestar()
    return emprestimo

def devolver_livro(usuario, livro):
    emprestimo = next((e for e in usuario.emprestimos if e.livro == livro), None)
    if not emprestimo:
        raise Exception("Empréstimo não encontrado para este livro e usuário.")
    usuario.remover_emprestimo(emprestimo)
    livro.devolver()