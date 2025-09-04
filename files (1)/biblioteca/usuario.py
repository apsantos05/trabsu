class Usuario:
    def __init__(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula
        self._emprestimos = []

    @property
    def nome(self):
        return self._nome

    @property
    def matricula(self):
        return self._matricula

    @property
    def emprestimos(self):
        return self._emprestimos

    def pode_emprestar(self):
        return False  # Polimorfismo: implementado nas subclasses

    def registrar_emprestimo(self, emprestimo):
        self._emprestimos.append(emprestimo)

    def remover_emprestimo(self, emprestimo):
        self._emprestimos.remove(emprestimo)