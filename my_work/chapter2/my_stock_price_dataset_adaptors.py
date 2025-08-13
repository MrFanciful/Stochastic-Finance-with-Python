from yahoofinancials import YahooFinancials
from abc import ABC, abstractmethod, ABCMeta
import pandas as pd

import enum
import requests
from typing import List
import sys

class Frequency(enum.Enum):
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'


class StockPriceDatasetAdaptor(metaclass=ABCMeta):

    """
    Interface to access any data source of stock price quotes. Multiple implementations can be data sources
    """

    DEFAULT_TRACKER = 'PFE'

    @property
    @abstractmethod
    def training_set(self):
        ...

    """
    Function to get training dataset for a given stock symbol (ticker). This dataset can be used to train a stock price model.
    Although there is no such restriction on using it elsewhere
    
    Returns
    ----
    A dataframe. Each dataframe has two columns: stock price & time
    """