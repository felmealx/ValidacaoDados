class Cpf:

    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF invalido !")

    def __str__(self):
        return self.format_Cpf()
    def cpf_valido(self,documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def format_Cpf(self):
        fatia1 = self.cpf[:3]
        fatia2 = self.cpf[3:6]
        fatia3 = self.cpf[6:9]
        fatia4 = self.cpf[9:]

        cpf_formatado = "{}.{}.{}-{}".format(
            fatia1,
            fatia2,
            fatia3,
            fatia4
        )
        return cpf_formatado