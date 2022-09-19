from data_process_global import *
from data_process_class import *

process = uniqueAccount(data_path="cus_ifo.csv", excel_or_csv="csv")
process.process()
process.export("cus_acc.csv", excel_or_csv="csv")

for file_name in RAW_DATA:
    process1 = chronological(data_path=file_name + ".csv", excel_or_csv="csv")
    process1.process()
    process1.export(file_name + "_R1.csv", excel_or_csv="csv")