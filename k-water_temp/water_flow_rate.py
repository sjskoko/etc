from asyncio.windows_events import NULL
from cmath import nan
from typing import DefaultDict
from xml.dom import WrongDocumentErr
import pandas as pd
from collections import defaultdict
from tqdm import tqdm
import matplotlib.pyplot as plt
import pickle
import numpy as np

# pickle 저장
# with open('./k-water_temp/data/tag_data.pickle', 'wb') as f:
#     pickle.dump(tag_data, f)

'''
데이터 로드
'''
# 원 DATA
data = pd.read_csv('./k-water_temp/data/water_flow.csv', encoding='cp949')
# tag 별 정리 DATA
with open('./k-water_temp/data/tag_data.pickle', 'rb') as f:
    tag_data = pickle.load(f)

data['발생일자']

# data1 = pd.DataFrame(columns=data.columns)
# data1.loc[len(data1)] = data.iloc[0].copy()

tags = sorted(list(set(data['자료 수집 TAG 설명'].values.tolist())))

tag_data = defaultdict(pd.DataFrame)
for tag in tags:
    tag_data[tag] = pd.DataFrame(columns=data.columns)

for i in tqdm(range(len(data))):
    target_df = tag_data[data.iloc[i]['자료 수집 TAG 설명']]
    target_df.loc[len(target_df)] = data.iloc[i].copy()

tag_data['팔당1(취)1단계관로유출적산#1차'].plot(x='발생일자', y='압력')
plt.show()

max(tag_data['팔당(1취) 유량순시#1']['압력']) # 999
min(tag_data['팔당(1취) 유량순시#1']['압력']) # 0

max(tag_data['팔당(1취) 유량순시#1']['압력']) # 999
min(tag_data['팔당(1취) 유량순시#1']['압력']) # 0




for tag in tqdm(tag_data):
    for i in range(len(tag_data[tag])):
        while ',' in tag_data[tag].loc[i, '압력']:
            tag_data[tag].loc[i, '압력'] = tag_data[tag].loc[i, '압력'].replace(',', '', )
    
for tag in tqdm(tag_data):
    wrong_data = []
    for i in range(len(tag_data[tag])):
        try:
            tag_data[tag].loc[i, '압력'] = float(tag_data[tag].loc[i, '압력'])
        except:
            fault = tag_data[tag].loc[i, '압력']
            wrong_data.append((i, fault, type(fault)))
            tag_data[tag].loc[i, '압력'] = np.NaN
    print(f'{tag} 항목의 {[i[0] for i in wrong_data]}번째 행에 문제가 있습니다')
    print(f'값은 각각 {[i[1] for i in wrong_data]}이며 해당 항목의 타입은 {[i[2] for i in wrong_data]}입니다')
    print(f'총 {len(wrong_data)}개의 값을 nan으로 변환하였습니다')
