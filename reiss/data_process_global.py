
def can_convert_to_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

RAW_DATA = ("cus_info",
            "cus_account")

RAW_DATA1 = ("kr_equity",
             "os_equity")

DATA_PATH = ("kr_equity",
             "os_equity",
             "cus_account")

DATA_PATH1 = ("os_equity",
              "cus_account")

DATA_PATH2 = ("cus_account_R3",
              "cus_assets_R1",
              "kr_equity_R2",
              "os_equity_R3")

DATA_PATH3 = ("cus_account",
              "cus_assets",
              "kr_equity",
              "os_equity")

DATA_PATH4 = ("cus_account_R5",
              "cus_assets_R5",
              "kr_equity_R5",
              "os_equity_R5",
              "cus_info_R3")

ASSET_COLUMNS = ("tot_aet_tld_rnd_202201",
                 "tot_aet_tld_rnd_202202",
                 "tot_aet_tld_rnd_202203",
                 "tot_aet_tld_rnd_202204",
                 "tot_aet_tld_rnd_202205",
                 "tot_aet_tld_rnd_202206")

MODE_COLUMNS = ("act_no",
                "mts_mm_access_type",
                "SEX_F",
                "SEX_M",
                "SEX_NA",
                "cus_age_stn_cd",
                "pft_amt_stn_cd",
                "fst_act_opn_dt",
                "LIFESTAGE_1",
                "LIFESTAGE_2",
                "LIFESTAGE_3",
                "LIFESTAGE_4",
                "LIFESTAGE_5",
                "LIFESTAGE_6",
                "LIFESTAGE_7",
                "LIFESTAGE_8",
                "LIFESTAGE_9",
                "LIFESTAGE_10",
                "LIFESTAGE_NA",
                "tco_cus_grd_cd",
                "tot_ivs_te_sgm_cd",
                "HOLDINGS_TYPE_1.0",
                "HOLDINGS_TYPE_2.0",
                "HOLDINGS_TYPE_3.0",
                "HOLDINGS_TYPE_4.0",
                "HOLDINGS_TYPE_NA",
                "loy_sgm_cd",
                "SECTOR_1.0",
                "SECTOR_2.0",
                "SECTOR_3.0",
                "SECTOR_4.0",
                "SECTOR_5.0",
                "SECTOR_6.0",
                "SECTOR_7.0",
                "SECTOR_8.0",
                "SECTOR_9.0",
                "SECTOR_10.0",
                "SECTOR_11.0",
                "SECTOR_12.0",
                "SECTOR_13.0",
                "SECTOR_14.0",
                "SECTOR_15.0",
                "SECTOR_16.0")

MAX_COLUMNS = ("stk_pdt_hld_yn",
               "ose_stk_pdt_hld_yn",
               "mrz_pdt_tp_sgm_cd",
               "mrz_mkt_dit_cd",
               "aet_bse_stk_trd_tp_cd",
               "bas_stk_trd_tp_cd")