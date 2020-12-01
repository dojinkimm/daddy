import csv
import pandas as pd

past = dict()
cur = dict()
with open("sellcode_2020.csv", newline="") as csvfile:
    rdr = csv.DictReader(csvfile)
    for i in rdr:
        past[i.get("code1")] = i.get("title1")
        if i.get("code2") != "":
            cur[i.get("code2")] = i.get("title2")

print(len(past), len(cur))



# df = pd.DataFrame(exp_time)
# df.to_csv("calculate_time_4.csv", encoding="utf-8-sig")

# df = pd.DataFrame(arr)
# df.to_csv("result.csv", encoding="utf-8-sig")

# xl_file = pd.ExcelFile(file_name)
#
# dfs = {sheet_name: xl_file.parse(sheet_name)
#           for sheet_name in xl_file.sheet_names}