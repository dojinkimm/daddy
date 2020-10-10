import random
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

    window = sg.Window("문장 랜덤 생성기", layout)

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

randomized_phrases = []
for p in phrases:
    delimiters = re.split(", |/", p)
    combine = " ".join(delimiters)
    arr = combine.split()
    randomized_phrase = random.sample(arr, len(arr))
    randomized_phrases.append(" ".join(randomized_phrase))

df = pd.DataFrame(randomized_phrases)
df.to_csv(file_name, encoding="utf-8-sig")
