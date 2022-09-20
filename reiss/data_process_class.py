import pandas
import pandas as pd
import numpy as np
from numpy import nan
from scipy import stats
from data_process_global import *
import ta
from ta.utils import dropna


class DataProcess(object):
    def __init__(self, data_path, excel_or_csv="", data_path1="", data_path2="", data_path3="", data_path4="",
                 data_path5="", data_path6="", data_path7="", data_path8="", data_path9=""):

        if excel_or_csv == "csv":
            self.df = pd.read_csv(data_path, sep=',', encoding = 'unicode_escape')
            self.df_list = [self.df]
            if data_path1 != "":
                self.df1 = pd.read_csv(data_path1, sep=',', encoding = 'unicode_escape')
                self.df_list.append(self.df1)
            if data_path2 != "":
                self.df2 = pd.read_csv(data_path2, sep=',', encoding = 'unicode_escape')
                self.df_list.append(self.df2)
            if data_path3 != "":
                self.df3 = pd.read_csv(data_path3, sep=',', encoding = 'unicode_escape')
                self.df_list.append(self.df3)
            if data_path4 != "":
                self.df4 = pd.read_csv(data_path4, sep=',', encoding = 'unicode_escape')
                self.df_list.append(self.df4)
            if data_path5 != "":
                self.df5 = pd.read_csv(data_path5, sep=',', encoding = 'unicode_escape')
                self.df_list.append(self.df5)
            if data_path6 != "":
                self.df6 = pd.read_csv(data_path6, sep=',', encoding = 'unicode_escape')
                self.df_list.append(self.df6)
            if data_path7 != "":
                self.df7 = pd.read_csv(data_path7, sep=',', encoding = 'unicode_escape')
                self.df_list.append(self.df7)
            if data_path8 != "":
                self.df8 = pd.read_csv(data_path8, sep=',', encoding = 'unicode_escape')
                self.df_list.append(self.df8)
            if data_path9 != "":
                self.df9 = pd.read_csv(data_path9, sep=',', encoding = 'unicode_escape')
                self.df_list.append(self.df9)
        else:
            self.df = pd.read_excel(data_path)
            self.df_list = [self.df]
            if data_path1 != "":
                self.df1 = pd.read_excel(data_path1)
                self.df_list.append(self.df1)
            if data_path2 != "":
                self.df2 = pd.read_excel(data_path2)
                self.df_list.append(self.df2)
            if data_path3 != "":
                self.df3 = pd.read_excel(data_path3)
                self.df_list.append(self.df3)
            if data_path4 != "":
                self.df4 = pd.read_excel(data_path4)
                self.df_list.append(self.df4)
            if data_path5 != "":
                self.df5 = pd.read_excel(data_path5)
                self.df_list.append(self.df5)
            if data_path6 != "":
                self.df6 = pd.read_excel(data_path6)
                self.df_list.append(self.df6)
            if data_path7 != "":
                self.df7 = pd.read_excel(data_path7)
                self.df_list.append(self.df7)
            if data_path8 != "":
                self.df8 = pd.read_excel(data_path8)
                self.df_list.append(self.df8)
            if data_path9 != "":
                self.df9 = pd.read_excel(data_path9)
                self.df_list.append(self.df9)

        self.df_len = len(self.df)

    # dfs: data frames
    # dps: data paths
    def export(self, dps, excel_or_csv=""):
        if len(dps) == len(self.dfs):

            if excel_or_csv == "csv":
                for i in range(len(self.dfs)):
                    self.dfs[i].to_csv(dps[i])
                print("Exported To:", dps)

            else:
                for i in range(len(self.dfs)):
                    self.dfs[i].to_excel(dps[i])
                print("Exported To:", dps)

        else:
            print("Incorrect Number of Data Paths")
            print("Data Paths: ", len(dps))
            print("Data Frames: ", len(self.dfs))


class DropExchangeClose(DataProcess):
    def __init__(self, data_path, data_path1, data_path2, data_path3):
        super().__init__(data_path=data_path, data_path1=data_path1, data_path2=data_path2,
                         data_path3=data_path3)

    def process(self):
        for i in range(len(self.df)):
            if self.df.loc[i, "SPY_CLOSE"] == self.df.loc[i, "SH_CLOSE"] == self.df.loc[i, "IYR_CLOSE"] == self.df.loc[
                i, "GLD_CLOSE"] == 0:
                self.df.drop(index=i, inplace=True)
                self.df1.drop(index=i, inplace=True)
                self.df2.drop(index=i, inplace=True)
                self.df3.drop(index=i, inplace=True)

        self.df.reset_index(inplace=True)
        self.df1.reset_index(inplace=True)
        self.df2.reset_index(inplace=True)
        self.df3.reset_index(inplace=True)

        self.dfs = [self.df, self.df1, self.df2, self.df3]


