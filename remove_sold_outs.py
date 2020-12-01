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

keys = []
for k, v in past.items():
    if k not in cur:
        keys.append(k)

for k in keys:
    del past[k]

past_list = []
for k, v in past.items():
    past_list.append([k, v])

cur_list = []
for k, v in cur.items():
    cur_list.append([k, v])

arr = []
for i in range(len(past_list)):
    arr.append({
        "code1": past_list[i][0],
        "title1": past_list[i][1],
        "code2": cur_list[i][0],
        "title2": cur_list[i][1],
    })

arr.append({
    "code1": "",
    "title1": "",
    "code2": cur_list[len(cur_list)-1][0],
    "title2": cur_list[len(cur_list)-1][1],
})

print(len(arr))

df = pd.DataFrame(arr)
df.to_csv("testtest.csv", encoding="utf-8-sig")
