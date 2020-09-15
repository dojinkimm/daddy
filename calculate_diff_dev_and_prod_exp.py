import csv
import pandas as pd

# 09-15
prod_arr = []
with open("production_exp.csv", newline="") as csvfile:
    rdr = csv.DictReader(csvfile)
    for i in rdr:
        prod_arr.append(i.get("experiment_key"))


with open("development_exp.csv", newline="") as csvfile:
    rdr = csv.DictReader(csvfile)
    for i in rdr:
        if i.get("experiment_key") not in prod_arr:
            print(i.get("experiment_key"))


# collect_my_tab_show_organization_terms_on_api_link_server
# auth_show_toast_after_api_authentication_ios
# reliability_replace_banksaladgateway_with_lightweightgateway_mobile