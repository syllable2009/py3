from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)
print(type(now))
dt = datetime(2015, 4, 19, 12, 20, 1)
print(dt)
print(dt.timestamp())  # timestamp是一个浮点数，整数位表示秒,timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的
print(datetime.fromtimestamp(1429417200.0))
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
print(now.strftime('%Y-%m-%d %H:%M:%S'))
f = now + timedelta(days=2, hours=12);  # datetime加减
print(datetime.strftime(f, '%Y-%m-%d %H:%M:%S'))

tz_utc_8 = timezone(timedelta(hours=8))  # 创建时区UTC+8:00
dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:00

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)  # 拿到UTC时间，并强制设置时区为UTC+0:00
print(datetime.strftime(utc_dt, '%Y-%m-%d %H:%M:%S'))
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))  # astimezone()将转换时区为北京时间
print(datetime.strftime(bj_dt, '%Y-%m-%d %H:%M:%S'))

