import pandas as pd
import numpy as np
from numpy import nan
from scipy import stats
from data_process_global import *
from datetime import date, datetime
import investpy
import threading
import time
import multiprocessing
from pandas_datareader import data as pdr
from sklearn.preprocessing import MinMaxScaler
from pandas_profiling import ProfileReport

pd.set_option("display.max_columns", None)
pd.set_option('display.max_rows', None)

# for 예선

# class DataProcess(object):
#     def __init__(self, data_path, excel_or_csv="", data_path1="", data_path2="", data_path3="", data_path4="",
#                  data_path5="", data_path6="", data_path7="", data_path8="", data_path9=""):
#
#         if excel_or_csv == "csv":
#             self.df = pd.read_csv(data_path, sep=',', encoding='unicode_escape')
#             self.df_list = [self.df]
#             if data_path1 != "":
#                 self.df1 = pd.read_csv(data_path1, sep=',', encoding='unicode_escape')
#                 self.df_list.append(self.df1)
#             if data_path2 != "":
#                 self.df2 = pd.read_csv(data_path2, sep=',', encoding='unicode_escape')
#                 self.df_list.append(self.df2)
#             if data_path3 != "":
#                 self.df3 = pd.read_csv(data_path3, sep=',', encoding='unicode_escape')
#                 self.df_list.append(self.df3)
#             if data_path4 != "":
#                 self.df4 = pd.read_csv(data_path4, sep=',', encoding='unicode_escape')
#                 self.df_list.append(self.df4)
#             if data_path5 != "":
#                 self.df5 = pd.read_csv(data_path5, sep=',', encoding='unicode_escape')
#                 self.df_list.append(self.df5)
#             if data_path6 != "":
#                 self.df6 = pd.read_csv(data_path6, sep=',', encoding='unicode_escape')
#                 self.df_list.append(self.df6)
#             if data_path7 != "":
#                 self.df7 = pd.read_csv(data_path7, sep=',', encoding='unicode_escape')
#                 self.df_list.append(self.df7)
#             if data_path8 != "":
#                 self.df8 = pd.read_csv(data_path8, sep=',', encoding='unicode_escape')
#                 self.df_list.append(self.df8)
#             if data_path9 != "":
#                 self.df9 = pd.read_csv(data_path9, sep=',', encoding='unicode_escape')
#                 self.df_list.append(self.df9)
#         else:
#             self.df = pd.read_excel(data_path)
#             self.df_list = [self.df]
#             if data_path1 != "":
#                 self.df1 = pd.read_excel(data_path1)
#                 self.df_list.append(self.df1)
#             if data_path2 != "":
#                 self.df2 = pd.read_excel(data_path2)
#                 self.df_list.append(self.df2)
#             if data_path3 != "":
#                 self.df3 = pd.read_excel(data_path3)
#                 self.df_list.append(self.df3)
#             if data_path4 != "":
#                 self.df4 = pd.read_excel(data_path4)
#                 self.df_list.append(self.df4)
#             if data_path5 != "":
#                 self.df5 = pd.read_excel(data_path5)
#                 self.df_list.append(self.df5)
#             if data_path6 != "":
#                 self.df6 = pd.read_excel(data_path6)
#                 self.df_list.append(self.df6)
#             if data_path7 != "":
#                 self.df7 = pd.read_excel(data_path7)
#                 self.df_list.append(self.df7)
#             if data_path8 != "":
#                 self.df8 = pd.read_excel(data_path8)
#                 self.df_list.append(self.df8)
#             if data_path9 != "":
#                 self.df9 = pd.read_excel(data_path9)
#                 self.df_list.append(self.df9)
#
#         self.df_len = len(self.df)
#
#     # dfs: data frames
#     # dps: data paths
#     def export(self, dps, excel_or_csv=""):
#         if len(dps) == len(self.dfs):
#
#             if excel_or_csv == "csv":
#                 for i in range(len(self.dfs)):
#                     self.dfs[i].to_csv(dps[i])
#                 print("Exported To:", dps)
#
#             else:
#                 for i in range(len(self.dfs)):
#                     self.dfs[i].to_excel(dps[i])
#                 print("Exported To:", dps)
#
#         else:
#             print("Incorrect Number of Data Paths")
#             print("Data Paths: ", len(dps))
#             print("Data Frames: ", len(self.dfs))

# for 본선
class DataProcess(object):
    def __init__(self, data_path, excel_or_csv="", data_path1="", data_path2="", data_path3="", data_path4="",
                 data_path5="", data_path6="", data_path7="", data_path8="", data_path9=""):

        if excel_or_csv == "csv":
            self.df = pd.read_csv(data_path, encoding='utf-8', sep=',')
            self.df_list = [self.df]
            if data_path1 != "":
                self.df1 = pd.read_csv(data_path1, encoding='utf-8', sep=',')
                self.df_list.append(self.df1)
            if data_path2 != "":
                self.df2 = pd.read_csv(data_path2, encoding='utf-8', sep=',')
                self.df_list.append(self.df2)
            if data_path3 != "":
                self.df3 = pd.read_csv(data_path3, encoding='utf-8', sep=',')
                self.df_list.append(self.df3)
            if data_path4 != "":
                self.df4 = pd.read_csv(data_path4, encoding='utf-8', sep=',')
                self.df_list.append(self.df4)
            if data_path5 != "":
                self.df5 = pd.read_csv(data_path5, encoding='utf-8', sep=',')
                self.df_list.append(self.df5)
            if data_path6 != "":
                self.df6 = pd.read_csv(data_path6, encoding='utf-8', sep=',')
                self.df_list.append(self.df6)
            if data_path7 != "":
                self.df7 = pd.read_csv(data_path7, encoding='utf-8', sep=',')
                self.df_list.append(self.df7)
            if data_path8 != "":
                self.df8 = pd.read_csv(data_path8, encoding='utf-8', sep=',')
                self.df_list.append(self.df8)
            if data_path9 != "":
                self.df9 = pd.read_csv(data_path9, encoding='utf-8', sep=',')
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

            if i == self.df_len - 1:
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


