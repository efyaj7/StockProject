"""""
__init__

Create a DataManager instance and store it as self.data_manager
Load existing stocks from the JSON file using self.data_manager.load()
Store the loaded stocks in self.stocks as a list of Stock objects


Method 1 — add_stock(ticker, shares, purchase_price)

Takes ticker, shares and purchase price as arguments
Check if the stock already exists in the portfolio — if it does print a message and return
Create a new Stock object with those details
Append it to self.stocks
Save the updated portfolio using self.data_manager.save_price()


Method 2 — remove_stock(ticker)

Takes a ticker as argument
Loop through self.stocks and find the matching stock
Remove it from the list
Save the updated portfolio
If not found — print a message


Method 3 — refresh_prices()

Loop through every stock in self.stocks
Call self.data_manager.fetch_price(stock.ticker) for each one
Update each stock's current_price attribute
Print a message confirming prices were refreshed


Method 4 — total_portfolio_value()

Loop through all stocks
Add up the total value of each stock using stock.total_value()
Return the grand total


Method 5 — display()

Check if portfolio is empty — print message if so
Loop through all stocks and call stock.display() on each one
Print the total portfolio value at the end

"""
import time

from data import DataManager
from Stock import Stock
import pandas  as pd


class Portfolio :

    def __init__(self):

        self.data = DataManager()
        self.cash,data = self.data.load()


        self.stocks = []
        for loaded in data :
            self.stocks.append(Stock(loaded["ticker"] , loaded["shares"] , loaded["purchase_price"] , loaded["current_price"]))





    def add_stock(self , ticker , shares , purchase_price):
        for existing_stock in self.stocks :
            if ticker.upper() == existing_stock.ticker.upper():
                print("this already exists in the portfolio")

                return

        new_stocks = Stock(ticker , shares , purchase_price)

        self.stocks.append(new_stocks)

        portfolio_data = [stock.to_dict() for stock in self.stocks]

        self.data.save_price(portfolio_data , self.cash)
        print(f"{ticker} added successfully")

    def remove_stock(self,ticker) :

        found = False

        for matching_stack in self.stocks:
            if ticker.upper() == matching_stack.ticker.upper():
                cash_received = matching_stack.purcahse_price  * matching_stack.shares
                self.cash += cash_received
                print(self.cash)
                self.stocks.remove(matching_stack)
                found = True
                break


        if found :
            portfolio_data = [stock.to_dict() for stock in self.stocks]
            self.data.save_price(portfolio_data , self.cash)
            print(f"{ticker} succesfully sold")
        else :
            print(print(f"{ticker} not found in portfolio"))



    def refresh_stock(self):

        for refresh_stock in self.stocks :
            price = self.data.fetch_price(refresh_stock.ticker)
            time.sleep(1)

            if price is not None :
                refresh_stock.current_price = price

        portfolio_data = [s.to_dict() for s in self.stocks]
        self.data.save_price(portfolio_data , self.cash)

        print("prices refreshed successfully")
    def total_portfolio_value(self):

        total = 0

        for value in self.stocks :
            stock_value = value.total_value()

            if stock_value is not None :
                total +=  stock_value


        return round(total , 2)

    def display(self) :
        if  self.stocks:
            table = [x.to_dict() for x in self.stocks]
            dataframe_table = pd.DataFrame(table)
            print(dataframe_table)

        print("---------Portfolio-----------")


        TOTAL_NET_WORTH = self.total_portfolio_value() + self.cash


        print(f" this is the total portfolio value : ${self.total_portfolio_value()}")
        print(f" cash : {self.cash}")
        print(f"total networth : {TOTAL_NET_WORTH}")



    def list_tickers(self):
        if not self.stocks:
            print("portfolio is empty")
            return

        for w in self.stocks :
            print(w.ticker)





















"""""
checking = Portfolio()
checking.add_stock("AAPL", 10, 150.00)
checking.refresh_stock()
checking.display()

"""












