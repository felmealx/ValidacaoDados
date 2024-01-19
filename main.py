
from Acesso_cep import BuscaEndereco

cep = "04181160"

obj = BuscaEndereco(cep)

bairro,cidade,uf = obj.acessa_via_cep()

print(bairro,cidade,uf)

