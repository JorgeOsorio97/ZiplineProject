import pandas_datareader as web
from zipline.api import order,record,symbol
from zipline.algorithm import TradingAlgorithm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def initialize(context):
    context.asset = symbol('AAPL')
    context.invest = False


def handle_data(context, data):
    print("Corriendo algoritmo")


