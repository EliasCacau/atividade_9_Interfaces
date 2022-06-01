from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
from manipulador import ManipuladorDeTributaveis
from tributavel import TributavelInterface
from seguro_de_vida import SeguroDeVida
from conta_investimento import ContaInvestimento


cc = ContaCorrente(12, "Alex", 2500)
seguro = SeguroDeVida(1, 500, cc)


cc.saldo()
print()

TributavelInterface.register(ContaCorrente)
TributavelInterface.register(SeguroDeVida)

cc.valor_imposto()
seguro.valor_imposto()



cc.extrato.imprime()
cc.saldo()

print("\n--------------------------------------------\n")

cc2 = ContaCorrente(1, "Maria", 6000)
seguro2 = SeguroDeVida(2, 250, cc2)
cp = ContaPoupanca(2, "Victor", 100)
cc3 = ContaCorrente(3, "João", 9000)
seguro3 = SeguroDeVida(3, 1000, cc3)

cp.saldo()
cc2.saldo()
cc3.saldo()

print()

manipulador = ManipuladorDeTributaveis()
tributos = [cc2, seguro2, cp, cc3, seguro3]
# Nome da pessoa da Conta Concorrente se repete devido ser tributado pela conta e pelo seguro de vida
manipulador.calcular_impostos(tributos)

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

ci.saldo()
print()

TributavelInterface.register(ContaInvestimento)

tributos = [ci, seguro_ci]
# Nome da pessoa da Conta Concorrente se repete devido ser tributado pela conta e pelo seguro de vida
manipulador.calcular_impostos(tributos)

print()

ci.extrato.imprime()
ci.saldo()
