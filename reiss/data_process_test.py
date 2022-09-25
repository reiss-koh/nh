class aggregateLeverage(DataProcess):
    def __init__(self, data_path, data_path1, excel_or_csv=""):
        super().__init__(data_path=data_path, data_path1=data_path1, excel_or_csv=excel_or_csv)

    def process(self):
        self.df1 = pd.DataFrame()
        leverage = 0

        current_acc = ""
        k = 0

        for i in range(self.df_len):
            print(i)
            if current_acc == "":
                leverage += float(self.df.loc[i]["lon_amt"])
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