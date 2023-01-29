import pandas as pd
import datetime as datetime
import yfinance as yf
import yahoofinancials as yfs
import matplotlib.pyplot as plt
import pandas_datareader as pdr
y = int(input("enter year to be checked: "))
m = int(input("enter month to be checked: "))
d = int(input("enter date to be checked: "))
c = datetime.datetime.now()
day = c.day
month = c.month
year = c.year
start_date = str(y) + "-" + str(m) + "-" + str(d)
end_date = str(year) + "-" + str(month) + "-" + str(day)
A = "TSLA"
stock = yf.download(A,start_date,end_date)
df = pd.DataFrame(stock,columns = ["Close"])
u = yfs.YahooFinancials([A])
data = u.get_current_price()
for stock_name,price in data.items():
    p = price
    if stock_name.endswith(".NS"):
        print(stock_name,":",price,"Rs")
    else:
        print(stock_name,":",price,"$")
if p != None:
    amount = int(input("How much do u want to invest(enter amount): "))
    for stock_name,price in data.items():
            shares = amount/price
    print("shares u have recieved: ",shares)
    for stock_name,price in data.items():
            profit = shares*price - amount
    print("if u sell now u will have a profit of: ",profit)
else:
    pass
#x = u.get_daily_dividend_data(start_date, end_date)
#print(x)
plt.style.use("dark_background")
df.plot(cmap="Wistia")
plt.show()
