

from Portfolio import Portfolio

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
            print("this is not correct")
            continue

        match choices :
            case 1 :
                ticker = input("provide the stock ticker").upper().strip()

                if  not ticker.isalpha() :
                    print("this is incorrect")
                    continue

                purchase_price = portfolio.data.fetch_price(ticker)

                if purchase_price is None:
                    print("there is no data")
                    continue

                print(f"current price of {ticker} : {purchase_price}")




                try :
                    share_amount = int(input("how many shares do you want"))
                except ValueError:
                    print("this has to be a number")
                    continue

                portfolio.add_stock(ticker , share_amount, purchase_price)



            case 2:

                portfolio.list_tickers()
                remove_stock = input("which stock would you like to remove").upper().strip()

                portfolio.remove_stock(remove_stock)
            case 3:
                portfolio.refresh_stock()
            case 4:
                portfolio.display()
            case 5:
                print("thank you for using this have a nice day")
                break








if __name__ == '__main__':
    main()

