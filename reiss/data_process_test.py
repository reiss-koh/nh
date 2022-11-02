class groupBy(DataProcess):
    def __init__(self, data_path, excel_or_csv=""):
        super().__init__(data_path=data_path, excel_or_csv=excel_or_csv)

    def process(self, group_by="CUS_NO"):
        self.df_output = pd.DataFrame()

        cus_no = []
        current_cus = ""
        for i in range(self.df_len):
            print(i)
            if current_cus == "":
                current_cus = self.df.loc[i][group_by]
                indicies = [0]
            elif current_cus == self.df.loc[i][group_by]:
                indicies.append(i)
            elif current_cus != self.df.loc[i][group_by]:

                self.df1 = pd.DataFrame()
                self.df1 = self.df.iloc[indicies, :]
                self.df1 = self.df1.sort_values(by=sort_by, ascending=True)
                self.df_output = self.df_output.append(self.df1, ignore_index=True)

                current_cus = self.df.loc[i][group_by]
                indicies = [i]

            if i == self.df_len - 1:
                self.df1 = pd.DataFrame()
                self.df1 = self.df.iloc[indicies, :]
                self.df1 = self.df1.sort_values(by=sort_by, ascending=True)
                self.df_output = self.df_output.append(self.df1, ignore_index=True)

        self.dfs = [self.df_output]