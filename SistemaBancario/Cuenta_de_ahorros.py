__author__ = "willy santiago solarte"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "willy.solarte@campusucc.edu.co"

from Cliente import Cliente
class CuentadeAhorros:

    # Aqui inicia la declaracion de la clase

    """#-------------------------------------
    # Atributos
    -----------------------------------------#"""

    saldo=0
    interes_mensual = 0.6



    _method_  = ""
    _parameter_ = ""
    _returns_ = ""         
    _Description_ = ""

    _method_  = "DarSaldo"
    _parameter_ = "Saldo"
    _returns_ = "Saldo"         
    _Description_ = "metodo que trasfiere valor a otra cuenta"
    def consignarvalor(self,nuevoValor):
        #aqui va el codigo
        self.saldo = self.saldo + nuevoValor

    _method_  = "DarValor"
    _parameter_ = "ninguno"
    _returns_ = "Saldo de la cuenta"         
    _Description_ = "metodo que muestra el saldo de la cuenta"
    def Darsaldo(self):
        # aqui va el codigo
        return self.saldo

    _method_  = "retirarValor"
    _parameter_ = "monto"
    _returns_ = "Saldo"         
    _Description_ = "metodo que permite retirar saldo de la cuenta"
    def RetirarValor(self,monto):
        #aqui va el codigo
        self.saldo = self.saldo-monto

    _method_  = "DarInteresMensual"
    _parameter_ = "ninguno"
    _returns_ = "Interes"         
    _Description_ = "metodo que muestra el interes de la cuenta"
    def DarInteresMensual(self):
        #aqui va el codigo
        return self.interes

    _method_  = "actualizarsaldoPorMes"
    _parameter_ = "Ninguno"
    _returns_ = "Saldo"         
    _Description_ = "metodo que actualiza el saldo"
    def actualizarSaldoPorPasoMes(self):
        #aqui va el codigo
        ""