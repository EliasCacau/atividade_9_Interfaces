from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
from manipulador import ManipuladorDeTributaveis
from tributavel import TributavelInterface
from seguro_de_vida import SeguroDeVida
from conta_investimento import ContaInvestimento
from banco import Banco

cc = ContaCorrente(12, "Alex", 1000)
seguro = SeguroDeVida(1, 100, cc)
banco = Banco(6060, "NuBank")
banco.inserir_conta(cc)
banco.inserir_seguro(seguro)

cc.saldo()
print()

TributavelInterface.register(ContaCorrente)
TributavelInterface.register(SeguroDeVida)

manipulador = ManipuladorDeTributaveis()
# Nome da pessoa da Conta Concorrente se repete devido ser tributado pela conta e pelo seguro de vida
banco.tributar()
banco.total_tributos()

cc.extrato.imprime()
cc.saldo()

print("\n--------------------------------------------\n")

cc2 = ContaCorrente(1, "Maria", 6000)
seguro2 = SeguroDeVida(2, 250, cc2)
cp = ContaPoupanca(2, "Victor", 100)
cc3 = ContaCorrente(3, "João", 9000)
seguro3 = SeguroDeVida(3, 1000, cc3)

banco.inserir_conta(cc2)
banco.inserir_conta(cp)
banco.inserir_conta(cc3)
banco.inserir_seguro(seguro2)
banco.inserir_seguro(seguro3)

print()

cp.saldo()
cc2.saldo()
cc3.saldo()

print()

manipulador = ManipuladorDeTributaveis()
# Nome da pessoa da Conta Concorrente se repete devido ser tributado pela conta e pelo seguro de vida
banco.tributar()
banco.total_tributos()

# Valor dos impostos: R$ 430.50

print()

cc2.extrato.imprime()
cc2.saldo()
print()
cc3.extrato.imprime()
cc3.saldo()
cp.extrato.imprime()
cp.saldo()

print("\n--------------------------------------------\n")

ci = ContaInvestimento(57, "Silvio", 700000)
seguro_ci = SeguroDeVida(57, 150000, ci)

banco.inserir_conta(ci)
banco.inserir_seguro(seguro_ci)

ci.saldo()
print()

TributavelInterface.register(ContaInvestimento)

manipulador = ManipuladorDeTributaveis()
# Nome da pessoa da Conta Concorrente se repete devido ser tributado pela conta e pelo seguro de vida
banco.tributar()
banco.total_tributos()

# Valor dos impostos: R$ 28534.00

print()

ci.extrato.imprime()
ci.saldo()

