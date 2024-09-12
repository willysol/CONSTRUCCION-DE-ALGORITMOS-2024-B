__author__ = "willy santiago solarte"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "willy.solarte@campusucc.edu.co"

"""-----------------------------------------------
# Atributos 
-------------------------------------------------"""

from Cuenta_de_ahorros import CuentadeAhorros
from CuentaCorriente import CuentaCorriente
from CDT import CDT

class  SimuladorBancario:

    """-----------------------------------------------
    # Atributos 
    -------------------------------------------------"""
    __descedula=""
    __nombre=""
    __mesActual= 0

    """-----------------------------------------------
    # Asociaciones
    -------------------------------------------------"""

    __CuentadeAhorros=CuentadeAhorros()
    __CuentaCorriente=CuentaCorriente()
    __CDT=CDT()

    """-----------------------------------------------
    # Metodos
    -------------------------------------------------"""

    _method_  = "DarSaldo"
    _parameter_ = "ninguno"
    _returns_ = "saldo de la cuenta"         
    _Description_ = "metodo que muestra el saldo de la cuenta"

    _method_  = "DepositarCuentaCorriente"
    _parameter_ = "monto"
    _returns_ = "ninguno"         
    _Description_ = "metodo que permite depositar en la cuenta corriente"
    def DepositarCuentaCorriente(self,monto):
        # Aqui inicia mi codigo 
        self.__CuentaCorriente.consignarSaldo(monto)

    _method_  = "CalcularSaldoTotal"
    _parameter_ = "ninguno"
    _returns_ = "Saldo total de todas las cuentas"         
    _Description_ = "metodo que permite calcular saldo total actual en todas las cuentas"
    def ConsultarSaldoTotal(self):
        #aqui inica mi codigo
        #metodo 1
        #total - self.__CuentaCorriente.DarSaldo()+self.__CuentadeAhorros.DarSaldo()
        #return total
        #metodo 2
        return"el saldo total es:" + self.__CuentadeAhorros.Darsaldo()+ self.__CuentaCorriente.Darsaldo()
    
    _method_  = "PasarAhorrosACorriente"
    _parameter_ = "ninguno"
    _returns_ = "ninguno"         
    _Description_ = "metodo que permite pasar saldo de la cuenta de ahorros a la cuenta corriente"
    def PasarAhorrosACorriente(self):
        #aqui inicia mi codigo
        saldoAhorros = self.__CuentadeAhorros.Darsaldo()
        self.__CuentadeAhorros.RetirarSaldo(saldoAhorros)
        self.__CuentaCorriente.consignarSaldo(saldoAhorros)

    _method_  = "Ahorrar"
    _parameter_ = "monto"
    _returns_ = "" 
    _Description_ = "pasa de la cuenta corriente a la cuenta de ahorros el valor que se entrega como parametro(suponiendo que hay suficientes fondos)"
    def ahorrar(self, monto):
        self.__CuentadeAhorros.RetirarValor(monto)
        self.__CuentaCorriente.consignarSaldo(monto)

    _method_  = "RetirarAhorro"
    _parameter_ = "monto"
    _returns_ = "" 
    _Description_ ="retira un valor dado de la cuenta de ahorros(suponiendo que hay suficiente fondos)"
    def RetirarAhorro(self,monto):
        self.__CuentadeAhorros.RetirarValor(monto)

    _method_  = "retirartodo"
    _parameter_ = ""
    _returns_ = "" 
    _Description_ ="Retira todo el dinero que hay en la cuenta corriente y en la cuenta de ahorros"
    def retirartodo(self):
        self.__CuentaCorriente.retirarSaldo(self.__CuentaCorriente.DarSaldo())
        self.__CuentadeAhorros.RetirarValor(self.__CuentadeAhorros.DarSaldo())

    _method_  = "duplicarAhorro"
    _parameter_ = ""
    _returns_ = "" 
    _Description_ ="Duplica la cantidad de dinero que hay en la cuenta de ahorros"
    def duplicarAhorros(self):
        self.__CuentadeAhorros.consignarvalor(self.__CuentadeAhorros.Darsaldo())

    _method_  = "DarSaldoCorriente"
    _parameter_ = ""
    _returns_ = "saldo" 
    _Description_ ="Retorna el saldo que hay en la cuenta corriente"
    def DarsaldoCorriente(self):
        # aqui inicia mi codigo
        return self.__CuentaCorriente.DarSaldo()
    




