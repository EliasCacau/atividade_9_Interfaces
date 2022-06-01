from conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, titular, saldo, numero):
        super().__init__(titular, saldo, numero)

    def atualiza(self, taxa):
        valor = self._saldo * taxa * 3
        self.depositar(valor)
        return valor