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
import matplotlib.pyplot as plt



class Portfolio :

    def __init__(self):

        self.data = DataManager()
        self.cash,data = self.data.load()


        self.stocks = [] # []
        for loaded in data :
            self.stocks.append(Stock(loaded["ticker"] , loaded["shares"] , loaded["purchase_price"] , loaded["current_price"]))



    def add_stock(self , ticker , shares ):

        purchase_price = self.data.fetch_historical_price(ticker)

        price_to_check = self.data.fetch_price(ticker)

        if purchase_price is None:
            print("could not fetch historical price")
            return

        if price_to_check is None:
            print("could not fetch current price")

        today_price = price_to_check if price_to_check is not None else purchase_price
        # guarantees current_price is never left blank - falls back to the price we
        # already have (purchase_price) if the live fetch failed

        # you want to make sure that the person actually has the money to purchase what they want
        cost = purchase_price * shares
        #

        if cost > self.cash :
            # checking to see whether
            print(f"not enough money - this would cost £{cost:.2f}")
            return

        match = False

        for existing_stock in self.stocks :
            if ticker.upper() == existing_stock.ticker.upper():
                """
                what this does it checks whether the ticker the user has matches whats inside 
                
                self.stocks = [
                    Stock<ticker="SHEL", shares=100, purchase_price=77.54, current_price=89.53>,
                    Stock<ticker="AAPL", shares=100, purchase_price=281.74, current_price=331.90>,
                    Stock<ticker="BP",   shares=50,  purchase_price=37.35,  current_price=43.85>,
                    Stock<ticker="AAL",  shares=200, purchase_price=16.52,  current_price=15.27>,
                ]
                
                you would have something like this 
                
                """
                total_shares = existing_stock.shares + shares  # 100 shares + 50 shares
                total_cost = (existing_stock.purchase_price * existing_stock.shares) + cost  #
                existing_stock.purchase_price = round(total_cost / total_shares, 2)
                existing_stock.shares = total_shares
                existing_stock.current_price = today_price
                # so buying more of a stock you already hold also fixes a stale/NaN
                # current_price on that existing position, not just brand-new ones

                match = True

                print(f"added {shares} more shares of {ticker} - new avg cost £{existing_stock.purchase_price}")
                break

        if not match :
             new_stocks = Stock(ticker , shares , purchase_price , current_price = today_price)
             self.stocks.append(new_stocks)
             print(f"{ticker} added succesfully")



        self.cash -= cost
        # this just - the cash amount from the cost
        # lets say you had 1000 in you cash and the cost was 500

        portfolio_data = [stock.to_dict() for stock in self.stocks]
        #  every method within the stock object what this does it to converts this into dictiona

        """
        
        so you might have had this below 
        
        [Stock <ticker , purchase>]
        this then only looks at the ticker and coverts this into its dictionary form of "tickr": ticker
        
        """


        self.data.save_price(portfolio_data , self.cash)


    def remove_stock(self,ticker , shares): 

        found = False

        # mathing stack is just going to be stock objects found
        # remember that self.stocks is a list of stock objects containing the data

        
        for matching_stack in self.stocks: #  matching_stack is just a stock object that is 
            # found within the self.stocks list  Stock <Ticker , shares , purchase_price , current_price>
            # it would check for all of these stock objects and see whether 
            # the ticker that you are trying to sell matches any of the stock objects within the self.stocks list
            if ticker.upper() == matching_stack.ticker.upper(): 

                if shares > matching_stack.shares:
                    print(f"you only have {matching_stack.shares} shares of {ticker}")
                    return
                # checks whether tne ticker that you are trying to access is the same as the one found in the 
                # Stock object within the self.stocks list
               
                # updated the current price of the stock object to the live price that was fetched from the API
                cash_received = matching_stack.current_price * matching_stack.shares 
               
                self.cash += cash_received
                print(self.cash)
                remaining__shares = matching_stack.shares - shares
                matching_stack.shares = remaining__shares # update the number of shares remaining
               
                found = True
                break


        if found :
            portfolio_data = [stock.to_dict() for stock in self.stocks]
            self.data.save_price(portfolio_data , self.cash)
            print(f"{ticker} succesfully sold")
        else :
            print(f"{ticker} not found in portfolio")



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
            # converts the stock object into a dictionary 
            # Stock<ticker , shares , purchase_price , current_price>  into a dictionary form of {"ticker" : ticker , "shares": shares , "purchase_price" : purchase_price , "current_price" : current_price}
            dataframe_table = pd.DataFrame(table) 
            # transfporms the list of dictionaries into a pandas dataframe
            print(dataframe_table)
            # prints the pandas dataframe into a table format



            fig, ax = plt.subplots(figsize=(12, 4))
            ax.axis("off")
            plt.table( cellText=dataframe_table.values ,colLabels=dataframe_table.columns , loc="center")
            plt.savefig("portfolio.png")
            plt.show()



        print("---------Portfolio-----------")


        TOTAL_NET_WORTH = round(self.total_portfolio_value() + self.cash, 2)


        print(f" this is the total portfolio value : ${self.total_portfolio_value()}")
        print(f" cash : {self.cash:.2f}")
        print(f"total networth : {TOTAL_NET_WORTH}")


# -------------------------------   Helper function ---------------------------------

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












