from data_process_global import *
from data_process_class import *

# Check Number of Accounts per Customer
process = customerAccount(data_path="cus_info.xlsx")
process.process()
process.export(["cus_acc.csv"], excel_or_csv="csv")

# Reorder Data in Chronological Order for each Customer
for file_name in RAW_DATA:
    process1 = chronological(data_path=file_name + ".xlsx")
    process1.export([file_name + "_R1.csv"], excel_or_csv="csv")