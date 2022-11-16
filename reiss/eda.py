import pandas as pd
import numpy as np
from numpy import nan
from scipy import stats
from datetime import date, datetime
import investpy
from pandas_datareader import data as pdr
from pandas_profiling import ProfileReport

df = pd.read_csv("GA2.csv", encoding='utf-8', sep=',')
profile = ProfileReport(df, title="Report")
profile.to_file("GA.html")

