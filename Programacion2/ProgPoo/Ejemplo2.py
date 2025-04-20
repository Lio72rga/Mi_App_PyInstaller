class cuenta_bancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
    def extraer(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
cuenta = cuenta_bancaria("Sofia", 1000)
cuenta.depositar(500)
print(cuenta.get_saldo()) #1500








        
        
