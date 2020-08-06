from itertools import permutations
import pandas as pd
import PySimpleGUI as sg

"""
코멕스 데이킵스 II 냉장고 문짝 용기 490ml (소)
데이드림내추럴리헤어마스카라/새치커버/염색/뿌리/스피드/헤어스타일/워터프루프/모발케어/대용량
NOMADE 20L 워터박스(수통)
290ml 테이크아웃 / 거리-베이지 종이컵 100개 X 2개
Urban 인테리어 투명 아크릴 한국형 티슈 휴지케이스
DY 콕스 천연갈대 소재의 빗자루 갈목비
미소반 깊은맛을 살린 건강하고 맛있는 절임 베이직 4종세트(명이나물 고추냉이잎 돌산갓 방풍나물)
접착식 3D입체 벽돌단열벽지 20M 1개 보온벽지
"""


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