class DropExchangeCloseVIX(DataProcess):
    def __init__(self, data_path):
        super().__init__(data_path=data_path)

    def process(self):
        for i in range(len(self.df)):
            if self.df.loc[i, "VIX_CLOSE"] == 0:
                self.df.drop(index=i, inplace=True)

        self.df.reset_index(inplace=True)

        self.dfs = [self.df]


class DropNoData(DataProcess):
    def __init__(self, data_path):
        super().__init__(data_path=data_path)

    def process(self):
        for column in self.df:
            if self.df.loc[0][column] == 0:
                self.df.drop(column, inplace=True, axis=1)

        self.dfs = [self.df]


class DropOpenClose(DataProcess):
    def __init__(self, data_path, data_path1):
        super().__init__(data_path=data_path, data_path1=data_path1)

    def process(self, ETFS=("")):
        for i in ETFS:
            self.df.drop(i + "_OPEN", inplace=True, axis=1)
            self.df.drop(i + "_CLOSE", inplace=True, axis=1)
            self.df1.drop(i + "_OPEN", inplace=True, axis=1)
            self.df1.drop(i + "_CLOSE", inplace=True, axis=1)

        self.dfs = [self.df, self.df1]


class DropNA(DataProcess):
    def __init__(self, data_path):
        super().__init__(data_path=data_path)

    def process(self, na="na"):
        for i in range(len(self.df)):
            if self.df.loc[i]["Bull-Bear Spread"] == na:
                self.df.drop(index=i, inplace=True)

        self.df.reset_index(inplace=True)

        self.dfs = [self.df]


class MACD(DataProcess):
    def __init__(self, data_path):
        super().__init__(data_path=data_path)

    def process(self, EMA_short_rw=12, EMA_long_rw=26, input="SPY"):
        self.df = self.df[["Date", input + "_CLOSE"]]
        self.df["EMA" + str(EMA_short_rw)] = ["_"] * len(self.df)
        self.df["EMA" + str(EMA_long_rw)] = ["_"] * len(self.df)
        self.df["MACD"] = ["_"] * len(self.df)

        EMA_func(df=self.df, rolling_window=EMA_short_rw, init_index=EMA_short_rw - 1, input=input + "_CLOSE",
                 output="EMA" + str(EMA_short_rw))
        EMA_func(df=self.df, rolling_window=EMA_long_rw, init_index=EMA_long_rw - 1, input=input + "_CLOSE",
                 output="EMA" + str(EMA_long_rw))
        MACD_func(df=self.df, EMA_short="EMA" + str(EMA_short_rw), EMA_long="EMA" + str(EMA_long_rw), output="MACD")

        self.dfs = [self.df]


