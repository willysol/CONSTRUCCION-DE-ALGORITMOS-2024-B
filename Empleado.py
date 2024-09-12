__author__ = "willy santiago solarte"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "willy.solarte@campusucc.edu.co"

from fecha import fecha


class empleado:
    # Aqui inicia la declaracion de la clase

    '''#----------------------------------------
    #Atributos
    -------------------------------------------#'''

    nombre = ""
    apellido = ""
    salario = 0 

    '''#-----------------------------------------
    # 1 = masculino, 2 = femenino
    ---------------------------------------------#'''

    sexo = 0
    '''#-----------------------------------------
    # Asociacion
    ---------------------------------------------#'''

    fechaingreso = fecha()
    fechanacimiento = fecha()

    '''#------------------------------------------
    # metodos
    ---------------------------------------------#'''

    _method_  = ""
    _parameter_ = ""
    _returns_ = ""
    _Description_ = ""
    def Darnombre(self):
        # Aqui va mi codigo
        return self.nombre
    
    _method_  = ""
    _parameter_ = ""
    _returns_ = ""         
    _Description_ = ""
    def cambiarSalario(self, nuevoSalario):
        #Aqui va mi codigo
        self.salario = nuevoSalario


    _method_  = ""
    _parameter_ = ""
    _returns_ = ""         
    _Description_ = ""
    def DarSalario(self):
        #Aqui va mi codigo
        return self.salario
    
    def consultarfechaIngreso(self):
        return self.fechaIngreso.Darfecha()
    
    _method_  = "CalcularSalarioAnual"
    _parameter_ = "Ninguno"
    _returns_ = "Salario Anual"         
    _Description_ = "muestra el salario anual del empleado"
    def CalcularSalarioAnual(self):
        # aqui va mi codigo
        # forma 1
        #total= self.salario*12
        #return total
        # forma 2
        return self.salario*12
    
    _method_  = "CalcularImpuestoSalarioAnual"
    _parameter_ = "Ninguno"
    _returns_ = "Impuesto del Salario Anual"         
    _Description_ = "muestra el impuesto del salario anual del empleado"
    def Calcularimpuestosalarioanual(self):
        # Aqui inicia mi codigo
        # forma 1 
        #SalarioAnual=self.CalcularSalarioAnual()
        #impuestoAnual=SalarioAnual*0.19
        #return impuestoAnual
        # forma 2
        return self.CalcularSalarioAnual()*0.19
    
    _method_  = "CalcularImpuestoSalario"
    _parameter_ = "Ninguno"
    _returns_ = "Impuesto del Salario"         
    _Description_ = "muestra el impuesto del salario del empleado"
    def CalcularimpuestoSalarioAnual(self):
        # Aqui inicia mi codigo
        return self.CalcularSalarioAnual()*0.19
    
    
    
    
    

