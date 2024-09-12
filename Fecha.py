__author__ = "willy santiago solarte"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "willy.solarte@campusucc.edu.co"

class fecha:
    # Aqui inicia la declaracion de la clase

    '''#----------------------------------------
    #Atributos
    -------------------------------------------#'''

    dia = 0
    mes = 0
    anio = 0 

    '''#-----------------------------------------
    # Metodos
    --------------------------------------------#'''
    _method_  = "Dardia"
    _parameter_ = "Ninguno"
    _returns_ = "Dia"
    _Description_ = "metodo que regresa el dia"

    def Dardia(self):
        return self.dia
    
    _method_  = "Darmes"
    _parameter_ = "Ninguno"
    _returns_ = "Mes"
    _Description_ = "metodo que regresa el mes"

    def Darmes(self):
        return self.mes
    

    _method_  = "DarAnio"
    _parameter_ = "Ninguno"
    _returns_ = "Anio"
    _Description_ = "metodo que regresa el anio"

    def Daranio(self):
        return self.anio
    
    _method_  = "Darfecha"
    _parameter_ = "Ninguno"
    _returns_ = "La fecha de la clase"
    _Description_ = "metodo que regresa la fecha digitada por el usuario"

    def Darfecha(self):
        return self.dia+'/'+self.mes+'/'+self.anio
    
        
    