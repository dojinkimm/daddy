from itertools import permutations
import pandas as pd
import PySimpleGUI as sg

def arg_parse():
    layout = [
        [sg.Text('문장을 입력하세요', size=(25, 1))],
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

phrase = args[0]
file_name = args[1]+".csv"

perm = permutations(phrase.split())
arr = []

for p in perm:
    randomized_phraze = ""
    for word in p:
        randomized_phraze += word + " "
    arr.append(randomized_phraze[:-1])

df = pd.DataFrame(arr)
df.to_csv(file_name)
