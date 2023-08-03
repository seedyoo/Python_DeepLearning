import datetime
from datetime import datetime, timedelta

today = datetime.today()
tommorow = today + timedelta(days=1)
print(tommorow)
# 내일의 날짜정보만 추출
# tomDate = tommorow .strftime('%Y-%m-%d')
tomDate = tommorow .strftime('%Y년%m월%d일')
print(tomDate)
# tomDate = tommorow .strftime('%H-%M-%S')

