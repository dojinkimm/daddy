import re

import pandas as pd
import PySimpleGUI as sg


def arg_parse():
    layout = [
        [sg.Text("문장을 입력하세요", size=(25, 1))],
        [sg.InputText()],
        [sg.Text("제거할 단어들을 입력해주세요")],
        [sg.InputText()],
        [sg.Text("저장할 파일의 이름을 입력하세요")],
        [sg.InputText()],
        [sg.Submit(), sg.Cancel()],
    ]

    window = sg.Window("문장 단어 제거기", layout)

    event, values = window.read()
    window.close()

    if event is None or event == "Cancel":
        exit()

    return values


args = arg_parse()

phrases = args[0].split("\n")
words = args[1].split("\n")
file_name = args[2] + ".csv"
if args[2] == "":
    file_name = "test.csv"

generated_words = []
for p in phrases:
    if p == "":
        continue

    new_p = p
    for w in words:
        new_p = re.sub(w, "", new_p)

    new_p = re.sub(" {2}", " ", new_p)
    generated_words.append(new_p)

df = pd.DataFrame(generated_words)
df.to_csv(file_name, encoding="utf-8-sig")
