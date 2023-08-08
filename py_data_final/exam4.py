# 세종시
# 2012년 ~ 2017년까지
# 30대 인구수 (조치원읍)
import pandas as pd

df = pd.read_csv('datago/201212_201712_연령별인구현황_연간.csv', encoding='cp949')
df_mod = df.drop(['행정구역'], axis=1)
df = pd.concat([df_mod], axis=1)
print(df.head())
# print(df.size)

# 컬럼이름 확인 확인 또는 갯수
print('컬럼개수: ', len(df.columns))
print(df.iloc[1,0])

print(df.iloc[1,range(1, len(df.columns), 6)])