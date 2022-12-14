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

# ??????

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

# def func_process9():
#     process9 = totalAI(data_path="GA2.csv", data_path1="all_R10_2.csv", excel_or_csv="csv")
#     process9.process()
#     process9.export(["all_R10_3_1.csv"], excel_or_csv="csv")

# def func_process10():
#     process10 = combine(data_path="all_R10_3.csv", data_path1="all_R10_3_1.csv", excel_or_csv="csv")
#     process10.process()
#     process10.export(["all_R10_4.csv"], excel_or_csv="csv")
#
# func_process10()

# def func_process11():
#     process11 = totalNonTrading(data_path="GA2.csv", data_path1="all_R10_2.csv", excel_or_csv="csv")
#     process11.process()
#     process11.export(["all_R10_3_2.csv"], excel_or_csv="csv")
#
# def func_process12():
#     process12 = totalMaterial(data_path="GA2.csv", data_path1="all_R10_2.csv", excel_or_csv="csv")
#     process12.process()
#     process12.export(["all_R10_3_3.csv"], excel_or_csv="csv")

# def func_process13():
#     process13 = combine(data_path="all_R10_3.csv", data_path1="all_R10_3_1.csv", data_path2="all_R10_3_2.csv",
#                         data_path3="all_R10_3_3.csv", excel_or_csv="csv")
#     process13.process()
#     process13.export(["all_R10_4.csv"], excel_or_csv="csv")

    # df = pd.read_csv("all_R10_4.csv", encoding='utf-8', sep=',')
    # profile = ProfileReport(df, title="Report")
    # profile.to_file("all_R10_4.html")

# replace all NaN with _ on Excel
# remove acc number 9731 due to TOTAL_NTP outlier
# drop missing rows

# def func_process14():
#     process14 = outlierAndDrop(data_path="all_R10_4.csv", excel_or_csv="csv")
#     process14.process()
#     process14.export(["all_R10_5.csv"], excel_or_csv="csv")
#
# def func_process15():
#     process15 = minMaxScale(data_path="all_R10_5.csv", excel_or_csv="csv")
#     process15.process()
#     process15.export(["all_R10_6.csv"], excel_or_csv="csv")
#
# def func_process16():
#     process16 = dropUnnamed(data_path="all_R10_6.csv", excel_or_csv="csv")
#     process16.process()
#     process16.export(["all_R10_7.csv"], excel_or_csv="csv")

def func_process17():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster1_subcluster1.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster1_sub1_unmapped.csv"], excel_or_csv="csv")

def func_process18():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster1_subcluster2.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster1_sub2_unmapped.csv"], excel_or_csv="csv")

def func_process19():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster1_subcluster3.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster1_sub3_unmapped.csv"], excel_or_csv="csv")

def func_process20():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster1_subcluster4.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster1_sub4_unmapped.csv"], excel_or_csv="csv")

def func_process21():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster2_subcluster1.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster2_sub1_unmapped.csv"], excel_or_csv="csv")

def func_process22():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster2_subcluster2.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster2_sub2_unmapped.csv"], excel_or_csv="csv")

def func_process23():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster2_subcluster3.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster2_sub3_unmapped.csv"], excel_or_csv="csv")

def func_process24():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster2_subcluster4.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster2_sub4_unmapped.csv"], excel_or_csv="csv")

def func_process25():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster3_subcluster1.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster3_sub1_unmapped.csv"], excel_or_csv="csv")

def func_process26():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster3_subcluster2.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster3_sub2_unmapped.csv"], excel_or_csv="csv")

def func_process27():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster3_subcluster3.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster3_sub3_unmapped.csv"], excel_or_csv="csv")

def func_process28():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster3_subcluster4.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster3_sub4_unmapped.csv"], excel_or_csv="csv")

def func_process29():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster4_subcluster1.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster4_sub1_unmapped.csv"], excel_or_csv="csv")

def func_process30():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster4_subcluster2.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster4_sub2_unmapped.csv"], excel_or_csv="csv")

