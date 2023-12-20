from validate_docbr import CPF,CNPJ
class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if tipo_documento == "cpf":
            if self.cpf_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF invalido !")
        elif tipo_documento == "cnpj":
            if self.cnpj_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ invalido !")
        else:
                raise ValueError("Tipo de documento invalido")
    def __str__(self):
        if self.tipo_documento == "cpf":
            return self.format_Cpf()
        elif self.tipo_documento == "cnpj":
            return self.format_Cnpj()
    def cpf_valido(self,documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de digitos invalida!!")
    def format_Cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def format_Cnpj(self):
        mascara = CNPJ()
        return  mascara.mask(self.cnpj)

    def cnpj_valido(self,cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de digitos invalida!!")