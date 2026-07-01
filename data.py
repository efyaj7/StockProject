

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
            url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_ticker}&apikey={self.api_key}"

            responce = requests.get(url)
            data = responce.json()

            price = float(data["Global Quote"]["05. price"])

            return price
        except (requests.exceptions.RequestException, KeyError) :
            print(f"Error fetching price for {stock_ticker}")
            return None







