"""
문장 리스트에서 (xxxx) _xxxx 형식의 숫자를 제거해주는 GUI 프로그램

GUI Program that finds pattern of (xxxx) or _xxxx in a list of sentences,
and deletes numbers
"""

import re

import pandas as pd
import PySimpleGUI as sg


def arg_parse():
    layout = [
        [sg.Text("문장을 입력하세요", size=(25, 1))],
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
file_name = args[1] + ".csv"
if args[1] == "":
    file_name = "test.csv"

digit_regexp = "\(\d\d\d\d\)|_\d\d\d\d"

generated_words = []
for p in phrases:
    if p == "":
        continue

    match = re.search(digit_regexp, p)
    if match is None:
        generated_words.append(p)
        continue

    new_p = re.sub(digit_regexp, "", p)
    new_p = re.sub(" {2}", " ", new_p)
    generated_words.append(new_p)

df = pd.DataFrame(generated_words)
df.to_csv(file_name, encoding="utf-8-sig")
