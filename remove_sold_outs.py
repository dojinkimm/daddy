import csv

import pandas as pd
import PySimpleGUI as sg


def arg_parse():
    layout = [
        [sg.Text("파일을 입력하세요(ex. test.csv)", size=(25, 1))],
        [sg.InputText()],
        [sg.Text("저장할 파일의 이름을 입력하세요")],
        [sg.InputText()],
        [sg.Submit(), sg.Cancel()],
    ]

    window = sg.Window("팔린 상품 제거기", layout)

    event, values = window.read()
    window.close()

    if event is None or event == "Cancel":
        exit()

    return values


args = arg_parse()
read_file = args[0].split("\n")[0]
write_file = args[1].split("\n")[0]

past = dict()
cur = dict()
with open(read_file, newline="") as csvfile:
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

if len(past_list) > len(cur_list):
    for i in range(len(cur_list)):
        arr.append(
            {
                "code1": past_list[i][0],
                "title1": past_list[i][1],
                "code2": cur_list[i][0],
                "title2": cur_list[i][1],
            }
        )

    for j in range(len(cur_list), len(past_list)):
        arr.append(
            {
                "code1": past_list[j][0],
                "title1": past_list[j][1],
                "code2": "",
                "title2": "",
            }
        )


if len(cur_list) > len(past_list):
    for i in range(len(past_list)):
        arr.append(
            {
                "code1": past_list[i][0],
                "title1": past_list[i][1],
                "code2": cur_list[i][0],
                "title2": cur_list[i][1],
            }
        )

    for j in range(len(past_list), len(cur_list)):
        arr.append(
            {
                "code1": "",
                "title1": "",
                "code2": cur_list[j][0],
                "title2": cur_list[j][1],
            }
        )

df = pd.DataFrame(arr)
df.to_csv(write_file, encoding="utf-8-sig")
