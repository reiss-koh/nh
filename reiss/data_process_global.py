

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