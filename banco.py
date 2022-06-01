from manipulador import ManipuladorDeTributaveis


class Banco:
    def __init__(self, numero, nome):
        self._num = numero
        self._nome = nome
        self._contas = []
        self._caixa_geral = 0
        self._total_tributos = 0
        self._manipulador = ManipuladorDeTributaveis()
        self._seguros = []

    def inserir_conta(self, conta):
        self._contas.append(conta)

    def remover_conta(self, conta):
        self._contas.pop(conta)

    def inserir_seguro(self, seguro):
        self._contas.append(seguro)

    def remover_seguro(self, seguro):
        self._contas.pop(seguro)

    def listar_contas(self):
        caixa_temporario = 0
        for tr in self._contas:
            print(f'Extrato da conta {tr.numero}')
            tr.extrato.imprime()
            print('---------------------')
            print(f'Saldo final {tr.saldo}')
            print('---------------------')
            caixa_temporario += tr.saldo
        self._caixa_geral = caixa_temporario

    def total_banco(self):
        print(f'Total de dinheiro no banco: {self._caixa_geral}')

    def atualizar_contas(self, taxa):
        total_atualizacoes = 0
        total_saldo = 0
        for c in self._contas:
            print(c)
            total_atualizacoes += c.atualiza(taxa)
            total_saldo += c.saldo
            print(c)
        print(f'Total das atualizações: {total_atualizacoes}')
        print(f'Total dos saldos: {total_saldo}')

    def tributar(self):
        self._total_tributos += self._manipulador.calcular_impostos(self._contas + self._seguros)
        return self._total_tributos

    def total_tributos(self):
        return print(f"Valor de todos impostos no banco {self._nome}: R$ {self._total_tributos:.2f}")
