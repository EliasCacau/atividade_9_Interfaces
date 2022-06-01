from tributavel import TributavelInterface


class SeguroDeVida(TributavelInterface):
    def __init__(self, numero, valor, titular):
        self._numero = numero
        self._valor = valor
        self._titular = titular

    def __str__(self):
        return self._titular.nome()

    def valor_imposto(self):
        valor = self._valor * 0.05 + 34
        self._titular.sacar(self._valor * 0.05 + 34)
        return valor
