export_arr = []
for i in range(1, 39):
    export_arr.append("insu/energy/energy_" + str(i) + ".csv")

process41 = toStockOCHLV(data_path="insu/energy_close_raw.xlsx", data_path1="insu/energy_high_raw.xlsx", data_path2="insu/energy_low_raw.xlsx", data_path3="insu/energy_open_raw.xlsx", data_path4="insu/energy_volume_raw.xlsx")
process41.process()
process41.export(export_arr, excel_or_csv="csv")