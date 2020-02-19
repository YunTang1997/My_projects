from datetime import datetime, timedelta, date, time
from dateutil.parser import parse

dt = datetime(2011, 10, 29, 20, 30, 21)
dt2 = datetime(2011, 11, 15, 22, 30)
print(dt.day)
print(dt.minute)
print('日期是：' + str(dt.date()))
print('时间是：' + str(dt.time()))

print(str(dt))  # 将datetime对象按默认格式转化为字符串
print(dt.strftime('%m/%d/%Y %H:%M'))  # 将datetime对象按指定格式转化为字符串
print(parse('20091031'))  # 将字符串按默认格式转化为datetime对象
print(datetime.strptime('20091031', '%Y%m%d'))  # 将字符串按指定格式转化为datetime对象
print(dt.replace(minute=0, second=0))  # 将分钟、秒替换为0

delta = dt2 - dt
print(delta)
print('两者相差多少秒： ' + str(delta.total_seconds()))  # 将两者时差转化为总共多少秒

dt + timedelta(hours=10)
dt + timedelta(days=1)
dt + timedelta(days=2, hours=12)