class ADX(DataProcess):
    def __init__(self, data_path, data_path1):
        super().__init__(data_path=data_path, data_path1=data_path1)

    def process(self, input="SPY", rw=14):
        self.df = self.df[["Date", input + "_CLOSE"]]
        self.df[input + "_HIGH"] = self.df1[input + "_HIGH"]
        self.df[input + "_LOW"] = self.df1[input + "_LOW"]

        self.df["High_t Less Low_t"] = ["_"] * len(self.df)
        self.df["High_t Less Close_t-1"] = ["_"] * len(self.df)
        self.df["Low_t Less Close_t-1"] = ["_"] * len(self.df)
        self.df["True Range"] = ["_"] * len(self.df)
        self.df["Positive DM"] = ["_"] * len(self.df)  # DM: Directional Movement
        self.df["Negative DM"] = ["_"] * len(self.df)
        self.df["Smoothed True Range"] = ["_"] * len(self.df)
        self.df["Smoothed Positive DM"] = ["_"] * len(self.df)
        self.df["Smoothed Negative DM"] = ["_"] * len(self.df)
        self.df["Positive Directional Indicator"] = ["_"] * len(self.df)
        self.df["Negative Directional Indicator"] = ["_"] * len(self.df)
        self.df["DX"] = ["_"] * len(self.df)
        self.df["ADX"] = ["_"] * len(self.df)

        for i in range(1, len(self.df)):
            self.df.at[i, "High_t Less Low_t"] = self.df.loc[i][input + "_HIGH"] - self.df.loc[i][input + "_LOW"]
            self.df.at[i, "High_t Less Close_t-1"] = abs(
                self.df.loc[i][input + "_HIGH"] - self.df.loc[i - 1][input + "_CLOSE"])
            self.df.at[i, "Low_t Less Close_t-1"] = abs(
                self.df.loc[i][input + "_LOW"] - self.df.loc[i - 1][input + "_CLOSE"])
            self.df.at[i, "True Range"] = max(self.df.loc[i]["High_t Less Low_t"],
                                              self.df.loc[i]["High_t Less Close_t-1"],
                                              self.df.loc[i]["Low_t Less Close_t-1"])

            # derive Positive DM
            if (self.df.loc[i][input + "_HIGH"] - self.df.loc[i - 1][input + "_HIGH"]) > (
                    self.df.loc[i - 1][input + "_LOW"] - self.df.loc[i][input + "_LOW"]):
                self.df.at[i, "Positive DM"] = self.df.loc[i][input + "_HIGH"] - self.df.loc[i - 1][input + "_HIGH"]
            else:
                self.df.at[i, "Positive DM"] = 0

            # derive Negative DM
            if (self.df.loc[i - 1][input + "_LOW"] - self.df.loc[i][input + "_LOW"]) > (
                    self.df.loc[i][input + "_HIGH"] - self.df.loc[i - 1][input + "_HIGH"]):
                self.df.at[i, "Negative DM"] = self.df.loc[i - 1][input + "_LOW"] - self.df.loc[i][input + "_LOW"]
            else:
                self.df.at[i, "Negative DM"] = 0

        # initiate smooth
        sum_POSITIVE = 0
        sum_NEGATIVE = 0
        sum_TRUE_RANGE = 0
        for i in range(1, rw + 1):
            sum_POSITIVE += self.df.loc[i]["Positive DM"]
            sum_NEGATIVE += self.df.loc[i]["Negative DM"]
            sum_TRUE_RANGE += self.df.loc[i]["True Range"]
        self.df.at[rw, "Smoothed Positive DM"] = sum_POSITIVE
        self.df.at[rw, "Smoothed Negative DM"] = sum_NEGATIVE
        self.df.at[rw, "Smoothed True Range"] = sum_TRUE_RANGE

        # derive smooth
        for i in range(rw + 1, len(self.df)):
            self.df.at[i, "Smoothed Positive DM"] = self.df.loc[i - 1]["Smoothed Positive DM"] - (
                    self.df.loc[i - 1]["Smoothed Positive DM"] / rw) + self.df.loc[i]["Positive DM"]
            self.df.at[i, "Smoothed Negative DM"] = self.df.loc[i - 1]["Smoothed Negative DM"] - (
                    self.df.loc[i - 1]["Smoothed Negative DM"] / rw) + self.df.loc[i]["Negative DM"]
            self.df.at[i, "Smoothed True Range"] = self.df.loc[i - 1]["Smoothed True Range"] - (
                    self.df.loc[i - 1]["Smoothed True Range"] / rw) + self.df.loc[i]["True Range"]

        # derive directional indicator, DX
        for i in range(rw, len(self.df)):
            # indicator as a percentage
            self.df.at[i, "Positive Directional Indicator"] = (self.df.loc[i]["Smoothed Positive DM"] / self.df.loc[i][
                "Smoothed True Range"]) * 100
            self.df.at[i, "Negative Directional Indicator"] = (self.df.loc[i]["Smoothed Negative DM"] / self.df.loc[i][
                "Smoothed True Range"]) * 100

            self.df.at[i, "DX"] = abs((self.df.loc[i]["Positive Directional Indicator"] - self.df.loc[i][
                "Negative Directional Indicator"]) / abs(
                self.df.loc[i]["Positive Directional Indicator"] + self.df.loc[i][
                    "Negative Directional Indicator"])) * 100

        # initiate ADX
        sum_DX = 0
        for i in range(rw, rw * 2):
            sum_DX += self.df.loc[i]["DX"]
        avg_DX = sum_DX / rw
        self.df.at[(rw * 2) - 1, "ADX"] = avg_DX

        # derive ADX
        for i in range(rw * 2, len(self.df)):
            self.df.at[i, "ADX"] = ((self.df.loc[i - 1]["ADX"] * (rw - 1)) + self.df.loc[i]["DX"]) / rw

        self.dfs = [self.df]


