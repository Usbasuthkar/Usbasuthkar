from datetime import datetime
import yfinance as yf
import yahoofinancials as yfs
import bugfix as bf
import pandas as pd
import socket
now = datetime.now()
hour = now.hour
mins = now.minute
start_date = "2022-01-01"
end_date = str(now.year)+"-"+str(now.month)+"-"+str(now.day)
region = input("enter region: ")
A = input("enter stock name: ")
if(region == 'US'):
    pass
elif(region == 'IN'):
    A = A + '.NS'
elif(region == "GR"):
    A = A + '.DE'
elif(region == "BE"):
    A = A + '.BR'
elif(region=='CA'):
    A = A + '.TO'
elif(region == "MX"):
    A = A + '.V'
elif(region == 'BR'):
    A = A + '.SA'
elif(region == 'TR'):
    A = A + '.IS'
elif(region == 'SA'):
    A = A + 'JO'
socket.getaddrinfo('localhost', 8080)
flag = 0
try:
    close_rate = yf.download(A,start_date,end_date)
    df = pd.DataFrame(close_rate,columns = ["Close"])
    last_price = df.tail(1).values
    print("Last",last_price[0][0])
except:
    flag = 1
    print("THIS COMPANY IS DELISTED OR DOSEN'T BELONG TO THE PARTICULAR REGION")
price_list = []
historical_price = {}
u = yfs.YahooFinancials([A])
data = u.get_current_price()
while True:
    a = datetime.now()
    stock = yfs.YahooFinancials([A])
    data = stock.get_current_price()
    i = 0
    if(flag == 1):
        percentage = 0
    else:
        for j in data.items():
            price_list.append(j[1])
        for i in range(len(price_list)):
            percentage = ((price_list[i] - last_price[0][0])/last_price[0][0])*100
        i +=1
    for stock_name,price in data.items():
        stock_name = stock_name[:-3]
        historical_price[stock_name] = price
        price_list.append(price)
        if percentage > 0:
            print(historical_price,"at time " + str(a.hour) + ":"+str(a.minute) +":"+str(a.second),"percentage:",round(percentage,2),"up")
        elif percentage < 0:
            print(historical_price,"at time " + str(a.hour) + ":"+str(a.minute) +":"+str(a.second),"percentage:",round(percentage,2),"down")
        else:
            print(historical_price,"at time " + str(a.hour) + ":"+str(a.minute) +":"+str(a.second),"percentage:",percentage)
