class Historico:
    def __init__(self):
        self.transacoes = []

    def imprime(self):
        soma = ''
        for tr in self.transacoes:
            soma += (f"{tr}\n")
        return print(soma)
