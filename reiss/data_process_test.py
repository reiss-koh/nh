from data_process_global import *
from data_process_class import *

process9 = totalAI(data_path="GA2.csv", data_path1="all_R10_2.csv", excel_or_csv="csv")
process9.process()
process9.export(["all_R10_3_1.csv"], excel_or_csv="csv")