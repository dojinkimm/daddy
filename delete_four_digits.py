"""
문장 리스트에서 4자리 혹은 3자리 숫자를 찾아서 숫자를 제거해주는 GUI 프로그램

GUI Program that finds four digit or three digit number in a list of sentences,
and deletes numbers
"""

import re

import pandas as pd
import PySimpleGUI as sg


def arg_parse():
    layout = [
        [sg.Text("문장을 입력하세요", size=(25, 1))],
        [sg.InputText()],
        [sg.Text("제거할 숫자의 길이를 입력해주세요")],
        [sg.InputText()],
        [sg.Text("저장할 파일의 이름을 입력하세요")],
        [sg.InputText()],
        [sg.Submit(), sg.Cancel()],
    ]

    window = sg.Window("문장 숫자 제거기", layout)

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

digit_regexp = "\d\d\d\d"
if digit != "" and int(digit) == 3:
    digit_regexp = "\d\d\d"

generated_words = []
for p in phrases:
    if p == "":
        continue

    match = re.search(digit_regexp, p)
    if match is None:
        generated_words.append(p)
        continue

    end = re.search(digit_regexp, p).end()
    if end + 2 < len(p) and (
        p[end : end + 2] == "ml"
        or p[end : end + 2] == "kg"
        or p[end : end + 2] == "cm"
    ):
        generated_words.append(p)
        continue

    new_p = re.sub(digit_regexp, "", p)
    generated_words.append(new_p)

df = pd.DataFrame(generated_words)
df.to_csv(file_name, encoding="utf-8-sig")
