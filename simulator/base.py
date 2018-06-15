import pandas as pd
import numpy as np


class Simulator:
    def __init__(self, securityDF, initCapital = None, stdPurchase = None):
        self.securityDF = securityDF

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
    
    def add_indicator(name ='', decision = []):
        if len(securityDF['Close']) == len(decision):
            