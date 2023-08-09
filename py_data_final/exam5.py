import pandas as pd

df = pd.read_csv('datago/201212_201412_연령별인구현황_연간.csv', encoding='cp949')

for r in range(1, len(df)):
    print(df.iloc[r,0])
    for c in range(len(df.columns)):
        if df.columns[c].endswith('년_거주자_30~39세'):
            print(df.iloc[r,c])

# 2017년에 인구수가 제일 많은 행정구역은 어디인가요?
