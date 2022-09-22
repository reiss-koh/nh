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
# process4 = renameCusAcc(data_path="cus_info_R2.csv", excel_or_csv="csv")
# acc_dict = process4.process()
# process4.export(["cus_info_R3.csv"], excel_or_csv="csv")

# Rename Accounts and Drop Customers since each account observation maps to a unique customer observation
# for file_name in DATA_PATH:
#     process5 = renameCusAcc1(data_path=file_name + "_R1.csv", excel_or_csv="csv")
#     process5.process(acc_dict=acc_dict)
#     process5.export([file_name + "_R2.csv"], excel_or_csv="csv")
#
# process6 = renameCusAcc2(data_path="cus_assets.xlsx")
# process6.process(acc_dict=acc_dict)
# process6.export(["cus_assets_R1.csv"], excel_or_csv="csv")

# One Hot Encode FX
# for file_name in DATA_PATH1:
#     process7 = oneHotFX(data_path=file_name + "_R2.csv", excel_or_csv="csv")
#     process7.process()
#     process7.export([file_name + "_R3.csv"], excel_or_csv="csv")

# Order Accounts Ascending for All Files
# Make All Revision to R4 for Comparability
# for file_name in DATA_PATH2:
#     process8 = accToNum(data_path=file_name + ".csv", excel_or_csv="csv")
#     process8.process()
#     process8.export([file_name[:-3] + "_R4.csv"], excel_or_csv="csv")

# for file_name in DATA_PATH3:
#     process9 = sortByAcc(data_path=file_name + "_R4.csv", excel_or_csv="csv")
#     process9.process()  # merge sort is used for stability
#     process9.export([file_name + "_R5.csv"], excel_or_csv="csv")

# Remove Unnecessary Index Columns
# Make All Revision to R6 for Comparability
# for file_name in DATA_PATH4:
#     process10 = dropUnnamed(data_path=file_name + ".csv", excel_or_csv="csv")
#     process10.process()
#     process10.export([file_name[:-3] + "_R6.csv"], excel_or_csv="csv")

# process11 = accToNum(data_path="cus_info_R6" + ".csv", excel_or_csv="csv")
# process11.process(drop="cus_no")
# process11.export(["cus_info_R7.csv"], excel_or_csv="csv")

# process12 = monthlyAccessCount(data_path="cus_info_R7" + ".csv", excel_or_csv="csv")
# process12.process()
# process12.export(["cus_info_R8.csv"], excel_or_csv="csv")

# process13 = oneHotSex(data_path="cus_info_R8" + ".csv", excel_or_csv="csv")
# process13.process()
# process13.export(["cus_info_R9.csv"], excel_or_csv="csv")

# process14 = processAge(data_path="cus_info_R9" + ".csv", excel_or_csv="csv")
# process14.process()
# process14.export(["cus_info_R10.csv"], excel_or_csv="csv")

# process15 = regroupSecurity(data_path="cus_info_R10" + ".csv", excel_or_csv="csv")
# process15.process()
# process15.export(["cus_info_R11.csv"], excel_or_csv="csv")
#
# process16 = lifestageProcess(data_path="cus_info_R11" + ".csv", excel_or_csv="csv")
# process16.process()
# process16.export(["cus_info_R12.csv"], excel_or_csv="csv")
#
# process17 = totalDurationInvestingProcess(data_path="cus_info_R13" + ".csv", excel_or_csv="csv")
# process17.process()
# process17.export(["cus_info_R14.csv"], excel_or_csv="csv")
#
# process18 = holdingsTypeProcessing(data_path="cus_info_R14" + ".csv", excel_or_csv="csv")
# process18.process()
# process18.export(["cus_info_R15.csv"], excel_or_csv="csv")
#
# process19 = loyaltyProcess(data_path="cus_info_R15" + ".csv", excel_or_csv="csv")
# process19.process()
# process19.export(["cus_info_R16.csv"], excel_or_csv="csv")

# process20 = mainMarketProcess(data_path="cus_info_R16" + ".csv", excel_or_csv="csv")
# process20.process()
# process20.export(["cus_info_R17.csv"], excel_or_csv="csv")

# process21 = mainSectorProcess(data_path="cus_info_R17" + ".csv", excel_or_csv="csv")
# process21.process()
# process21.export(["cus_info_R18.csv"], excel_or_csv="csv")

# process22 = netWorthProcess(data_path="cus_info_R18" + ".csv", excel_or_csv="csv")
# process22.process()
# process22.export(["cus_info_R19.csv"], excel_or_csv="csv")

process23 = tradeFrequencyProcess(data_path="cus_info_R19" + ".csv", excel_or_csv="csv")
process23.process()
process23.export(["cus_info_R20.csv"], excel_or_csv="csv")