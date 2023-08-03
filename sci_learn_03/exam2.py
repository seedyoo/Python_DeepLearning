# unit price 엑셀데이터를 사용하여 직원 1인당 비용
# 총인원 40 (Senior 10명, Junior 30명)
# 1인당 비용 비율 2:1 (2만원:만원)
# x원*30명 + 2*x원*10명 = 총비용

import pandas as pd

df = pd.read_excel('data/unit_price.xlsx')

def multilpy_columns(vec) :
    return vec['price'] * vec['count']

df2 = df.apply(multilpy_columns, axis=1)
df['s_sum'] = df2
total = df['s_sum'].sum()
print(total)
senior = 2 * total / 50
junior = total / 50
print(senior)
print(junior)

