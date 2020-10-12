"""
문장 리스트에서 4자리 혹은 3자리 숫자를 찾아서 랜덤 숫자로 변경해주는 GUI 프로그램

GUI Program that finds four digit or three digit number in a list of sentences,
and changes to random number
"""


import random
import re

import pandas as pd
import PySimpleGUI as sg


def arg_parse():
    layout = [
        [sg.Text("문장을 입력하세요", size=(25, 1))],
        [sg.InputText()],
        [sg.Text("변경할 숫자의 길이를 입력해주세요")],
        [sg.InputText()],
        [sg.Text("저장할 파일의 이름을 입력하세요")],
        [sg.InputText()],
        [sg.Submit(), sg.Cancel()],
    ]

    window = sg.Window("문장 숫자 랜덤 생성기", layout)

    event, values = window.read()
    window.close()

    if event is None or event == "Cancel":
        exit()

    return values


args = arg_parse()

phrases = args[0].split("\n")
digit = args[1]
file_name = args[2] + ".csv"
if args[2] == "":
    file_name = "test.csv"

generated_words = []
digit_regexp = "\d\d\d\d((?=[^kg|^Kg|^ml|^cm|^mm|^MM|^WT]))|\d\d\d\d$"
if digit != "" and int(digit) == 3:
    digit_regexp = "\d\d\d\d((?=[^kg|^Kg|^ml|^cm|^mm|^MM|^WT]))|\d\d\d\d$"
for p in phrases:
    if p == "":
        continue

    match = re.search(digit_regexp, p)
    if match is None:
        generated_words.append(p)
        continue

    rand = random.randint(1000, 9999)
    if digit != "" and int(digit) == 3:
        rand = random.randint(100, 999)
    random.seed(p)

    new_p = re.sub(digit_regexp, str(rand), p)
    generated_words.append(new_p)

df = pd.DataFrame(generated_words)
df.to_csv(file_name, encoding="utf-8-sig")
