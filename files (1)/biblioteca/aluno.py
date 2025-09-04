from usuario import Usuario

class Aluno(Usuario):
    LIMITE_EMPRESTIMOS = 3

    def pode_emprestar(self):
        return len(self.emprestimos) < self.LIMITE_EMPRESTIMOS