import abc


class TributavelInterface(abc.ABC):
    """
    Classe responsável pelas operações de um objeto autenticável as suas
    subclasses concretas devem sobreescrever o método "valor_imposto"
    """
    @abc.abstractmethod
    def valor_imposto(self):
        """"
        Método que tem como função aplicar a taxa de imposto sobre
        determinado valor do objeto
        """
        pass