import re

email1 = 'Meu numero é 1234-1234'
email2 = 'Fale comigo em 1234-1234, esse é meu telefone'
email3 = '1234-1234 é o meu telefone'
email4 = 'lalala 99122-3323, 12341234'


padrao = "[0-9]{4,5}[-]*[0-9]{4}"

retorno = re.findall(padrao, email4)
print(retorno)
