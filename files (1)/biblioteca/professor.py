from usuario import Usuario

class Professor(Usuario):
    LIMITE_EMPRESTIMOS = 5

    def pode_emprestar(self):
        return len(self.emprestimos) < self.LIMITE_EMPRESTIMOS