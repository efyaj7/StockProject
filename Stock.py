"""""
Method 1 — calculate_profit_loss()

Uses self.current_price, self.purchase_price and self.shares
Formula: (current_price - purchase_price) × shares
Returns the profit or loss as a float
If current_price is None — return None — price hasn't been fetched yet


Method 2 — calculate_percentage()

Calculates the percentage gain or loss
Formula: ((current_price - purchase_price) / purchase_price) × 100
Returns the percentage rounded to 2 decimal places
If current_price is None — return None


Method 3 — total_value()

Calculates the total current value of this stock holding
Formula: current_price × shares
Returns the total value
If current_price is None — return None


Method 4 — to_dict()

Converts the stock object into a dictionary
This is needed for saving to JSON — you can't save objects directly to JSON but you can save dictionaries
Returns a dictionary with all the stock's attributes


Method 5 — display()

Prints a neat summary of the stock
Shows ticker, shares, purchase price, current price, profit/loss and percentage
Format it clearly like:





"""



class Stock:

    def __init__(self , ticker , shares, purchase_price , current_price = None)  :
        self.ticker = ticker
        self.shares = shares
        self.purcahse_price = purchase_price

        self.current_price = current_price


    def calculate_profit_loss(self):
        # (current_price - purchase_price) × shares

        if self.current_price is None :
            return None
        calc = float((self.current_price - self.purcahse_price ) * self.shares)

        return calc
    def calculate_percentage(self) :

        if self.current_price is None:

            # return essentially brwaks out of the function so no code after that point is executed
            return None

        return round(((self.current_price - self.purcahse_price) / self.purcahse_price) * 100 , 2)
    def total_value(self):

        if self.current_price is None:
            return None

        return self.current_price * self.shares

    def to_dict(self) :
        data = {"ticker" : self.ticker , "shares": self.shares , "purchase_price" : self.purcahse_price , "current_price" : self.current_price}
        return data

    def display(self):

        if self.current_price is None:
            print("there is no data for this")
            return
        print(f"Ticker :{self.ticker}")
        print(f"Current Price :{self.current_price}")
        print(f"Shares :{self.shares}")
        print(f"Purchase Price {self.purcahse_price}")
        print(f"Percentage : {self.calculate_percentage()}")
        profit = self.calculate_profit_loss()

        if profit > 0:
            print(f"Profit Gain :+{profit}")
        else:
            print(f"Profit Loss : {profit}")
        print(f"Total Value : {self.total_value()}")