class OBV(DataProcess):
    def __init__(self, data_path, data_path1):
        super().__init__(data_path=data_path, data_path1=data_path1)

    def process(self, input="SPY"):
        self.df = self.df[["Date", input + "_CLOSE"]]
        self.df[input + "_VOLUME"] = self.df1[input + "_VOLUME"] * 1000000
        self.df["OBV"] = ["_"] * len(self.df)

        self.df.at[0, "OBV"] = self.df.loc[0][input + "_VOLUME"]

        for i in range(1, len(self.df)):
            if self.df.loc[i][input + "_CLOSE"] > self.df.loc[i - 1][input + "_CLOSE"]:
                self.df.at[i, "OBV"] = self.df.loc[i - 1]["OBV"] + self.df.loc[i][input + "_VOLUME"]
            elif self.df.loc[i][input + "_CLOSE"] < self.df.loc[i - 1][input + "_CLOSE"]:
                self.df.at[i, "OBV"] = self.df.loc[i - 1]["OBV"] - self.df.loc[i][input + "_VOLUME"]
            else:
                self.df.at[i, "OBV"] = self.df.loc[i - 1]["OBV"]

        self.dfs = [self.df]


class BB(DataProcess):
    def __init__(self, data_path):
        super().__init__(data_path=data_path)

    def process(self, rw=20, stddev=2, input="SPY"):
        self.df = self.df[["Date", input + "_CLOSE"]]
        self.df[str(rw) + "D_SMA"] = ["_"] * len(self.df)
        self.df[str(rw) + "D_STDDEV"] = ["_"] * len(self.df)
        self.df["UPPER_BAND"] = ["_"] * len(self.df)
        self.df["LOWER_BAND"] = ["_"] * len(self.df)

        for i in range(rw - 1, len(self.df)):
            arr = []
            for j in range(i - (rw - 1), i + 1):
                arr.append(self.df.loc[j][input + "_CLOSE"])
            self.df.at[i, str(rw) + "D_SMA"] = np.mean(arr)
            self.df.at[i, str(rw) + "D_STDDEV"] = np.std(arr, ddof=1)
            self.df.at[i, "UPPER_BAND"] = self.df.loc[i][str(rw) + "D_SMA"] + (
                    stddev * self.df.loc[i][str(rw) + "D_STDDEV"])
            self.df.at[i, "LOWER_BAND"] = self.df.loc[i][str(rw) + "D_SMA"] - (
                    stddev * self.df.loc[i][str(rw) + "D_STDDEV"])

        self.dfs = [self.df]


