import pandas
import pandas as pd
import numpy as np
from numpy import nan
from scipy import stats
from data_process_global import *

pd.set_option("display.max_columns", None)


class DataProcess(object):
    def __init__(self, data_path, excel_or_csv="", data_path1="", data_path2="", data_path3="", data_path4="",
                 data_path5="", data_path6="", data_path7="", data_path8="", data_path9=""):

        if excel_or_csv == "csv":
            self.df = pd.read_csv(data_path, sep=',', encoding='unicode_escape')
            self.df_list = [self.df]
            if data_path1 != "":
                self.df1 = pd.read_csv(data_path1, sep=',', encoding='unicode_escape')
                self.df_list.append(self.df1)
            if data_path2 != "":
                self.df2 = pd.read_csv(data_path2, sep=',', encoding='unicode_escape')
                self.df_list.append(self.df2)
            if data_path3 != "":
                self.df3 = pd.read_csv(data_path3, sep=',', encoding='unicode_escape')
                self.df_list.append(self.df3)
            if data_path4 != "":
                self.df4 = pd.read_csv(data_path4, sep=',', encoding='unicode_escape')
                self.df_list.append(self.df4)
            if data_path5 != "":
                self.df5 = pd.read_csv(data_path5, sep=',', encoding='unicode_escape')
                self.df_list.append(self.df5)
            if data_path6 != "":
                self.df6 = pd.read_csv(data_path6, sep=',', encoding='unicode_escape')
                self.df_list.append(self.df6)
            if data_path7 != "":
                self.df7 = pd.read_csv(data_path7, sep=',', encoding='unicode_escape')
                self.df_list.append(self.df7)
            if data_path8 != "":
                self.df8 = pd.read_csv(data_path8, sep=',', encoding='unicode_escape')
                self.df_list.append(self.df8)
            if data_path9 != "":
                self.df9 = pd.read_csv(data_path9, sep=',', encoding='unicode_escape')
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
            if "Unnamed" in column:
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
            if self.df.loc[i]["bas_stk_trd_tp_cd"] == 99 or self.df.loc[i]["bas_stk_trd_tp_cd"] == "_":
                self.df.at[i, "bas_stk_trd_tp_cd"] = "NA"
            elif int(self.df.loc[i]["bas_stk_trd_tp_cd"]) in dictionary:
                self.df.at[i, "bas_stk_trd_tp_cd"] = dictionary[self.df.loc[i]["bas_stk_trd_tp_cd"]]
            else:
                self.df.at[i, "bas_stk_trd_tp_cd"] = "NA"

        self.dfs = [self.df]
