import urllib.request
import urllib.error
import time
from datetime import date

dday = ''
# 시간표현 DHHMM0 <- 0초
while dday != '616190':
    date = urllib.request.urlopen('http://www.google.com').headers['Date']
    print(date)
    now =  int(time.mktime(time.strptime(date, '%a, %d %b %Y %H:%M:%S %Z')))+64800
    print(now)
    kst = time.gmtime(now)
    dday = str(kst.tm_mday) + str(kst.tm_hour) + str(kst.tm_min) + str(kst.tm_sec)
    print(dday)
print("HIT!!!")


