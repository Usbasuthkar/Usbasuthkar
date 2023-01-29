from datetime import datetime
import yfinance as yf
import yahoofinancials as yfs
import pandas as pd
import socket
now = datetime.now()
hour = now.hour
mins = now.minute
start_date = str(now.year)+"-"+str(now.month)+"-"+str(now.day-1)
end_date = str(now.year)+"-"+str(now.month)+"-"+str(now.day)
if now.day == 1:
    if now.month == 5 or now.month == 7  or now.month==10 or now.month==12:
        start_date = str(now.year)+"-"+str(now.month-1)+"-"+str(now.day+29)
    elif now.month == 2 or now.month == 4 or now.month == 6 or now.month == 8 or now.month == 9 or now.month==11:
        start_date = str(now.year)+"-"+str(now.month-1)+"-"+str(now.day+30)
    elif now.month == 1:
        start_date = str(now.year-1)+"-"+str(now.month+11)+"-"+str(now.day+30)
    elif now.month == 3 and now.year%4 == 0 and now.year%100!=0 or now.year%400 == 0:
        start_date = str(now.year)+"-"+str(now.month)+"-"+str(now.day+28)
    elif now.month == 3 and not now.year%4 == 0 and now.year%100!=0 or now.year%400 == 0:
        start_date = str(now.year)+"-"+str(now.month)+"-"+str(now.day+27)
if now.weekday() == 5:
    if now.day == 1 and now.month == 5 or now.month == 7  or now.month==10 or now.month==12:
        start_date = str(now.year)+"-"+str(now.month-1)+"-"+str(now.day+28)
    elif now.day == 1 and now.month == 2 or now.month == 4 or now.month == 6 or now.month == 8 or now.month == 9 or now.month==11 :
        start_date = str(now.year)+"-"+str(now.month-1)+"-"+str(now.day+29)
    elif now.month == 1 and now.day == 1:
        start_date = str(now.year-1)+"-"+str(now.month+11)+"-"+str(now.day+29)
    elif now.month == 3 and now.day == 1 and now.year%4 == 0 and now.year%100!=0 or now.year%400 == 0:
        start_date = str(now.year)+"-"+str(now.month)+"-"+str(now.day+27)
    elif now.month == 3 and now.day == 1 and not now.year%4 == 0 and now.year%100!=0 or now.year%400 == 0:
        start_date = str(now.year)+"-"+str(now.month)+"-"+str(now.day+25)
if now.weekday() == 6:
    if now.day == 1 and now.month == 5 or now.month == 7  or now.month==10 or now.month==12:
        start_date = str(now.year)+"-"+str(now.month-1)+"-"+str(now.day+27)
    elif now.day == 1 and now.month == 2 or now.month == 4 or now.month == 6 or now.month == 8 or now.month == 9 or now.month==11 :
        start_date = str(now.year)+"-"+str(now.month-1)+"-"+str(now.day+28)
    elif now.month == 1 and now.day == 1:
        start_date = str(now.year-1)+"-"+str(now.month+11)+"-"+str(now.day+28)
    elif now.month == 3 and now.day == 1 and now.year%4 == 0 and now.year%100!=0 or now.year%400 == 0:
        start_date = str(now.year)+"-"+str(now.month)+"-"+str(now.day+26)
    elif now.month == 3 and now.day == 1 and not now.year%4 == 0 and now.year%100!=0 or now.year%400 == 0:
        start_date = str(now.year)+"-"+str(now.month)+"-"+str(now.day+25)
if now.weekday() == 0:
    if now.day == 1 and now.month == 5 or now.month == 7  or now.month==10 or now.month==12:
        start_date = str(now.year)+"-"+str(now.month-1)+"-"+str(now.day+27)
    elif now.day == 1 and now.month == 2 or now.month == 4 or now.month == 6 or now.month == 8 or now.month == 9 or now.month==11:
        start_date = str(now.year)+"-"+str(now.month-1)+"-"+str(now.day+28)
    elif now.month == 1 and now.day == 1:
        start_date = str(now.year-1)+"-"+str(now.month+11)+"-"+str(now.day+28)
    elif now.month == 3 and now.day == 1 and (now.year%4 == 0 and now.year%100!=0 or now.year%400 == 0):
        start_date = str(now.year)+"-"+str(now.month-1)+"-"+str(now.day+26)
    elif now.month == 3 and now.day == 1 and not (now.year%4 == 0 and now.year%100!=0 or now.year%400 == 0):
        start_date = str(now.year)+"-"+str(now.month-1)+"-"+str(now.day+25)
if now.weekday() == 0 and hour >= 9 and mins >= 15:
    if now.day == 1 and now.month == 5 or now.month == 7  or now.month==10 or now.month==12:
        start_date = str(now.year)+"-"+str(now.month-1)+"-"+str(now.day+27)
    elif now.day == 1 and now.month == 2 or now.month == 4 or now.month == 6 or now.month == 8 or now.month == 9 or now.month==11:
        start_date = str(now.year)+"-"+str(now.month-1)+"-"+str(now.day+28)
    elif now.month == 1 and now.day == 1:
        start_date = str(now.year-1)+"-"+str(now.month+11)+"-"+str(now.day+28)
    elif now.month == 3 and now.day == 1 and (now.year%4 == 0 and now.year%100!=0 or now.year%400 == 0):
        start_date = str(now.year)+"-"+str(now.month-1)+"-"+str(now.day+26)
    elif now.month == 3 and now.day == 1 and not (now.year%4 == 0 and now.year%100!=0 or now.year%400 == 0):
        start_date = str(now.year)+"-"+str(now.month-1)+"-"+str(now.day+25)
A = "HUDCO.NS"
print(start_date)
socket.getaddrinfo('localhost', 8080)
try:
    close_rate = yf.download(A,start_date,end_date)
    df = pd.DataFrame(close_rate,columns = ["Close"])
    last_price = df.loc[start_date]
except KeyError:
    close_rate = yf.download(A,"2022-08-01",end_date)
    df = pd.DataFrame(close_rate,columns = ["Close"])
    last_price = df.tail(1)
print("Last",last_price)
price_list = []
historical_price = {}
while True:
    a = datetime.now()
    u = yfs.YahooFinancials([A])
    data = u.get_current_price()
    i = 0
    for j in data.items():
        price_list.append(j[1])
    for i in range(len(price_list)):
        percentage = ((price_list[i] - last_price)/last_price)*100
    i +=1
    for stock_name,price in data.items():
        historical_price[stock_name] = price
        price_list.append(price)
        if percentage.empty > 0:
            print(historical_price,"at time " + str(a.hour) + ":"+str(a.minute) +":"+str(a.second),"percentage:",round(percentage,2),"up")
        elif percentage.empty < 0:
            print(historical_price,"at time " + str(a.hour) + ":"+str(a.minute) +":"+str(a.second),"percentage:",round(percentage,2),"down")
        else:
            print(historical_price,"at time " + str(a.hour) + ":"+str(a.minute) +":"+str(a.second),"percentage:",percentage)