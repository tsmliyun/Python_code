import time

# print(time.time())
#
# print(time.localtime())
#
# print(time.strftime('%Y-%m-%d %H:%M:%S'))


import datetime

print(datetime.datetime.now())
newtime = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + newtime)

oneday = datetime.datetime(2009, 5, 28)
newdate = datetime.timedelta(days=10)
print(oneday + newdate)
