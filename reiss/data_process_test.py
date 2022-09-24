for i in range(self.df_len):
    if self.df.loc[i]["bas_stk_trd_tp_cd"] == 99 or self.df.loc[i]["bas_stk_trd_tp_cd"] == "_":
        self.df.at[i, "bas_stk_trd_tp_cd"] = "NA"
    elif self.df.loc[i]["bas_stk_trd_tp_cd"] in dict:
        self.df.at[i, "bas_stk_trd_tp_cd"] = dict[self.df.loc[i]["bas_stk_trd_tp_cd"]]
    else:
        self.df.at[i, "bas_stk_trd_tp_cd"] = "NA"