def func_process31():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster4_subcluster3.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster4_sub3_unmapped.csv"], excel_or_csv="csv")

def func_process32():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster4_subcluster4.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster4_sub4_unmapped.csv"], excel_or_csv="csv")

def func_process33():
    df = pd.read_csv("cluster1_sub1_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster1_sub1_unmapped.html")

def func_process34():
    df = pd.read_csv("cluster1_sub2_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster1_sub2_unmapped.html")

def func_process35():
    df = pd.read_csv("cluster1_sub3_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster1_sub3_unmapped.html")

def func_process36():
    df = pd.read_csv("cluster1_sub4_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster1_sub4_unmapped.html")

def func_process37():
    df = pd.read_csv("cluster2_sub1_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster2_sub1_unmapped.html")

def func_process38():
    df = pd.read_csv("cluster2_sub2_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster2_sub2_unmapped.html")

def func_process39():
    df = pd.read_csv("cluster2_sub3_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster2_sub3_unmapped.html")

def func_process40():
    df = pd.read_csv("cluster2_sub4_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster2_sub4_unmapped.html")

def func_process41():
    df = pd.read_csv("cluster3_sub1_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster3_sub1_unmapped.html")

def func_process42():
    df = pd.read_csv("cluster3_sub2_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster3_sub2_unmapped.html")

def func_process43():
    df = pd.read_csv("cluster3_sub3_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster3_sub3_unmapped.html")

def func_process44():
    df = pd.read_csv("cluster3_sub4_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster3_sub4_unmapped.html")

def func_process45():
    df = pd.read_csv("cluster4_sub1_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster4_sub1_unmapped.html")

def func_process46():
    df = pd.read_csv("cluster4_sub2_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster4_sub2_unmapped.html")

def func_process47():
    df = pd.read_csv("cluster4_sub3_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster4_sub3_unmapped.html")

def func_process48():
    df = pd.read_csv("cluster4_sub4_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster4_sub4_unmapped.html")

def func_process49():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster1.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster1_unmapped.csv"], excel_or_csv="csv")

def func_process50():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster2.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster2_unmapped.csv"], excel_or_csv="csv")

def func_process51():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster3.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster3_unmapped.csv"], excel_or_csv="csv")

def func_process52():
    process = unMappedCluster(data_path="all_R10_5.csv", data_path1="Cluster Files/FBA_Finals_cluster4.csv", excel_or_csv="csv")
    process.process(TOP9_FEATURES=TOP9_FEATURES)
    process.export(["cluster4_unmapped.csv"], excel_or_csv="csv")

def func_process53():
    df = pd.read_csv("cluster1_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster1_unmapped.html")

def func_process54():
    df = pd.read_csv("cluster2_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster2_unmapped.html")

def func_process55():
    df = pd.read_csv("cluster3_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster3_unmapped.html")

