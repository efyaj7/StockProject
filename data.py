

import  json
import requests
import yfinance


""""
Setup

Create the class DataManager
Define __init__ with these attributes:

filename — the name of the JSON file to save to e.g. "portfolio.json"
api_key — your Alpha Vantage API key stored as an attribute




Method 1 — save(portfolio)

Takes the portfolio data as an argument
Opens the JSON file in write mode
Converts the portfolio data to JSON and writes it
Wrap in try/except for IOError


Method 2 — load()

Opens the JSON file in read mode
Reads and parses the JSON back into Python
Returns the data
Wrap in try/except for FileNotFoundError and json.JSONDecodeError
If file doesn't exist — return an empty list


Method 3 — fetch_price(ticker)

Takes a stock ticker as argument e.g. "AAPL"
Builds the API URL using the ticker and api_key
Makes a GET request using requests.get()
Parses the JSON response
Extracts and returns the current price
Wrap in try/except for network errors



"""


class DataManager :

    def __init__(self ,filename = "portfolio.json" ):
        self.filename = filename
        self.api_key = "CA919FAR8VTFO7CL"



    def save_price(self , portfolio , cash):

        try :
            with open (self.filename , "w") as f :
                json.dump({"portfolio":portfolio ,"cash" : cash}, f , indent= 4 , sort_keys= True)
        except IOError:
            return "this file is not found"


    def load(self ):
        try :
            with open(self.filename , "r") as f :
                data = json.load(f)


                return data["cash"] , data["portfolio"]
        except FileNotFoundError :
            return 0,[]
    def fetch_price(self , stock_ticker):
        try :
            stock = yfinance.Ticker(stock_ticker)
            specific_price  = stock.history(period="1d").iloc[-1]
            # remember iloc is used in pandas to find the index
            # this represents the table of values today


            # now as dataframes are similar to dictionaries you would access the same way
            # as a key value pair

            prices = round(float(specific_price["Close"]),2)

            return prices
        except (IndexError , Exception) :
            print(f"Error fetching price for {stock_ticker}")
            return None

    def fetch_historical_price(self , stock_ticker):
        try:

            stock = yfinance.Ticker(stock_ticker)
            specific_price = stock.history(period="3d").iloc[0]
            # this represents the d table of values today

            # now as dataframes are similar to dictionaries you would access the same way
            # as a key value pair

            prices = round(float(specific_price["Close"]) , 2)

            return prices
        except (IndexError, Exception):
            print(f"Error fetching price for {stock_ticker}")
            return None





"""""
Now your next steps:
Step 1 — Create fetch_historical_price() method

Same structure as fetch_price()
But instead of period="1d" — fetch a specific date range covering a few days back
Return the closing price from a few days ago as the purchase price

Step 2 — Update add_stock() in Portfolio

Remove purchase_price as a parameter
Call self.data.fetch_historical_price(ticker, 3) internally instead
Use the returned price as purchase_price

Step 3 — Update main.py Case 1

Remove the manual price fetch and display
Just ask for ticker and shares
Let add_stock() handle everything internally

"""