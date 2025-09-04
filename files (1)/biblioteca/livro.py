class Livro:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor
        self._disponivel = True

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def disponivel(self):
        return self._disponivel

    def emprestar(self):
        if not self._disponivel:
            raise Exception("Livro já está emprestado.")
        self._disponivel = False

    def devolver(self):
        self._disponivel = True