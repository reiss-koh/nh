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

# process16 = customerLvlProcess(data_path="cus_info_R12" + ".csv", excel_or_csv="csv")
# process16.process()
# process16.export(["cus_info_R13.csv"], excel_or_csv="csv")

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

# process23 = tradeFrequencyProcess(data_path="cus_info_R19" + ".csv", excel_or_csv="csv")
# process23.process()
# process23.export(["cus_info_R20.csv"], excel_or_csv="csv")

# process24 = dropColumn(data_path="cus_assets_R6.csv", excel_or_csv="csv")
# process24.process(column_name="mts_mm_access_type")
# process24.export(["cus_assets_R7.csv"], excel_or_csv="csv")

# process25 = dropColumn(data_path="cus_account_R6.csv", excel_or_csv="csv")
# process25.process(column_name="itg_pdt_tp_cd")
# process25.export(["cus_account_R7.csv"], excel_or_csv="csv")

# process26 = maxAssetValue(data_path="cus_assets_R7.csv", excel_or_csv="csv")
# process26.process()
# process26.export(["cus_assets_R8.csv"], excel_or_csv="csv")

# process27 = dropColumn(data_path="cus_info_R20.csv", excel_or_csv="csv")
# process27.process(column_name="cus_aet_stn_cd")
# process27.export(["cus_info_R21.csv"], excel_or_csv="csv")

# process28 = accLifespan(data_path="cus_info_R21.csv", excel_or_csv="csv")
# process28.process()
# process28.export(["cus_info_R22.csv"], excel_or_csv="csv")

# process29 = dropUnnamed(data_path="cus_info_R22.csv", excel_or_csv="csv")
# process29.process()
# process29.export(["cus_info_R23.csv"], excel_or_csv="csv")

# process30 = infoToCrossSectMode(data_path="cus_info_R23.csv", excel_or_csv="csv")
# process30.process()
# process30.export(["cus_info_R23_mode.csv"], excel_or_csv="csv")

# process31 = infoToCrossSectMax(data_path="cus_info_R23.csv", excel_or_csv="csv")
# process31.process()
# process31.export(["cus_info_R23_max.csv"], excel_or_csv="csv")

# process32 = concatDataframes(data_path="cus_info_R23_mode.csv", data_path1="cus_info_R23_max.csv", excel_or_csv="csv")
# process32.process()
# process32.export(["cus_info_R24.csv"], excel_or_csv="csv")

# process33 = dropUnnamed(data_path="cus_info_R24.csv", excel_or_csv="csv")
# process33.process()
# process33.export(["cus_info_R25.csv"], excel_or_csv="csv")

# process34 = dropColumn(data_path="cus_account_R7.csv", excel_or_csv="csv")
# process34.process(column_name="fc_sec_trd_nat_cd")
# process34.export(["cus_account_R8.csv"], excel_or_csv="csv")

# process35 = removeWhiteSpace(data_path="cus_account_R8.csv", excel_or_csv="csv")
# process35.process(column_name="iem_cd")
# process35.export(["cus_account_R9.csv"], excel_or_csv="csv")

# process36 = getTicker(data_path="cus_account_R10.xlsx")
# process36.process()
# process36.export(["cus_account_R11.csv"], excel_or_csv="csv")

# process37 = accountDrop(data_path="cus_account_R12.xlsx")
# process37.process()
# process37.export(["cus_account_R13.csv"], excel_or_csv="csv")
#
# process38 = dropUnnamed(data_path="cus_account_R13.csv", excel_or_csv="csv")
# process38.process()
# process38.export(["cus_account_R14.csv"], excel_or_csv="csv")

# process39 = finalVol3M(data_path="cus_account_R14.csv", excel_or_csv="csv")
# process39.process()
# process39.export(["cus_account_R15.csv"], excel_or_csv="csv")

# process40 = valueWeightedVolatility(data_path="cus_account_R15.csv", excel_or_csv="csv")
# process40.process()
# process40.export(["cus_account_R16.csv"], excel_or_csv="csv")

# process41 = aggregateLeverage(data_path="cus_account_R15.csv", excel_or_csv="csv")
# process41.process()
# process41.export(["cus_account_R17.csv"], excel_or_csv="csv")

# process42 = concatDataframes2(data_path="cus_account_R16.csv", data_path1="cus_account_R17.csv", excel_or_csv="csv")
# process42.process(column_name="leverage")
# process42.export(["cus_account_R18.csv"], excel_or_csv="csv")

# process43 = concatAll(data_path="cus_info_R25.csv", data_path1="cus_assets_R8.csv", data_path2="cus_account_R18.csv", excel_or_csv="csv")
# process43.process(path1_column="MAX_ASSET_VALUE", path2_column="value_weighted_volatility", path2_column1="leverage")
# process43.export(["all_R1.csv"], excel_or_csv="csv")

# process44 = dropColumn(data_path="all_R1.csv", excel_or_csv="csv")
# process44.process(column_name="SEX_NA")
# process44.export(["all_R2.csv"], excel_or_csv="csv")
#
# process45 = dropColumn(data_path="all_R2.csv", excel_or_csv="csv")
# process45.process(column_name="LIFESTAGE_NA")
# process45.export(["all_R3.csv"], excel_or_csv="csv")
#
# process46 = dropColumn(data_path="all_R3.csv", excel_or_csv="csv")
# process46.process(column_name="HOLDINGS_TYPE_NA")
# process46.export(["all_R4.csv"], excel_or_csv="csv")
#
# process47 = dropColumn(data_path="all_R4.csv", excel_or_csv="csv")
# process47.process(column_name="act_no.1")
# process47.export(["all_R5.csv"], excel_or_csv="csv")