class uniqueFX(DataProcess):
    def __init__(self, data_path, data_path1, excel_or_csv=""):
        super().__init__(data_path=data_path, data_path1=data_path1, excel_or_csv=excel_or_csv)

    def process(self, column=""):
        unique_fx = []

        for i in range(self.df_len):
            if self.df.loc[i][column] not in unique_fx:
                unique_fx.append(self.df.loc[i][column])

        for i in range(len(self.df1)):
            if self.df1.loc[i][column] not in unique_fx:
                unique_fx.append(self.df1.loc[i][column])

        for fx in unique_fx:
            print(fx)

        self.dfs = [self.df]


class renameCusAcc(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        current_cus = ""
        current_acc = ""
        j = 0
        acc_dict = {}

        for i in range(self.df_len):
            print(i)
            if current_cus == "" and current_acc == "":
                current_cus = self.df.loc[i]["cus_no"]
                current_acc = self.df.loc[i]["act_no"]
                acc_dict[self.df.loc[i]["act_no"]] = "acc_" + str(j)

                self.df.at[i, "cus_no"] = "cus_" + str(j)
                self.df.at[i, "act_no"] = "acc_" + str(j)
            elif current_cus == self.df.loc[i]["cus_no"] and current_acc == self.df.loc[i]["act_no"]:
                self.df.at[i, "cus_no"] = "cus_" + str(j)
                self.df.at[i, "act_no"] = "acc_" + str(j)
            elif current_cus != self.df.loc[i]["cus_no"] and current_acc != self.df.loc[i]["act_no"]:
                current_cus = self.df.loc[i]["cus_no"]
                current_acc = self.df.loc[i]["act_no"]

                j += 1

                acc_dict[self.df.loc[i]["act_no"]] = "acc_" + str(j)

                self.df.at[i, "cus_no"] = "cus_" + str(j)
                self.df.at[i, "act_no"] = "acc_" + str(j)

        self.dfs = [self.df]

        return acc_dict


class renameCusAcc1(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self, acc_dict={}):
        for i in range(self.df_len):
            print(i)
            self.df.at[i, "act_no"] = acc_dict[self.df.loc[i, "act_no"]]

        self.dfs = [self.df]


class renameCusAcc2(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self, acc_dict={}):
        self.df.drop("cus_no", axis=1, inplace=True)

        for i in range(self.df_len):
            print(i)
            self.df.at[i, "act_no"] = acc_dict[self.df.loc[i, "act_no"]]

        self.dfs = [self.df]


class oneHotFX(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        self.df1 = pd.get_dummies(self.df.cur_cd, prefix='FX')
        self.df = pd.concat([self.df, self.df1], axis=1)

        self.df.drop("cur_cd", axis=1, inplace=True)

        self.dfs = [self.df]


class accToNum(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self, drop=""):

        if drop != "":
            self.df = self.df.drop([drop], axis=1)

        for i in range(self.df_len):
            print(i)
            self.df.at[i, "act_no"] = int(self.df.loc[i]["act_no"][4:])

        self.dfs = [self.df]


class sortByAcc(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        self.df = self.df.sort_values(by="act_no", ascending=True, kind="mergesort")  # mergesort is stable

        self.dfs = [self.df]


class dropUnnamed(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):

        for column in self.df:
            if "Unnamed" in column or "index" in column:
                self.df = self.df.drop([column], axis=1)

        self.dfs = [self.df]


class monthlyAccessCount(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        for i in range(self.df_len):
            print(i)
            arr = list(str(self.df.loc[i]["mts_mm_access_type"]))

            sum = 0
            for j in arr:
                sum += int(j)

            self.df.at[i, "mts_mm_access_type"] = sum

        self.dfs = [self.df]


class oneHotSex(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        pd.set_option("display.max_columns", None)
        for i in range(self.df_len):

            if self.df.loc[i]["sex_dit_cd"] == 1:
                self.df.at[i, "sex_dit_cd"] = "M"
            elif self.df.loc[i]["sex_dit_cd"] == 2:
                self.df.at[i, "sex_dit_cd"] = "F"
            elif self.df.loc[i]["sex_dit_cd"] == 99:
                self.df.at[i, "sex_dit_cd"] = "NA"

        self.df1 = pd.get_dummies(self.df.sex_dit_cd, prefix='SEX')
        self.df = pd.concat([self.df, self.df1], axis=1)

        self.df.drop("sex_dit_cd", axis=1, inplace=True)

        self.dfs = [self.df]


class processAge(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        for i in range(self.df_len):
            if self.df.loc[i]["cus_age_stn_cd"] == 99:
                self.df.at[i, "cus_age_stn_cd"] = "NA"

        self.dfs = [self.df]


class regroupSecurity(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        low_risk = [1, 15, 14, 13, 12, 11, 10]
        mid_risk = [9, 8, 7, 6]
        high_risk = [5, 4, 3, 2]
        na = [99]

        for i in range(self.df_len):
            print(i)
            if self.df.loc[i]["mrz_pdt_tp_sgm_cd"] in low_risk:
                self.df.at[i, "mrz_pdt_tp_sgm_cd"] = 1
            elif self.df.loc[i]["mrz_pdt_tp_sgm_cd"] in mid_risk:
                self.df.at[i, "mrz_pdt_tp_sgm_cd"] = 2
            elif self.df.loc[i]["mrz_pdt_tp_sgm_cd"] in high_risk:
                self.df.at[i, "mrz_pdt_tp_sgm_cd"] = 3
            elif self.df.loc[i]["mrz_pdt_tp_sgm_cd"] in na:
                self.df.at[i, "mrz_pdt_tp_sgm_cd"] = "NA"

        self.dfs = [self.df]


class lifestageProcess(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        for i in range(self.df_len):
            if self.df.loc[i]["lsg_sgm_cd"] == 99:
                self.df.at[i, "lsg_sgm_cd"] = "NA"

        self.df1 = pd.get_dummies(self.df.lsg_sgm_cd, prefix='LIFESTAGE')
        self.df = pd.concat([self.df, self.df1], axis=1)

        self.df.drop("lsg_sgm_cd", axis=1, inplace=True)

        self.dfs = [self.df]


class customerLvlProcess(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        dictionary = {1: 7,
                      2: 6,
                      3: 5,
                      4: 4,
                      5: 3,
                      9: 2,
                      99: 1}

        for i in range(self.df_len):
            self.df.at[i, "tco_cus_grd_cd"] = dictionary[self.df.loc[i]["tco_cus_grd_cd"]]

        self.dfs = [self.df]


class totalDurationInvestingProcess(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        for i in range(self.df_len):
            if self.df.loc[i]["tot_ivs_te_sgm_cd"] == 99:
                self.df.at[i, "tot_ivs_te_sgm_cd"] = "NA"

        self.dfs = [self.df]


class holdingsTypeProcessing(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        for i in range(self.df_len):
            if self.df.loc[i]["hld_pdt_tp_sgm_cd"] == 99:
                self.df.at[i, "hld_pdt_tp_sgm_cd"] = "NA"

        self.df1 = pd.get_dummies(self.df.hld_pdt_tp_sgm_cd, prefix='HOLDINGS_TYPE')
        self.df = pd.concat([self.df, self.df1], axis=1)

        self.df.drop("hld_pdt_tp_sgm_cd", axis=1, inplace=True)

        self.dfs = [self.df]


class loyaltyProcess(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):

        dictionary = {1: 6,
                      2: 5,
                      3: 4,
                      4: 3,
                      5: 2,
                      6: 1}

        for i in range(self.df_len):
            print(i)
            if self.df.loc[i]["loy_sgm_cd"] == 99:
                self.df.at[i, "loy_sgm_cd"] = "NA"
            elif self.df.loc[i]["loy_sgm_cd"] in dictionary:
                self.df.at[i, "loy_sgm_cd"] = dictionary[self.df.loc[i]["loy_sgm_cd"]]
            else:
                self.df.at[i, "loy_sgm_cd"] = "NA"

        self.dfs = [self.df]


class mainMarketProcess(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        low_soph = [6]
        mid_soph = [1, 2, 4]
        high_soph = [5]
        vhigh_soph = [3]

        for i in range(self.df_len):
            if self.df.loc[i]["mrz_mkt_dit_cd"] == 99:
                self.df.at[i, "mrz_mkt_dit_cd"] = "NA"
            elif self.df.loc[i]["mrz_mkt_dit_cd"] in low_soph:
                self.df.at[i, "mrz_mkt_dit_cd"] = 1
            elif self.df.loc[i]["mrz_mkt_dit_cd"] in mid_soph:
                self.df.at[i, "mrz_mkt_dit_cd"] = 2
            elif self.df.loc[i]["mrz_mkt_dit_cd"] in high_soph:
                self.df.at[i, "mrz_mkt_dit_cd"] = 3
            elif self.df.loc[i]["mrz_mkt_dit_cd"] in vhigh_soph:
                self.df.at[i, "mrz_mkt_dit_cd"] = 4

        self.dfs = [self.df]


class mainSectorProcess(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):

        for i in range(self.df_len):
            if self.df.loc[i]["mrz_btp_dit_cd"] == 99:
                self.df.at[i, "mrz_btp_dit_cd"] = "NA"

        self.df1 = pd.get_dummies(self.df.mrz_btp_dit_cd, prefix='SECTOR')
        self.df = pd.concat([self.df, self.df1], axis=1)

        self.df.drop("mrz_btp_dit_cd", axis=1, inplace=True)

        # for i in range(self.df_len):
        #     print(i)
        #     for column in self.df:
        #         if self.df.loc[i][column] == np.nan:
        #             self.df.at[i, column] = "_"

        self.dfs = [self.df]


class netWorthProcess(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):

        dictionary = {1: 5,
                      2: 4,
                      3: 3,
                      4: 2,
                      5: 1}

        for i in range(self.df_len):
            if self.df.loc[i]["aet_bse_stk_trd_tp_cd"] == 99 or self.df.loc[i]["aet_bse_stk_trd_tp_cd"] == "_":
                self.df.at[i, "aet_bse_stk_trd_tp_cd"] = "NA"
            elif self.df.loc[i]["aet_bse_stk_trd_tp_cd"] in dictionary:
                self.df.at[i, "aet_bse_stk_trd_tp_cd"] = dictionary[self.df.loc[i]["aet_bse_stk_trd_tp_cd"]]
            else:
                self.df.at[i, "aet_bse_stk_trd_tp_cd"] = "NA"

        self.dfs = [self.df]


class tradeFrequencyProcess(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):

        dictionary = {1: 11,
                      2: 10,
                      3: 9,
                      4: 8,
                      5: 7,
                      6: 6,
                      7: 5,
                      8: 4,
                      9: 3,
                      10: 2,
                      11: 1}

        for i in range(self.df_len):
            if self.df.loc[i]["bas_stk_trd_tp_cd"] == 99:
                self.df.at[i, "bas_stk_trd_tp_cd"] = "NA"
            if can_convert_to_int(self.df.loc[i]["bas_stk_trd_tp_cd"]):
                self.df.at[i, "bas_stk_trd_tp_cd"] = dictionary[int(self.df.loc[i]["bas_stk_trd_tp_cd"])]
            else:
                self.df.at[i, "bas_stk_trd_tp_cd"] = "NA"

        self.dfs = [self.df]

class dropColumn(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self, column_name="Unnamed"):
        self.df = self.df.drop([column_name], axis=1)

        self.dfs = [self.df]

class maxAssetValue(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):

        for i in range(self.df_len):
            print(i)
            arr = []
            for column in ASSET_COLUMNS:
                if can_convert_to_int(self.df.loc[i][column]):
                    arr.append(self.df.loc[i][column])

            self.df.at[i, "MAX_ASSET_VALUE"] = max(arr)

        for column in ASSET_COLUMNS:
            self.df = self.df.drop([column], axis=1)

        self.dfs = [self.df]

class accLifespan(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        today = date.today()

        for i in range(self.df_len):
            year = int(str(self.df.loc[i]["fst_act_opn_dt"])[0:4])
            month = int(str(self.df.loc[i]["fst_act_opn_dt"])[4:6])
            day = int(str(self.df.loc[i]["fst_act_opn_dt"])[6:8])

            dateObject = date(year, month, day)

            self.df.at[i, "fst_act_opn_dt"] = (today - dateObject).days

        self.dfs = [self.df]

class infoToCrossSectMode(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):

        self.df1 = pd.DataFrame()

        for column_name in MODE_COLUMNS:
            current_acc = ""
            k = 0
            memory = []

            for i in range(self.df_len):
                print(column_name, i)

                if current_acc == "":
                    current_acc = self.df.loc[i]["act_no"]
                    memory.append(self.df.loc[i][column_name])
                elif self.df.loc[i]["act_no"] == current_acc:
                    memory.append(self.df.loc[i][column_name])
                elif self.df.loc[i]["act_no"] != current_acc:

                    self.df1.at[k, "act_no"] = current_acc
                    self.df1.at[k, column_name] = most_frequent(memory)

                    current_acc = self.df.loc[i]["act_no"]
                    memory = [self.df.loc[i][column_name]]

                    k += 1

                if i == self.df_len - 1:
                    self.df1.at[k, "act_no"] = current_acc
                    self.df1.at[k, column_name] = most_frequent(memory)

        self.dfs = [self.df1]

class infoToCrossSectMax(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):

        self.df1 = pd.DataFrame()

        for column_name in MAX_COLUMNS:
            current_acc = ""
            k = 0
            memory = []

            for i in range(self.df_len):
                print(column_name, i)

                if current_acc == "":
                    current_acc = self.df.loc[i]["act_no"]
                    memory.append(self.df.loc[i][column_name])
                elif self.df.loc[i]["act_no"] == current_acc:
                    memory.append(self.df.loc[i][column_name])
                elif self.df.loc[i]["act_no"] != current_acc:

                    self.df1.at[k, "act_no"] = current_acc
                    self.df1.at[k, column_name] = max(memory)

                    current_acc = self.df.loc[i]["act_no"]
                    memory = [self.df.loc[i][column_name]]

                    k += 1

                if i == self.df_len - 1:
                    self.df1.at[k, "act_no"] = current_acc
                    self.df1.at[k, column_name] = most_frequent(memory)

        self.dfs = [self.df1]

class concatDataframes(DataProcess):
    def __init__(self, data_path, data_path1, excel_or_csv=""):
        super().__init__(data_path=data_path, data_path1=data_path1, excel_or_csv=excel_or_csv)

    def process(self):
        self.df = pd.concat([self.df, self.df1], axis=1)

        self.dfs = [self.df]

class concatDataframes2(DataProcess):
    def __init__(self, data_path, data_path1, excel_or_csv=""):
        super().__init__(data_path=data_path, data_path1=data_path1, excel_or_csv=excel_or_csv)

    def process(self, column_name=""):
        self.df1 = self.df1[[column_name]]
        self.df = pd.concat([self.df, self.df1], axis=1)

        self.dfs = [self.df]

class concatAll(DataProcess):
    def __init__(self, data_path, data_path1, data_path2, excel_or_csv=""):
        super().__init__(data_path=data_path, data_path1=data_path1, data_path2=data_path2, excel_or_csv=excel_or_csv)

    def process(self, path1_column="", path2_column="", path2_column1=""):
        self.df1 = self.df1[[path1_column]]
        self.df2 = self.df2[[path2_column, path2_column1]]

        self.df = pd.concat([self.df, self.df1, self.df2], axis=1)

        self.dfs = [self.df]

class removeWhiteSpace(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self, column_name=""):
        for i in range(self.df_len):

            self.df.at[i, column_name] = str(self.df.loc[i][column_name]).strip()

        self.dfs = [self.df]


class getTicker(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        for i in range(self.df_len):
            if self.df.loc[i]["vol_3m"] == "_":
                print(i)
                try:
                    df = investpy.stocks.search_stocks(by='isin', value=str(self.df.loc[i]["iem_cd"]))
                    ticker = df.loc[0]['symbol']
                except:
                    ticker = "_"

                self.df.at[i, "new_ticker"] = ticker
            else:
                self.df.at[i, "new_ticker"] = "__"

        self.dfs = [self.df]

class accountDrop(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        for column in DROP_COLUMNS:
            self.df = self.df.drop([column], axis=1)

        self.dfs = [self.df]

class finalVol3M(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        for i in range(self.df_len):
            print(i)
            if isfloat(self.df.loc[i]["vol_3m"]):
                self.df.at[i, "final_vol_3m"] = self.df.loc[i]["vol_3m"]
            elif isfloat(self.df.loc[i]["new_vol_3m"]):
                self.df.at[i, "final_vol_3m"] = self.df.loc[i]["new_vol_3m"]
            else:
                self.df.at[i, "final_vol_3m"] = "_"

        self.dfs = [self.df]

class valueWeightedVolatility(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        self.df1 = pd.DataFrame()
        value_memory = []
        volatility_memory = []

        current_acc = ""
        k = 0

        for i in range(self.df_len):
            print(i)
            if current_acc == "":
                current_acc = self.df.loc[i]["act_no"]
                if can_convert_to_int(self.df.loc[i]["stl_bse_now_eal_amt"]) and isfloat(self.df.loc[i]["final_vol_3m"]):
                    value_memory.append(self.df.loc[i]["stl_bse_now_eal_amt"])
                    volatility_memory.append(self.df.loc[i]["final_vol_3m"])
            elif self.df.loc[i]["act_no"] == current_acc:
                if can_convert_to_int(self.df.loc[i]["stl_bse_now_eal_amt"]) and isfloat(self.df.loc[i]["final_vol_3m"]):
                    value_memory.append(self.df.loc[i]["stl_bse_now_eal_amt"])
                    volatility_memory.append(self.df.loc[i]["final_vol_3m"])
            elif self.df.loc[i]["act_no"] != current_acc:
                self.df1.at[k, "act_no"] = current_acc

                if len(value_memory) > 0 and len(volatility_memory) > 0:
                    weight_list = []
                    sum = np.sum(value_memory)

                    for value in value_memory:
                        weight_list.append(value/sum)

                    value_weighted_volatility = 0
                    for j in range(len(volatility_memory)):
                        value_weighted_volatility += float(volatility_memory[j]) * float(weight_list[j])

                    self.df1.at[k, "value_weighted_volatility"] = value_weighted_volatility
                else:
                    self.df1.at[k, "value_weighted_volatility"] = "_"

                value_memory = []
                volatility_memory = []
                if can_convert_to_int(self.df.loc[i]["stl_bse_now_eal_amt"]) and isfloat(self.df.loc[i]["final_vol_3m"]):
                    value_memory.append(self.df.loc[i]["stl_bse_now_eal_amt"])
                    volatility_memory.append(self.df.loc[i]["final_vol_3m"])

                current_acc = self.df.loc[i]["act_no"]
                k += 1

            if i == self.df_len - 1:
                self.df1.at[k, "act_no"] = current_acc
                if can_convert_to_int(self.df.loc[i]["stl_bse_now_eal_amt"]) and isfloat(self.df.loc[i]["final_vol_3m"]):
                    value_memory.append(self.df.loc[i]["stl_bse_now_eal_amt"])
                    volatility_memory.append(self.df.loc[i]["final_vol_3m"])

                if len(value_memory) > 0 and len(volatility_memory) > 0:
                    weight_list = []
                    sum = np.sum(value_memory)

                    for value in value_memory:
                        weight_list.append(value / sum)

                    value_weighted_volatility = 0
                    for j in range(len(volatility_memory)):
                        value_weighted_volatility += float(volatility_memory[j]) * float(weight_list[j])

                    self.df1.at[k, "value_weighted_volatility"] = value_weighted_volatility
                else:
                    self.df1.at[k, "value_weighted_volatility"] = "_"

        self.dfs = [self.df1]

class aggregateLeverage(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        self.df1 = pd.DataFrame()
        leverage = 0

        current_acc = ""
        k = 0

        for i in range(self.df_len):
            print(i)
            if current_acc == "":
                leverage += float(self.df.loc[i]["lon_amt"])
                current_acc = self.df.loc[i]["act_no"]
            elif self.df.loc[i]["act_no"] == current_acc:
                leverage += float(self.df.loc[i]["lon_amt"])
            elif self.df.loc[i]["act_no"] != current_acc:
                self.df1.at[k, "act_no"] = current_acc
                self.df1.at[k, "leverage"] = leverage

                leverage = 0
                current_acc = self.df.loc[i]["act_no"]
                k += 1

            if i == self.df_len - 1:
                self.df1.at[k, "act_no"] = current_acc
                self.df1.at[k, "leverage"] = leverage

        self.dfs = [self.df1]

class dropMissingData(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        for i in range(self.df_len):
            print(i)
            if self.df.loc[i]["cus_age_stn_cd"] == "_":
                self.df.drop(index=i, axis=0, inplace=True)
                continue
            if self.df.loc[i]["tot_ivs_te_sgm_cd"] == "_":
                self.df.drop(index=i, axis=0, inplace=True)
                continue
            if self.df.loc[i]["value_weighted_volatility"] == "_" or self.df.loc[i]["value_weighted_volatility"] == 0 or self.df.loc[i]["value_weighted_volatility"] == "0":
                self.df.drop(index=i, axis=0, inplace=True)
                continue

        self.df.reset_index(inplace=True)

        self.dfs = [self.df]

class processMissingData(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        for i in range(self.df_len):
            print(i)
            if self.df.loc[i]["loy_sgm_cd"] == "_":
                self.df.at[i, "loy_sgm_cd"] = 1
            if self.df.loc[i]["mrz_pdt_tp_sgm_cd"] == "_":
                self.df.at[i, "mrz_pdt_tp_sgm_cd"] = 1
            if self.df.loc[i]["mrz_mkt_dit_cd"] == "_":
                self.df.at[i, "mrz_mkt_dit_cd"] = 1
            if self.df.loc[i]["aet_bse_stk_trd_tp_cd"] == "_":
                self.df.at[i, "aet_bse_stk_trd_tp_cd"] = 1
            if self.df.loc[i]["bas_stk_trd_tp_cd"] == "_":
                self.df.at[i, "bas_stk_trd_tp_cd"] = 1

        self.dfs = [self.df]

class oneHotAccount(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        self.df1 = pd.get_dummies(self.df.act_no, prefix='ACCOUNT')
        self.df = pd.concat([self.df1, self.df], axis=1)

        self.df.drop("act_no", axis=1, inplace=True)

        self.dfs = [self.df]


class minMaxScale(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):
        scaler = MinMaxScaler()

        columns_list = []
        for column in self.df:
            columns_list.append(column)

        self.df = pd.DataFrame(scaler.fit_transform(self.df), columns=columns_list)

        self.dfs = [self.df]

# Aweful Algorithm
class groupAndOrder(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self, group_by="CUS_NO", order_by="VISIT_DATE"):
        self.df_output = pd.DataFrame()

        unique_cus = []

        while len(unique_cus) <= 10000:
            current_cus = ""
            print(len(unique_cus))
            for i in range(self.df_len):
                if current_cus == "" and self.df.loc[i][group_by] not in unique_cus:
                    unique_cus.append(self.df.loc[i][group_by])
                    current_cus = self.df.loc[i][group_by]

                    self.df_temp = pd.DataFrame()
                    self.df_temp = self.df.iloc[[i], :]
                elif current_cus == self.df.loc[i][group_by]:
                    self.df_temp = self.df_temp.append(self.df.iloc[[i], :], ignore_index=True)

            self.df_temp = self.df_temp.sort_values(by=order_by, ascending=True)
            self.df_output = self.df_output.append(self.df_temp, ignore_index=True)

            print(self.df_temp)

        self.dfs = [self.df_output]

# Version 2
class group(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self, group_by="CUS_NO"):
        self.df_output = pd.DataFrame()

        index_dict = {}

        for i in range(self.df_len):
            print(i)
            if self.df.loc[i][group_by] not in index_dict:
                index_dict[self.df.loc[i][group_by]] = [i]
            else:
                index_dict[self.df.loc[i][group_by]].append(i)

        for arr in index_dict.values():
            print(arr)
            for i in arr:
                self.df_output = self.df_output.append(self.df.iloc[[i], :], ignore_index=True)

        self.dfs = [self.df_output]

class mapCusAcc(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self, unique_column="cus_no"):

        self.df = self.df[["cus_no", "act_no"]]
        current_cus = ""

        for i in range(self.df_len):
            print(i)
            if current_cus == "":
                current_cus = self.df.loc[i][unique_column]
            elif current_cus == self.df.loc[i][unique_column]:
                self.df.drop(index=i, axis=0, inplace=True)
            elif current_cus != self.df.loc[i][unique_column]:
                current_cus = self.df.loc[i][unique_column]

        self.df.reset_index(inplace=True)

        self.dfs = [self.df]

class readData(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):

        self.df = self.df[["SCREENNAME", "EVENTCATEGORY", "EVENTACTION", "EVENTLABEL"]]
        print(self.df)

        self.dfs = [self.df]

class uniqueCus(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):

        self.df = self.df[["CUS_NO"]]
        unique = []

        for i in range(self.df_len):
            print(i)
            if self.df.loc[i]["CUS_NO"] not in unique:
                unique.append(self.df.loc[i]["CUS_NO"])

        print(len(unique))

        self.dfs = [self.df]

class mapGA(DataProcess):
    def __init__(self, data_path, data_path1, excel_or_csv=""):
        super().__init__(data_path=data_path, data_path1=data_path1, excel_or_csv=excel_or_csv)

    def process(self):

        map_dict = {}

        for i in range(len(self.df1)):
            print(i)
            map_dict[self.df1.loc[i]["cus_no"]] = i

        for i in range(self.df_len):
            print(i)
            self.df.at[i, "CUS_NO"] = map_dict[self.df.loc[i]["CUS_NO"]]

        self.dfs = [self.df]

class sumByCus(DataProcess):
    def __init__(self, data_path, data_path1, excel_or_csv=""):
        super().__init__(data_path=data_path, data_path1=data_path1, excel_or_csv=excel_or_csv)

    def process(self, col="DURATION_SUM", col1="VIEW_CNT"):

        self.df1.set_index('act_no', inplace=True)

        cus = ""
        duration_sum = 0
        view_cnt_sum = 0

        for i in range(self.df_len):
            print(i)
            if cus == "":
                cus = self.df.loc[i]["CUS_NO"]
                duration_sum += self.df.loc[i][col]
                view_cnt_sum += self.df.loc[i][col1]
            elif cus == self.df.loc[i]["CUS_NO"]:
                duration_sum += self.df.loc[i][col]
                view_cnt_sum += self.df.loc[i][col1]
            elif cus != self.df.loc[i]["CUS_NO"]:
                self.df1.at[cus, "TOTAL_DURATION"] = duration_sum
                self.df1.at[cus, "TOTAL_VIEW_CNT"] = view_cnt_sum

                cus = self.df.loc[i]["CUS_NO"]
                duration_sum = 0
                view_cnt_sum = 0

                duration_sum += self.df.loc[i][col]
                view_cnt_sum += self.df.loc[i][col1]

        self.dfs = [self.df1]

class totalForeign(DataProcess):
    def __init__(self, data_path, data_path1, excel_or_csv=""):
        super().__init__(data_path=data_path, data_path1=data_path1, excel_or_csv=excel_or_csv)

    def process(self):

        self.df1.set_index('act_no', inplace=True)

        cus = ""
        duration_sum = 0

        for i in range(self.df_len):
            print(i)
            if cus == "":
                cus = self.df.loc[i]["CUS_NO"]
                if "해외" in str(self.df.loc[i]["SCREENNAME"]) or "해외" in str(self.df.loc[i]["EVENTCATEGORY"]) or "해외" in \
                        str(self.df.loc[i]["EVENTACTION"]) or "해외" in str(self.df.loc[i]["EVENTLABEL"]):
                    duration_sum += self.df.loc[i]["DURATION_SUM"]
            elif cus == self.df.loc[i]["CUS_NO"]:
                if "해외" in str(self.df.loc[i]["SCREENNAME"]) or "해외" in str(self.df.loc[i]["EVENTCATEGORY"]) or "해외" in \
                        str(self.df.loc[i]["EVENTACTION"]) or "해외" in str(self.df.loc[i]["EVENTLABEL"]):
                    duration_sum += self.df.loc[i]["DURATION_SUM"]
            elif cus != self.df.loc[i]["CUS_NO"]:
                self.df1.at[cus, "TOTAL_FOREIGN"] = duration_sum

                cus = self.df.loc[i]["CUS_NO"]
                duration_sum = 0

                if "해외" in str(self.df.loc[i]["SCREENNAME"]) or "해외" in str(self.df.loc[i]["EVENTCATEGORY"]) or "해외" in \
                        str(self.df.loc[i]["EVENTACTION"]) or "해외" in str(self.df.loc[i]["EVENTLABEL"]):
                    duration_sum += self.df.loc[i]["DURATION_SUM"]

        self.dfs = [self.df1]

class totalAdv(DataProcess):
    def __init__(self, data_path, data_path1, excel_or_csv=""):
        super().__init__(data_path=data_path, data_path1=data_path1, excel_or_csv=excel_or_csv)

    def process(self):

        self.df1.set_index('act_no', inplace=True)

        mat_keywords = ("ETN", "공매도", "CFD", "코넥스", "K-OTC", "ELW", "선물", "옵션")

        cus = ""
        duration_sum = 0

        for i in range(self.df_len):
            print("Adv", i)
            if cus == "":
                cus = self.df.loc[i]["CUS_NO"]
                for keyword in mat_keywords:
                    if keyword in str(self.df.loc[i]["SCREENNAME"]) or keyword in str(
                            self.df.loc[i]["EVENTCATEGORY"]) or keyword in \
                            str(self.df.loc[i]["EVENTACTION"]) or keyword in str(self.df.loc[i]["EVENTLABEL"]):
                        duration_sum += self.df.loc[i]["DURATION_SUM"]
                        break
            elif cus == self.df.loc[i]["CUS_NO"]:
                for keyword in mat_keywords:
                    if keyword in str(self.df.loc[i]["SCREENNAME"]) or keyword in str(
                            self.df.loc[i]["EVENTCATEGORY"]) or keyword in \
                            str(self.df.loc[i]["EVENTACTION"]) or keyword in str(self.df.loc[i]["EVENTLABEL"]):
                        duration_sum += self.df.loc[i]["DURATION_SUM"]
                        break
            elif cus != self.df.loc[i]["CUS_NO"]:
                self.df1.at[cus, "TOTAL_ADV"] = duration_sum

                cus = self.df.loc[i]["CUS_NO"]
                duration_sum = 0

                for keyword in mat_keywords:
                    if keyword in str(self.df.loc[i]["SCREENNAME"]) or keyword in str(
                            self.df.loc[i]["EVENTCATEGORY"]) or keyword in \
                            str(self.df.loc[i]["EVENTACTION"]) or keyword in str(self.df.loc[i]["EVENTLABEL"]):
                        duration_sum += self.df.loc[i]["DURATION_SUM"]
                        break

        self.dfs = [self.df1]

class totalAI(DataProcess):
    def __init__(self, data_path, data_path1, excel_or_csv=""):
        super().__init__(data_path=data_path, data_path1=data_path1, excel_or_csv=excel_or_csv)

    def process(self):

        self.df1.set_index('act_no', inplace=True)

        mat_keywords = ("AI PICK3", "AI분석보기", "알고리즘", "로보어카운트", "로보랩")

        cus = ""
        duration_sum = 0

        for i in range(self.df_len):
            print("AI", i)
            if cus == "":
                cus = self.df.loc[i]["CUS_NO"]
                for keyword in mat_keywords:
                    if keyword in str(self.df.loc[i]["SCREENNAME"]) or keyword in str(
                            self.df.loc[i]["EVENTCATEGORY"]) or keyword in \
                            str(self.df.loc[i]["EVENTACTION"]) or keyword in str(self.df.loc[i]["EVENTLABEL"]):
                        duration_sum += self.df.loc[i]["DURATION_SUM"]
                        break
            elif cus == self.df.loc[i]["CUS_NO"]:
                for keyword in mat_keywords:
                    if keyword in str(self.df.loc[i]["SCREENNAME"]) or keyword in str(
                            self.df.loc[i]["EVENTCATEGORY"]) or keyword in \
                            str(self.df.loc[i]["EVENTACTION"]) or keyword in str(self.df.loc[i]["EVENTLABEL"]):
                        duration_sum += self.df.loc[i]["DURATION_SUM"]
                        break
            elif cus != self.df.loc[i]["CUS_NO"]:
                self.df1.at[cus, "TOTAL_AI"] = duration_sum

                cus = self.df.loc[i]["CUS_NO"]
                duration_sum = 0

                for keyword in mat_keywords:
                    if keyword in str(self.df.loc[i]["SCREENNAME"]) or keyword in str(
                            self.df.loc[i]["EVENTCATEGORY"]) or keyword in \
                            str(self.df.loc[i]["EVENTACTION"]) or keyword in str(self.df.loc[i]["EVENTLABEL"]):
                        duration_sum += self.df.loc[i]["DURATION_SUM"]
                        break

        self.dfs = [self.df1]

class combine(DataProcess):
    def __init__(self, data_path, data_path1, data_path2, data_path3, excel_or_csv=""):
        super().__init__(data_path=data_path, data_path1=data_path1, data_path2=data_path2, data_path3=data_path3, excel_or_csv=excel_or_csv)

    def process(self):

        self.df = pd.concat([self.df, self.df1[["TOTAL_AI"]]], axis=1)
        self.df = pd.concat([self.df, self.df2[["TOTAL_NTP"]]], axis=1)
        self.df = pd.concat([self.df, self.df3[["TOTAL_MAT"]]], axis=1)

        self.dfs = [self.df]

class totalNonTrading(DataProcess):
    def __init__(self, data_path, data_path1, excel_or_csv=""):
        super().__init__(data_path=data_path, data_path1=data_path1, excel_or_csv=excel_or_csv)

    def process(self):

        self.df1.set_index('act_no', inplace=True)

        mat_keywords = ("펀드", "ELS", "DLS", "CMA", "MMW", "RP", "포트폴리오", "퇴직", "연금", "IRP", "ISA")

        cus = ""
        duration_sum = 0

        for i in range(self.df_len):
            print("NTP", i)
            if cus == "":
                cus = self.df.loc[i]["CUS_NO"]
                for keyword in mat_keywords:
                    if keyword in str(self.df.loc[i]["SCREENNAME"]) or keyword in str(
                            self.df.loc[i]["EVENTCATEGORY"]) or keyword in \
                            str(self.df.loc[i]["EVENTACTION"]) or keyword in str(self.df.loc[i]["EVENTLABEL"]):
                        duration_sum += self.df.loc[i]["DURATION_SUM"]
                        break
            elif cus == self.df.loc[i]["CUS_NO"]:
                for keyword in mat_keywords:
                    if keyword in str(self.df.loc[i]["SCREENNAME"]) or keyword in str(
                            self.df.loc[i]["EVENTCATEGORY"]) or keyword in \
                            str(self.df.loc[i]["EVENTACTION"]) or keyword in str(self.df.loc[i]["EVENTLABEL"]):
                        duration_sum += self.df.loc[i]["DURATION_SUM"]
                        break
            elif cus != self.df.loc[i]["CUS_NO"]:
                self.df1.at[cus, "TOTAL_NTP"] = duration_sum

                cus = self.df.loc[i]["CUS_NO"]
                duration_sum = 0

                for keyword in mat_keywords:
                    if keyword in str(self.df.loc[i]["SCREENNAME"]) or keyword in str(
                            self.df.loc[i]["EVENTCATEGORY"]) or keyword in \
                            str(self.df.loc[i]["EVENTACTION"]) or keyword in str(self.df.loc[i]["EVENTLABEL"]):
                        duration_sum += self.df.loc[i]["DURATION_SUM"]
                        break

        self.dfs = [self.df1]

class totalMaterial(DataProcess):
    def __init__(self, data_path, data_path1, excel_or_csv=""):
        super().__init__(data_path=data_path, data_path1=data_path1, excel_or_csv=excel_or_csv)

    def process(self):

        self.df1.set_index('act_no', inplace=True)

        mat_keywords = ("지수/선물", "매매동향", "예상지수", "업종지수",
                        "투자컨텐츠", "시황안내", "Dart전자공시", "투자캘린더",
                        "맞춤형투자정보", "리포트", "브리프", "투자전략",
                        "기업분석", "사업분석", "FICC", "자산과리솔루션", "뉴스")

        cus = ""
        duration_sum = 0

        for i in range(self.df_len):
            print("MAT", i)
            if cus == "":
                cus = self.df.loc[i]["CUS_NO"]
                for keyword in mat_keywords:
                    if keyword in str(self.df.loc[i]["SCREENNAME"]) or keyword in str(
                            self.df.loc[i]["EVENTCATEGORY"]) or keyword in \
                            str(self.df.loc[i]["EVENTACTION"]) or keyword in str(self.df.loc[i]["EVENTLABEL"]):
                        duration_sum += self.df.loc[i]["DURATION_SUM"]
                        break
            elif cus == self.df.loc[i]["CUS_NO"]:
                for keyword in mat_keywords:
                    if keyword in str(self.df.loc[i]["SCREENNAME"]) or keyword in str(
                            self.df.loc[i]["EVENTCATEGORY"]) or keyword in \
                            str(self.df.loc[i]["EVENTACTION"]) or keyword in str(self.df.loc[i]["EVENTLABEL"]):
                        duration_sum += self.df.loc[i]["DURATION_SUM"]
                        break
            elif cus != self.df.loc[i]["CUS_NO"]:
                self.df1.at[cus, "TOTAL_MAT"] = duration_sum

                cus = self.df.loc[i]["CUS_NO"]
                duration_sum = 0

                for keyword in mat_keywords:
                    if keyword in str(self.df.loc[i]["SCREENNAME"]) or keyword in str(
                            self.df.loc[i]["EVENTCATEGORY"]) or keyword in \
                            str(self.df.loc[i]["EVENTACTION"]) or keyword in str(self.df.loc[i]["EVENTLABEL"]):
                        duration_sum += self.df.loc[i]["DURATION_SUM"]
                        break

        self.dfs = [self.df1]


class outlierAndDrop(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self):

        for i in range(self.df_len):
            if self.df.loc[i]["access_count"] == "_" or self.df.loc[i]["TOTAL_DURATION"] == "_" or self.df.loc[i]["act_no"] == 9731:
                self.df.drop(index=i, axis=0, inplace=True)

        self.df.reset_index(inplace=True)

        self.dfs = [self.df]

class unMappedCluster(DataProcess):
    def __init__(self, data_path, data_path1, excel_or_csv=""):
        super().__init__(data_path=data_path, data_path1=data_path1, excel_or_csv=excel_or_csv)

    def process(self, TOP9_FEATURES=()):
        self.df_output = pd.DataFrame()

        self.df = self.df[["act_no",
                           "TOTAL_VIEW_CNT",
                           "value_weighted_volatility",
                           "peak_asset_value",
                           "TOTAL_DURATION",
                           "account_age",
                           "TOTAL_FOREIGN",
                           "TOTAL_MAT",
                           "trading_frequency",
                           "age_group"]]

        self.df1 = self.df1[["act_no",
                             "TOTAL_VIEW_CNT",
                             "value_weighted_volatility",
                             "peak_asset_value",
                             "TOTAL_DURATION",
                             "account_age",
                             "TOTAL_FOREIGN",
                             "TOTAL_MAT",
                             "trading_frequency",
                             "age_group"]]

        # map_dict = {}
        #
        # for i in range(self.df_len):
        #     map_dict[i] = self.df.loc[i]["act_no"]
        #
        # self.df.set_index('act_no', inplace=True)
        for i in range(len(self.df1)):
            print(i)
            for feature in TOP9_FEATURES:
                acc_no = int(self.df1.loc[i]["act_no"])
                self.df_output.at[i, feature] = self.df.loc[acc_no][feature]

        self.dfs = [self.df_output]