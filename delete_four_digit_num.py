import pandas as pd
import PySimpleGUI as sg
import re

def arg_parse():
    layout = [
        [sg.Text('문장을 입력하세요', size=(25, 1))],
        [sg.InputText()],
        [sg.Text('제거할 숫자의 길이를 입력해주세요')],
        [sg.InputText()],
        [sg.Text('저장할 파일의 이름을 입력하세요')],
        [sg.InputText()],
        [sg.Submit(), sg.Cancel()]]

    window = sg.Window('문장 랜덤 생성기', layout)

    event, values = window.read()
    window.close()

    if event is None or event == 'Cancel':
        exit()

    return values

args = arg_parse()

phrases = args[0].split("\n")
digit = args[1]
file_name = args[2]+".csv"
if args[2] == "":
    file_name = "test.csv"

generated_words_without_number = []

digit_regexp = "\d\d\d\d"
if int(digit) == 3:
    digit_regexp = "\d\d\d"

for p in phrases:
    if p == "":
        continue

    match = re.search(digit_regexp, p)
    if match is None:
        generated_words_without_number.append(p)
        continue

    end = re.search(digit_regexp, p).end()
    if end + 2 < len(p) and (p[end:end + 2] == "ml" or p[end:end + 2] == "kg" or p[end:end + 2] == "cm"):
        generated_words_without_number.append(p)
        continue

    new_p = re.sub(digit_regexp, "", p)
    generated_words_without_number.append(new_p)

generated_words = []
for g in generated_words_without_number:
    new_g = re.sub(" +", " ", g)
    new_g = re.sub("[()]", "", new_g)
    generated_words.append(new_g)


print(len(generated_words))
df = pd.DataFrame(generated_words)
df.to_csv(file_name, encoding="utf-8-sig")
