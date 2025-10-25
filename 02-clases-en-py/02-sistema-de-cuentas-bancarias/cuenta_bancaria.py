class FondosInsuficientes(Exception):
    pass
class CuentaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo
    def depositar(self, deposito):
        saldo_anterior = self._saldo
        if deposito > 0:
            self._saldo += deposito
            print(f'El saldo anterios era de: {saldo_anterior}|El deposito fue de: {deposito}|El saldo actual es de:{self._saldo}')
        else: 
            print(f'El deposito no puede ser {deposito}')
    def retirar(self, retiro):
        saldo_anterior = self._saldo
        if retiro <= self._saldo:
            self._saldo -= retiro
            print(f'El saldo anterior era de: {saldo_anterior}|El retiro fue de: {retiro}|El saldo actual es de:{self._saldo}')
        else:
            raise FondosInsuficientes("No hay fondos para ese retiro")
    def ver_saldo(self):
        return f'Este es tu saldo: {self._saldo}'

class CuentaDeAhorros(CuentaBancaria):
    def __init__(self, saldo, interes):
        super().__init__(saldo)
        self._interes = interes
    def aplicar_interes(self):
        saldo_anterior = self._saldo
        self._saldo += self._saldo * self._interes
        print(f'El saldo anterior era de:{saldo_anterior}|El interes aplicado es de:{self._interes*100}%|El saldo actual es de {self._saldo}')

try:
    cuenta_de_ale = CuentaBancaria(1000)
    cuenta_de_ale.depositar(10000)
    cuenta_de_ale.retirar(5000)
    cuenta_de_ahorros = CuentaDeAhorros(10000, 1200)
    cuenta_de_ahorros.depositar(10000)
    cuenta_de_ahorros.aplicar_interes()
    cuenta_de_ahorros.retirar(1000000)
    cuenta_de_ahorros.ver_saldo()
    print(cuenta_de_ale.ver_saldo())
except FondosInsuficientes as e:
    print(e)