class MacroQoQ(DataProcess):
    def __init__(self, data_path):
        super().__init__(data_path=data_path)

    def process(self):
        self.df["OECD_LI_US_DEL"] = ["_"] * len(self.df)
        self.df["CB_LI_US_DEL"] = ["_"] * len(self.df)
        self.df["M2_US_DEL"] = ["_"] * len(self.df)
        self.df["CPI_US_DEL"] = ["_"] * len(self.df)
        self.df["NEW_DATA"] = ["_"] * len(self.df)
        self.df["OECD_LI_US_QoQ"] = ["_"] * len(self.df)
        self.df["CB_LI_US_QoQ"] = ["_"] * len(self.df)
        self.df["M2_US_QoQ"] = ["_"] * len(self.df)
        self.df["CPI_US_QoQ"] = ["_"] * len(self.df)

        # identify date of new data
        for i in range(1, len(self.df)):
            if self.df.loc[i]["OECD_LI_US"] != self.df.loc[i - 1]["OECD_LI_US"]:
                self.df.at[i, "OECD_LI_US_DEL"] = 1
            else:
                self.df.at[i, "OECD_LI_US_DEL"] = 0

            if self.df.loc[i]["CB_LI_US"] != self.df.loc[i - 1]["CB_LI_US"]:
                self.df.at[i, "CB_LI_US_DEL"] = 1
            else:
                self.df.at[i, "CB_LI_US_DEL"] = 0

            if self.df.loc[i]["M2_US"] != self.df.loc[i - 1]["M2_US"]:
                self.df.at[i, "M2_US_DEL"] = 1
            else:
                self.df.at[i, "M2_US_DEL"] = 0

            if self.df.loc[i]["CPI_US"] != self.df.loc[i - 1]["CPI_US"]:
                self.df.at[i, "CPI_US_DEL"] = 1
            else:
                self.df.at[i, "CPI_US_DEL"] = 0

            if self.df.loc[i]["OECD_LI_US_DEL"] == self.df.loc[i]["CB_LI_US_DEL"] == self.df.loc[i]["M2_US_DEL"] == \
                    self.df.loc[i]["CPI_US_DEL"] == 0:
                self.df.at[i, "NEW_DATA"] = 0
            else:
                self.df.at[i, "NEW_DATA"] = 1

        # initialize %QoQ
        self.df.at[9, "OECD_LI_US_QoQ"] = pctDel(self.df.loc[9]["OECD_LI_US"],
                                                 self.df.loc[9 - 5]["OECD_LI_US"])  # 5 chosen arbitrarily
        self.df.at[9, "CB_LI_US_QoQ"] = pctDel(self.df.loc[9]["CB_LI_US"], self.df.loc[9 - 5]["CB_LI_US"])
        self.df.at[9, "M2_US_QoQ"] = pctDel(self.df.loc[9]["M2_US"], self.df.loc[9 - 5]["M2_US"])
        self.df.at[9, "CPI_US_QoQ"] = pctDel(self.df.loc[9]["CPI_US"], self.df.loc[9 - 5]["CPI_US"])

        # derive %QoQ
        for i in range(10, len(self.df)):
            if self.df.loc[i]["NEW_DATA"] == 1:
                self.df.at[i, "OECD_LI_US_QoQ"] = pctDel(self.df.loc[i]["OECD_LI_US"], self.df.loc[i - 5]["OECD_LI_US"])
                self.df.at[i, "CB_LI_US_QoQ"] = pctDel(self.df.loc[i]["CB_LI_US"], self.df.loc[i - 5]["CB_LI_US"])
                self.df.at[i, "M2_US_QoQ"] = pctDel(self.df.loc[i]["M2_US"], self.df.loc[i - 5]["M2_US"])
                self.df.at[i, "CPI_US_QoQ"] = pctDel(self.df.loc[i]["CPI_US"], self.df.loc[i - 5]["CPI_US"])
            else:
                self.df.at[i, "OECD_LI_US_QoQ"] = self.df.at[i - 1, "OECD_LI_US_QoQ"]
                self.df.at[i, "CB_LI_US_QoQ"] = self.df.at[i - 1, "CB_LI_US_QoQ"]
                self.df.at[i, "M2_US_QoQ"] = self.df.at[i - 1, "M2_US_QoQ"]
                self.df.at[i, "CPI_US_QoQ"] = self.df.at[i - 1, "CPI_US_QoQ"]

        self.dfs = [self.df]


class YieldCurve(DataProcess):
    def __init__(self, data_path):
        super().__init__(data_path=data_path)

    def process(self, rw=5):
        self.df["10Y-2Y_EMA" + str(rw)] = ["_"] * len(self.df)
        self.df["10Y-3M_EMA" + str(rw)] = ["_"] * len(self.df)
        self.df["10Y-2Y_DEL"] = ["_"] * len(self.df)
        self.df["10Y-3M_DEL"] = ["_"] * len(self.df)

        EMA_func(df=self.df, rolling_window=rw, init_index=rw - 1, input="10Y-2Y", output="10Y-2Y_EMA" + str(rw))
        EMA_func(df=self.df, rolling_window=rw, init_index=rw - 1, input="10Y-3M", output="10Y-3M_EMA" + str(rw))

        # derive delta (bps)
        for i in range(1, len(self.df)):
            self.df.at[i, "10Y-2Y_DEL"] = 100 * (self.df.loc[i]["10Y-2Y"] - self.df.loc[i - 1]["10Y-2Y"])
            self.df.at[i, "10Y-3M_DEL"] = 100 * (self.df.loc[i]["10Y-3M"] - self.df.loc[i - 1]["10Y-3M"])

        self.dfs = [self.df]


