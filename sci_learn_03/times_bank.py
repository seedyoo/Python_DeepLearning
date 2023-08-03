import datetime
from datetime import datetime, timedelta
import pandas as pd

df = pd.read_csv('data/banklist.csv', encoding='utf-8')
df['close_dt'] = pd.to_datetime(df['Closing Date'])
df['update_dt'] = pd.to_datetime(df['Updated Date'])
df['close_year'] = df['close_dt'].dt.year   # 연도만 가지고 그룹핑
# 그룹핑하면 새롭게 Series 데이터 생성
sr_closing_year = df.groupby(['close_year']).size()
# print(df.head())
# df.info()
# print(sr_closing_year)
df_group = sr_closing_year.reset_index()
df_group.columns = ['year', 'count']

print(df_group)

import matplotlib.pyplot as plt
plt.plot(df_group['year'], df_group['count'])
plt.show()