from conta import Conta


class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo):
        super().__init__(numero, titular, saldo)

    def atualiza(self, taxa):
        valor = self._saldo * taxa * 2
        self.depositar(valor)
        self.sacar(0.1)
        return valor

    def valor_imposto(self):
        valor = self._saldo * 0.02
        ContaCorrente.sacar(self, valor)
        return valor