class ProcessVIX(DataProcess):
    def __init__(self, data_path):
        super().__init__(data_path=data_path)

    def process(self, ema_rw=5, stddev_rw=5):
        self.df["VIX_EMA" + str(ema_rw)] = ["_"] * len(self.df)
        self.df["VIX_DEL"] = ["_"] * len(self.df)
        self.df["VIX_DEL_STDDEV"] = ["_"] * len(self.df)

        EMA_func(df=self.df, rolling_window=ema_rw, init_index=ema_rw - 1, input="VIX_CLOSE",
                 output="VIX_EMA" + str(ema_rw))

        # derive delta (bps)
        for i in range(1, len(self.df)):
            self.df.at[i, "VIX_DEL"] = 100 * (self.df.loc[i]["VIX_CLOSE"] - self.df.loc[i - 1]["VIX_CLOSE"])

        # derive delta's (bps) volatility
        for i in range(stddev_rw, len(self.df)):
            arr = []
            for i in range(i - (stddev_rw - 1), i + 1):
                arr.append(self.df.loc[i]["VIX_DEL"])
            self.df.at[i, "VIX_DEL_STDDEV"] = np.std(arr, ddof=1)

        self.dfs = [self.df]


class IndexUSD(DataProcess):
    def __init__(self, data_path):
        super().__init__(data_path=data_path)

    def process(self):
        self.df["USDEUR_50"] = ["_"] * len(self.df)
        self.df["USDJPY_50"] = ["_"] * len(self.df)
        self.df["USD_INDEX"] = ["_"] * len(self.df)  # equal weight usd eur/jpy basket
        # interpreted as usd bull index

        # transform
        factor_USDEUR = 50 / self.df.loc[0]["USDEUR_MID"]
        factor_USDJPY = 50 / self.df.loc[0]["USDJPY_MID"]
        self.df.at[0, "USDEUR_50"] = 50
        self.df.at[0, "USDJPY_50"] = 50
        self.df.at[0, "USD_INDEX"] = 100

        for i in range(1, len(self.df)):
            self.df.at[i, "USDEUR_50"] = self.df.loc[i]["USDEUR_MID"] * factor_USDEUR
            self.df.at[i, "USDJPY_50"] = self.df.loc[i]["USDJPY_MID"] * factor_USDJPY
            self.df.at[i, "USD_INDEX"] = self.df.loc[i]["USDEUR_50"] + self.df.loc[i]["USDJPY_50"]

        self.dfs = [self.df]


class ProcessUSD(DataProcess):
    def __init__(self, data_path):
        super().__init__(data_path=data_path)

    def process(self, rw=5):
        self.df["USD_EMA" + str(rw)] = ["_"] * len(self.df)
        self.df["USD_PCTDEL"] = ["_"] * len(self.df)

        EMA_func(df=self.df, rolling_window=rw, init_index=rw - 1, input="USD_INDEX", output="USD_EMA5")

        # derive percent change
        for i in range(rw, len(self.df)):
            self.df.at[i, "USD_PCTDEL"] = pctDel(self.df.loc[i]["USD_INDEX"], self.df.loc[i - 1]["USD_INDEX"])

        self.dfs = [self.df]


class ProcessCDS1(DataProcess):
    def __init__(self, data_path):
        super().__init__(data_path=data_path)

    def process(self):
        for i in range(1, 39):
            self.df["CDX" + str(i) + "_DEL"] = ["_"] * len(self.df)

            # del: bps change in spread

            for j in range(1, len(self.df)):
                if self.df.loc[j]["CDX" + str(i)] != 0 and self.df.loc[j - 1]["CDX" + str(i)] != 0:
                    self.df.at[j, "CDX" + str(i) + "_DEL"] = self.df.loc[j]["CDX" + str(i)] - self.df.loc[j - 1][
                        "CDX" + str(i)]

        self.dfs = [self.df]


class ProcessCDS2(DataProcess):
    def __init__(self, data_path):
        super().__init__(data_path=data_path)

    def process(self):
        # TODO need to check if this is correct, it seems to be deleting a lot of rows
        for i in range(0, len(self.df)):
            drop = True
            for j in range(1, 39):
                if self.df.loc[i]["CDX" + str(j) + "_DEL"] == "_" or self.df.loc[i]["CDX" + str(j) + "_DEL"] == 0:
                    continue
                else:
                    drop = False
                    break

            if drop:
                self.df.drop(index=i, inplace=True)

        self.df.reset_index(inplace=True)

        self.dfs = [self.df]


