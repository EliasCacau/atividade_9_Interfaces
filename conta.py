from historico import Historico
import abc


class Conta(abc.ABC):
    __slots__ = ['_numero', '_titular', '_saldo', 'extrato']
    def __init__(self, numero, titular, saldo):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self.extrato = Historico()

    def __str__(self):
        return self._titular

    def nome(self):
        return self._titular

    @abc.abstractmethod
    def atualiza(self, taxa):
        pass

    def saldo(self):
        return print(f"Saldo na conta de {self._titular}: R$ {self._saldo:.2f}")

    def depositar(self, valor):
        self._saldo += valor
        self.extrato.transacoes.append(f'Depósito de R$ {valor:.2f} na conta de {self._titular}')

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo = self._saldo - valor
            self.extrato.transacoes.append(f'Saque de R$ {valor:.2f} na conta de {self._titular}')
        else:
            print("Saldo insuficiente!")
