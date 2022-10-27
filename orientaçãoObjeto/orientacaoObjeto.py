from conta import Conta
from datas import Data

conta = Conta(123, 'bob', 100, 159)
conta2 = Conta(1223, 'marcu', 100, 1555)


conta.transferencia(conta2, 10000)

conta2.extrato()
conta.extrato()

Conta.codigo_banco()





      