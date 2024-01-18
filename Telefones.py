import re
class Telefones:
    def __init__(self,telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Numero Invalido")
    def valida_telefone(self,telefone):
        padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
        resposta = re.findall(padrao,telefone)
        if resposta:
            return True
        else:
            return  False