def func_process56():
    df = pd.read_csv("cluster4_unmapped.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("cluster4_unmapped.html")

def func_process57():
    df = pd.read_csv("all_R10_5.csv", encoding='utf-8', sep=',')
    profile = ProfileReport(df, title="Report")
    profile.to_file("main_unmapped.html")


# check for top-level environment
if __name__ == '__main__':
    start_time = time.time()

    # p9 = multiprocessing.Process(target=func_process9)
    # p9.start()
    #
    # p11 = multiprocessing.Process(target=func_process11)
    # p11.start()
    #
    # p12 = multiprocessing.Process(target=func_process12)
    # p12.start()
    #
    # p9.join()
    # p11.join()
    # p12.join()

    # p17 = multiprocessing.Process(target=func_process17)
    # p17.start()
    #
    # p18 = multiprocessing.Process(target=func_process18)
    # p18.start()
    #
    # p19 = multiprocessing.Process(target=func_process19)
    # p19.start()
    #
    # p20 = multiprocessing.Process(target=func_process20)
    # p20.start()
    #
    # p21 = multiprocessing.Process(target=func_process21)
    # p21.start()
    #
    # p22 = multiprocessing.Process(target=func_process22)
    # p22.start()
    #
    # p23 = multiprocessing.Process(target=func_process23)
    # p23.start()
    #
    # p24 = multiprocessing.Process(target=func_process24)
    # p24.start()
    #
    # p25 = multiprocessing.Process(target=func_process25)
    # p25.start()
    #
    # p26 = multiprocessing.Process(target=func_process26)
    # p26.start()
    #
    # p27 = multiprocessing.Process(target=func_process27)
    # p27.start()
    #
    # p28 = multiprocessing.Process(target=func_process28)
    # p28.start()
    #
    # p29 = multiprocessing.Process(target=func_process29)
    # p29.start()
    #
    # p30 = multiprocessing.Process(target=func_process30)
    # p30.start()
    #
    # p31 = multiprocessing.Process(target=func_process31)
    # p31.start()
    #
    # p32 = multiprocessing.Process(target=func_process32)
    # p32.start()
    #
    # p17.join()
    # p18.join()
    # p19.join()
    # p20.join()
    # p21.join()
    # p22.join()
    # p23.join()
    # p24.join()
    # p25.join()
    # p26.join()
    # p27.join()
    # p28.join()
    # p29.join()
    # p30.join()
    # p31.join()
    # p32.join()

    # p33 = multiprocessing.Process(target=func_process33)
    # p33.start()
    #
    # p34 = multiprocessing.Process(target=func_process34)
    # p34.start()
    #
    # p35 = multiprocessing.Process(target=func_process35)
    # p35.start()
    #
    # p36 = multiprocessing.Process(target=func_process36)
    # p36.start()
    #
    # p37 = multiprocessing.Process(target=func_process37)
    # p37.start()
    #
    # p38 = multiprocessing.Process(target=func_process38)
    # p38.start()
    #
    # p39 = multiprocessing.Process(target=func_process39)
    # p39.start()
    #
    # p40 = multiprocessing.Process(target=func_process40)
    # p40.start()
    #
    # p41 = multiprocessing.Process(target=func_process41)
    # p41.start()
    #
    # p42 = multiprocessing.Process(target=func_process42)
    # p42.start()
    #
    # p43 = multiprocessing.Process(target=func_process43)
    # p43.start()
    #
    # p44 = multiprocessing.Process(target=func_process44)
    # p44.start()
    #
    # p45 = multiprocessing.Process(target=func_process45)
    # p45.start()
    #
    # p46 = multiprocessing.Process(target=func_process46)
    # p46.start()
    #
    # p47 = multiprocessing.Process(target=func_process47)
    # p47.start()
    #
    # p48 = multiprocessing.Process(target=func_process48)
    # p48.start()
    #
    # p33.join()
    # p34.join()
    # p35.join()
    # p36.join()
    # p37.join()
    # p38.join()
    # p39.join()
    # p40.join()
    # p41.join()
    # p42.join()
    # p43.join()
    # p44.join()
    # p45.join()
    # p46.join()
    # p47.join()
    # p48.join()

    # p49 = multiprocessing.Process(target=func_process49)
    # p49.start()
    #
    # p50 = multiprocessing.Process(target=func_process50)
    # p50.start()
    #
    # p51 = multiprocessing.Process(target=func_process51)
    # p51.start()
    #
    # p52 = multiprocessing.Process(target=func_process52)
    # p52.start()
    #
    # p49.join()
    # p50.join()
    # p51.join()
    # p52.join()

    # p53 = multiprocessing.Process(target=func_process53)
    # p53.start()
    #
    # p54 = multiprocessing.Process(target=func_process54)
    # p54.start()
    #
    # p55 = multiprocessing.Process(target=func_process55)
    # p55.start()
    #
    # p56 = multiprocessing.Process(target=func_process56)
    # p56.start()
    #
    # p53.join()
    # p54.join()
    # p55.join()
    # p56.join()

    # func_process14()
    # func_process15()
    # func_process16()
    func_process57()

    print("--- %s seconds ---" % (time.time() - start_time))