from conta import Conta
from cliente import Cliente

# Instânciado a classe e criando dois objetos
conta1 = Conta(25, 'Júlio', 20.0, 200.0)
conta2 = Conta(24, 'Eduarda', 100.0, 300.0)

# Transferindo um valor de um objeto para o outro
conta2.transfere(20, conta1)

# Chamado os métodos dos objetos
conta1.extrato()
conta2.extrato()

# Tentando sacar mais que o limite disponível
conta1.saca(1000)

# Tentando sacar dentro do limite e em seguida imprimindo o saldo
conta1.saca(10)
conta1.extrato()

# Testando os métodos 'GET' e 'SET'
print('Seu limite é de {}'.format(conta1.limite))
print('Seu saldo é de {}'.format(conta1.get_saldo()))
print('Seu titular é de {}'.format(conta1.get_titular()))
conta1.limite = 3000
print('Seu novo limite é de {}'.format(conta1.limite))

# Instanciando a classe Cliente e chamando o método com
# o @property, e em seguinda, alterando o valor com o @nome.setter
cliente = Cliente('Júlio')
print(cliente.nome)
cliente.nome = 'Eduarda'
print(cliente.nome)

# Chamando o método estático da classe
codigos = Conta.codigos_bancos()
print(codigos)
