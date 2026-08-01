

import re

from Portfolio import Portfolio

TICKER_PATTERN = re.compile(r"^\^?[A-Z]+([.-][A-Z]+)?$")
# allows an optional leading ^ for indices (e.g. ^GSPC) and an optional
# .LETTERS or -LETTERS suffix for share classes (e.g. BRK.B) or crypto pairs (e.g. BTC-USD)

def main():

    portfolio = Portfolio() 



    while True:

        try :

            choices = int(input("1. Add Stock\n "
                  "2. Sell Stock\n"
                  "3. Refresh price\n"
                  "4. View Portfolio\n"
                  "5. Exit"))
        except ValueError :
            print("this is not a valid choice please choose a number between 1 and 5")
            continue

        match choices :
            case 1 :

                try : 
                    ticker = input("provide the stock ticker").upper().strip()

                    if not TICKER_PATTERN.match(ticker) :
                        print("this is not a valid ticker")
                        continue
                except ValueError :
                    print("the ticker has to be a string")
                    continue

                purchase_price = portfolio.data.fetch_historical_price(ticker)
                # this fetches the data from 3 days ago and returns the closing price of that day

                if purchase_price is None: 
                    # if the purchase price is None then that means that the stock ticker is invalid and there is no data for it
                    print("there is no data")
                    # prints out a message to the user that there is no data for the stock ticker       

                    continue
                    # the continue skips the next step ad goes back to the start of the while loop so that 
                    # the user can try again with a different stock ticker 

                print(f"current price of {ticker} : {purchase_price}")




                try :
                    share_amount = int(input("how many shares do you want"))
                except ValueError:
                    print("this has to be a number")
                    continue

                portfolio.add_stock(ticker , share_amount)

            case 2:

                portfolio.list_tickers()

                
                try :
                    remove_stock = input("which stock would you like to remove").upper().strip()
                except ValueError:
                    print("this has to be a string")
                    continue


                try :
                    num_of_shares = int(input("how many shares would you like to sell").strip())
                except ValueError:
                    print("this has to be a number")
                    continue


                # this is going to be the number of shares that the user wants to sell from the stock that 
                # they want to remove

                

                portfolio.remove_stock(remove_stock , num_of_shares)
            case 3:
                portfolio.refresh_stock()
            case 4:
                portfolio.display()

            case 5:
                print("thank you for using this have a nice day")
                break

            case _:
                print("this is not a valid choice please choose a number between 1 and 5")
                continue








if __name__ == '__main__':
    main()