class Week52(DataProcess):
    def __init__(self, data_path, data_path1):
        super().__init__(data_path=data_path, data_path1=data_path1)

    def process(self, ETFS=("")):
        for i in range(len(ETFS)):
            self.df[ETFS[i] + "_%_to_52wH"] = ["_"] * len(self.df)
            self.df[ETFS[i] + "_%_from_52wL"] = ["_"] * len(self.df)

            for j in range(1, len(self.df)):
                if self.df.loc[j][ETFS[i] + "_52wH"] != 0 and self.df1.loc[j][ETFS[i] + "_CLOSE"] != 0 and \
                        self.df.loc[j][ETFS[i] + "_52wL"] != 0:
                    self.df.at[j, ETFS[i] + "_%_to_52wH"] = pctDel(self.df.loc[j][ETFS[i] + "_52wH"],
                                                                   self.df1.loc[j][ETFS[i] + "_CLOSE"])
                    self.df.at[j, ETFS[i] + "_%_from_52wL"] = pctDel(self.df1.loc[j][ETFS[i] + "_CLOSE"],
                                                                     self.df.loc[j][ETFS[i] + "_52wL"])

            self.dfs = [self.df]


class MomentsFirstSecond(DataProcess):
    def __init__(self, data_path):
        super().__init__(data_path=data_path)

    def process(self, ETFS=(""), rw=21):
        for i in range(len(ETFS)):
            self.df[ETFS[i] + "_MEAN"] = ["_"] * len(self.df)
            self.df[ETFS[i] + "_STDDEV"] = ["_"] * len(self.df)

            for j in range(rw, len(self.df)):
                print(i, j)
                arr = []
                for k in range(j - (rw - 1), j + 1):
                    if self.df.loc[k][ETFS[i] + "_LNRETURN"] == "_" or self.df.loc[k][ETFS[i] + "_LNRETURN"] == 0:
                        continue
                    else:
                        arr.append(self.df.loc[k][ETFS[i] + "_LNRETURN"])
                self.df.at[j, ETFS[i] + "_MEAN"] = np.mean(arr)
                self.df.at[j, ETFS[i] + "_STDDEV"] = np.std(arr, ddof=1)

        self.dfs = [self.df]


class MomentsThirdFourth(DataProcess):
    def __init__(self, data_path):
        super().__init__(data_path=data_path)

    def process(self, ETFS=(""), rw=21):
        for i in range(len(ETFS)):
            self.df[ETFS[i] + "_SKEW"] = ["_"] * len(self.df)
            self.df[ETFS[i] + "_KURTOSIS"] = ["_"] * len(self.df)

            break_outer_loop = False
            for j in range(rw, len(self.df)):
                print(i, j)
                arr = []
                for k in range(j - (rw - 1), j + 1):
                    if self.df.loc[k][ETFS[i] + "_LNRETURN"] == "_" or self.df.loc[k][ETFS[i] + "_LNRETURN"] == 0:
                        continue
                    else:
                        arr.append(self.df.loc[k][ETFS[i] + "_LNRETURN"])
                self.df.at[j, ETFS[i] + "_SKEW"] = stats.skew(arr)
                self.df.at[j, ETFS[i] + "_KURTOSIS"] = stats.kurtosis(arr)

        self.dfs = [self.df]


class DelStdDevCDS(DataProcess):
    def __init__(self, data_path, rw=10):
        super().__init__(data_path=data_path)

    def process(self, rw=10):
        for i in range(1, 39):
            self.df["CDX" + str(i) + "_DEL_STDDEV"] = ["_"] * len(self.df)

            for j in range(10, len(self.df)):
                print(i, j)
                arr = []
                for k in range(j - (rw - 1), j + 1):
                    if self.df.loc[k]["CDX" + str(i) + "_DEL"] == "_" or self.df.loc[k]["CDX" + str(i) + "_DEL"] == 0:
                        continue
                    else:
                        arr.append(self.df.loc[k]["CDX" + str(i) + "_DEL"])
                self.df.at[j, "CDX" + str(i) + "_DEL_STDDEV"] = np.std(arr, ddof=1)

        self.dfs = [self.df]


class ProcessCDS3(DataProcess):
    def __init__(self, data_path):
        super().__init__(data_path=data_path)

    def process(self, last_index=85):
        for i in range(last_index + 1):
            self.df.drop(index=i, inplace=True)

        self.df.reset_index(inplace=True)

        self.dfs = [self.df]


class ProcessCDS4(DataProcess):
    def __init__(self, data_path):
        super().__init__(data_path=data_path)

    def process(self, last_index=4):
        for i in range(1, last_index - 1):
            self.df.drop("CDX" + str(i) + "_DEL_STDDEV", inplace=True, axis=1)

        self.dfs = [self.df]


