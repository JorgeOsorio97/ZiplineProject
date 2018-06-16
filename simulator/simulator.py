import pandas as pd
import numpy as np


class Simulator:
    #Constructor donde se toman los siguientes parametros:

    ##security:
    ###Tipo Pandas.DataFrame debe tener OHLC 
    
    ##initCapital:(opcional)
    ###Tipo entero, el capital inicial de la simulacion 
    ###Si no se declara sera igual a stdPurchase * costo de la accion en el dia 0
    
    ##stdPurchase:(opcional)
    ###Acciones a comprar o vender cuando haya cambios
    ###Si no se declara es igual initCapital / costo de la accion en el dia 0
    def __init__(self, security, initCapital = None, stdPurchase = None):
        self.security = security

        if initCapital is not None and stdPurchase is not None:
            self.initCapital = initCapital
            self.stdPurchase = stdPurchase
        elif initCapital is not None:
            self.initCapital = initCapital
            self.stdPurchase = None
        elif stdPurchase is not None:
            self.initCapital = None
            self.stdPurchase = stdPurchase

    finCapital = 0
    indicators_names = []
    
    def add_indicator(self, name ='', decision = []):
        if len(self.security['Close']) == len(decision):
            self.security[name] = decision
            self.indicators_names.append(name)
    
    def calc_earning(self):
        if len(self.indicators_names)==0:
            return("Debes cargar los indicadores primero")
        for day in self.security.index.values:
            decision = []
            for indicator in self.indicators_names:
                decision.append(self.security[indicator][day])