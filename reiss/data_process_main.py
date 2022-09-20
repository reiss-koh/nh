from data_process_global import *
from data_process_class import *

# Check Number of Accounts per Customer
# process = customerAccount(data_path="cus_info.xlsx")
# process.process()
# process.export(["cus_acc.csv"], excel_or_csv="csv")

# Reorder Data in Chronological Order for each Account
# for file_name in RAW_DATA:
#     process1 = chronological2(data_path=file_name + ".xlsx")
#     process1.process(sort_by="bse_ym")
#     process1.export([file_name + "_R1.csv"], excel_or_csv="csv")

# for file_name in RAW_DATA1:
#     process1 = chronological2(data_path=file_name + ".xlsx")
#     process1.process(sort_by="orr_dt")
#     process1.export([file_name + "_R1.csv"], excel_or_csv="csv")

# Y/N to 1/0
# process2 = yesNo(data_path="cus_info_R1" + ".csv", excel_or_csv="csv")
# process2.process(columns=["stk_pdt_hld_yn", "ose_stk_pdt_hld_yn"])
# process2.export(["cus_info" + "_R2.csv"], excel_or_csv="csv")

# Check Number of Unique Currencies in Data
# process3 = uniqueFX(data_path="os_equity_R1.csv", data_path1="cus_account_R1.csv", excel_or_csv="csv")
# process3.process(column="cur_cd")
# Added Dictionary in data_process_global.py

# Rename Customers and Accounts
process4 = renameCusAcc(data_path="cus_info_R2.csv", excel_or_csv="csv")
acc_dict = process4.process()
process4.export(["cus_info_R3.csv"], excel_or_csv="csv")

# Rename Accounts and Drop Customers since each account observation maps to a unique customer observation
for file_name in DATA_PATH:
    process5 = renameCusAcc1(data_path=file_name + "_R1.csv", excel_or_csv="csv")
    process5.process(acc_dict=acc_dict)
    process5.export([file_name + "_R2.csv"], excel_or_csv="csv")

process6 = renameCusAcc2(data_path="cus_assets.xlsx")
process6.process(acc_dict=acc_dict)
process6.export(["cus_assets_R1.csv"], excel_or_csv="csv")