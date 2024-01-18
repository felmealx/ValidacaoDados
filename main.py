from cpf_cnpj import Documento

ex_cnpj = "35379838000112"
documento = Documento.cria_documento(ex_cnpj)

ex_cpf = "40856189898"
documento1 = Documento.cria_documento(ex_cpf)

print(documento1)
print(documento)


