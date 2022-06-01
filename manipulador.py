from tributavel import TributavelInterface

class ManipuladorDeTributaveis:
    def calcular_impostos(self, lista_tributaveis):
        total = 0
        for tr in lista_tributaveis:
            if isinstance(tr, TributavelInterface):
                print(f"A conta de {tr} é tributavel")
                total += tr.valor_imposto()
            else:
                print(f"A conta de {tr} não é tributavel")
        print(f'Valor dos impostos: R$ {total:.2f}')
        return total