# process48 = dropMissingData(data_path="all_R5.csv", excel_or_csv="csv")
# process48.process()
# process48.export(["all_R6.csv"], excel_or_csv="csv")

# process49 = processMissingData(data_path="all_R6.csv", excel_or_csv="csv")
# process49.process()
# process49.export(["all_R7.csv"], excel_or_csv="csv")

# process50 = dropColumn(data_path="all_R7.csv", excel_or_csv="csv")
# process50.process(column_name="index")
# process50.export(["all_R8.csv"], excel_or_csv="csv")
#
# process51 = dropUnnamed(data_path="all_R8.csv", excel_or_csv="csv")
# process51.process()
# process51.export(["all_R9.csv"], excel_or_csv="csv")

# R10: Removed accounts in top 0.1% of leverage and/or 0.1% of peak assets
# process52 = oneHotAccount(data_path="all_R10.csv", excel_or_csv="csv")
# process52.process()
# process52.export(["all_R11.csv"], excel_or_csv="csv")

# process53 = minMaxScale(data_path="all_R11.csv", excel_or_csv="csv")
# process53.process()
# process53.export(["all_R12.csv"], excel_or_csv="csv")

# process54 = dropUnnamed(data_path="all_R12.csv", excel_or_csv="csv")
# process54.process()
# process54.export(["all_R13.csv"], excel_or_csv="csv")

# process52 = minMaxScale(data_path="all_R10.csv", excel_or_csv="csv")
# process52.process()
# process52.export(["all_R11.csv"], excel_or_csv="csv")
#
# process53 = dropUnnamed(data_path="all_R11.csv", excel_or_csv="csv")
# process53.process()
# process53.export(["all_R12.csv"], excel_or_csv="csv")

# 본선

# process = groupAndOrder(data_path="GA.csv", excel_or_csv="csv")
# process.process(group_by="CUS_NO", order_by="VISIT_DATE")
# process.export(["GA1.csv"], excel_or_csv="csv")

# group customers together

# process = group(data_path="GA.csv", excel_or_csv="csv")
# process.process(group_by="CUS_NO", order_by="VISIT_DATE")
# process.export(["GA1.csv"], excel_or_csv="csv")

# map customers and accounts

# process1 = mapCusAcc(data_path="cus_info_R2.csv", excel_or_csv="csv")
# process1.process(unique_column="cus_no")
# process1.export(["MAP_CUS_ACC.csv"], excel_or_csv="csv")

# process2 = readData(data_path="GA.csv", excel_or_csv="csv")
# process2.process()

# count unique number of customers

# process3 = uniqueCus(data_path="GA1.csv", excel_or_csv="csv")
# process3.process()
# output: 8061 unique customers

# map GA1 cus_no to acc_no in data_final.csv

# process4 = mapGA(data_path="GA1.csv", data_path1="MAP_CUS_ACC.csv", excel_or_csv="csv")
# process4.process()
# process4.export(["GA2.csv"], excel_or_csv="csv")

# process5 = readData(data_path="GA2.csv", excel_or_csv="csv")
# process5.process()

# map GA1 cus_no to acc_no in data_final.csv

# process6 = sumByCus(data_path="GA2.csv", data_path1="all_R10.csv", excel_or_csv="csv")
# process6.process(col="DURATION_SUM", col1="VIEW_CNT")
# process6.export(["all_R10_1.csv"], excel_or_csv="csv")

# process7 = totalForeign(data_path="GA2.csv", data_path1="all_R10_1.csv", excel_or_csv="csv")
# process7.process()
# process7.export(["all_R10_2.csv"], excel_or_csv="csv")

# def func_process8():
#     process8 = totalAdv(data_path="GA2.csv", data_path1="all_R10_2.csv", excel_or_csv="csv")
#     process8.process()
#     process8.export(["all_R10_3.csv"], excel_or_csv="csv")

# t8 = threading.Thread(target=func_process8)
# t8.start()

def func_process9():
    process9 = totalAI(data_path="GA2.csv", data_path1="all_R10_2.csv", excel_or_csv="csv")
    process9.process()
    process9.export(["all_R10_3_1.csv"], excel_or_csv="csv")

# def func_process10():
#     process10 = combine(data_path="all_R10_3.csv", data_path1="all_R10_3_1.csv", excel_or_csv="csv")
#     process10.process()
#     process10.export(["all_R10_4.csv"], excel_or_csv="csv")
#
# func_process10()

def func_process11():
    process11 = totalNonTrading(data_path="GA2.csv", data_path1="all_R10_2.csv", excel_or_csv="csv")
    process11.process()
    process11.export(["all_R10_3_2.csv"], excel_or_csv="csv")

def func_process12():
    process12 = totalMaterial(data_path="GA2.csv", data_path1="all_R10_2.csv", excel_or_csv="csv")
    process12.process()
    process12.export(["all_R10_3_3.csv"], excel_or_csv="csv")

# check for top-level environment
if __name__ == '__main__':
    start_time = time.time()

    p9 = multiprocessing.Process(target=func_process9)
    p9.start()

    p11 = multiprocessing.Process(target=func_process11)
    p11.start()

    p12 = multiprocessing.Process(target=func_process12)
    p12.start()

    p9.join()
    p11.join()
    p12.join()

    print("--- %s seconds ---" % (time.time() - start_time))