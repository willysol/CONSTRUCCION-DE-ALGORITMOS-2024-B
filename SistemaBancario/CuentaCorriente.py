__author__ = "willy santiago solarte"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "willy.solarte@campusucc.edu.co"

from Cliente import Cliente

class CuentaCorriente:

    #--------------------------------------
    # Atributos
    #-------------------------------------------

    __Saldo=0

    #--------------------------------------
    # Metodos
    #-------------------------------------------

    _method_  = "DarSaldo"
    _parameter_ = "Ninguno"
    _returns_ = "Saldo de la cuenta"         
    _Description_ = "metodo que muestra el saldo de la cuenta"
    def DarSaldo(self):
        return self.__Saldo
    
    _method_  = "ConsignarSaldo"
    _parameter_ = "Monto"
    _returns_ = "Ninguno"         
    _Description_ = "metodo que permite consignar un monto a la cuenta corriente"
    def consignarSaldo(self,monto):
        # aqui inicia mi codigo
        self.__Saldo=self.__saldo+monto

    _method_  = "retirarSaldo"
    _parameter_ = "Monto"
    _returns_ = "Ninguno"         
    _Description_ = "metodo que permite retirar un monto a la cuenta"
    def retirarSaldo(self,monto):
        # aqui inicia mi codigo
        self.__Saldo=self.__saldo+monto
    