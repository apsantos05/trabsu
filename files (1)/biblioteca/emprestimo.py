from datetime import date, timedelta

class Emprestimo:
    def __init__(self, usuario, livro, prazo=7):
        self._usuario = usuario
        self._livro = livro
        self._data_retirada = date.today()
        self._prazo = prazo  # dias

    @property
    def usuario(self):
        return self._usuario

    @property
    def livro(self):
        return self._livro

    @property
    def data_retirada(self):
        return self._data_retirada

    @property
    def prazo(self):
        return self._prazo

    def data_devolucao(self):
        return self._data_retirada + timedelta(days=self._prazo)