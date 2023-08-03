import datetime
from datetime import datetime, timedelta
import pandas as pd

df = pd.read_csv('data/banklist.csv', encoding='utf-8')
print(df.head())
print(df.columns)