class ProcessCDS5(DataProcess):
    def __init__(self, data_path):
        super().__init__(data_path=data_path)

    def process(self, first_index=5):
        self.df["CDX_INDEX"] = ["_"] * len(self.df)

        for i in range(len(self.df)):
            arr = []
            for j in range(first_index, 39):
                if self.df.loc[i]["CDX" + str(j) + "_DEL_STDDEV"] > 0:
                    arr.append(self.df.loc[i]["CDX" + str(j) + "_DEL_STDDEV"])

            self.df.at[i, "CDX_INDEX"] = np.median(arr)

        self.dfs = [self.df]

class customerAccount(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        self.df = self.df[["cus_no", "act_no"]]

        memory = {}

        for i in range(len(self.df)):
            if self.df.loc[i]["cus_no"] not in memory:
                memory[self.df.loc[i]["cus_no"]] = [self.df.loc[i]["act_no"]]
            elif self.df.loc[i]["cus_no"] in memory:
                if self.df.loc[i]["act_no"] not in memory[self.df.loc[i]["cus_no"]]:
                    memory[self.df.loc[i]["cus_no"]].append(self.df.loc[i])

        self.df1 = pd.DataFrame()
        self.df1["Customer"] = ["_"] * len(memory)
        self.df1["Account Number"] = ["_"] * len(memory)

        j = 0
        for key, value in memory.items():
            self.df1.at[j, "Customer"] = key
            self.df1.at[j, "Account Number"] = len(value)
            j += 1

        for i in range(len(self.df1)):
            if self.df1.loc[i]["Account Number"] != 1:
                print("Not 1 Found")

        self.dfs = [self.df1]

# previous code, very bad, ignore
class chronological(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        current_acc = ""
        chronological_list = []
        chronological_index_list = []
        self.df1 = pd.DataFrame()

        k = 0

        for i in range(50):
            print(i)
            current_acc = self.df.loc[i]["act_no"]
            chronological_list.append(self.df.loc[i]["bse_ym"])
            chronological_index_list.append(i)

            if self.df.loc[i]["act_no"] == current_acc:
                for j in range(len(chronological_index_list)):
                    if self.df.loc[j]["bse_ym"] < chronological_list[j]:
                        chronological_list.insert(j, self.df.loc[i]["bse_ym"])
                        chronological_index_list.insert(j, i)
                    elif self.df.loc[j]["bse_ym"] > chronological_list[-1]:
                        chronological_list.append(self.df.loc[j]["bse_ym"])
                        chronological_index_list.append(i)
            elif self.df.loc[i]["act_no"] != current_acc:
                for j in chronological_index_list:
                    for column in self.df.columns:
                        self.df1.at[k, column] = self.df.loc[j][column]
                    k += 1

                current_acc = self.df.loc[i]["act_no"]
                chronological_list = [self.df.loc[i]["bse_ym"]]
                chronological_index_list = [i]

        self.dfs = [self.df1]

# new code, efficient, good
class chronological2(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self, sort_by="bse_ym"):
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        self.df_output = pd.DataFrame()
        current_acc = ""
        for i in range(self.df_len):
            print(i)
            if current_acc == "":
                current_acc = self.df.loc[i]["act_no"]
                indicies = [0]
            elif current_acc == self.df.loc[i]["act_no"]:
                indicies.append(i)
            elif current_acc != self.df.loc[i]["act_no"]:

                self.df1 = pd.DataFrame()
                self.df1 = self.df.iloc[indicies, :]
                self.df1 = self.df1.sort_values(by=sort_by, ascending=True)
                self.df_output = self.df_output.append(self.df1, ignore_index=True)

                current_acc = self.df.loc[i]["act_no"]
                indicies = [i]

            if i == self.df_len-1:
                self.df1 = pd.DataFrame()
                self.df1 = self.df.iloc[indicies, :]
                self.df1 = self.df1.sort_values(by=sort_by, ascending=True)
                self.df_output = self.df_output.append(self.df1, ignore_index=True)

        self.dfs = [self.df_output]

class yesNo(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self, columns=[]):
        for column in columns:
            for i in range(self.df_len):
                print(i)
                if self.df.loc[i][column] == "Y":
                    self.df.at[i, column] = 1
                elif self.df.loc[i][column] == "N":
                    self.df.at[i, column] = 0

        self.dfs = [self.df]