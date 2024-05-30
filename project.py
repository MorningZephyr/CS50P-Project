import yfinance as yf
import pandas as pd
import re


def main():
    """This will be the core of the project"""

    stock = get_stock()
    print(stock)
    


def get_stock() -> yf.Ticker:
    """Checks if the given stock symbol is valid, then return that ticker object,
    else the user will be reprompted until above statement is satisfied
    """
    
    print("----------------------------------------")
    while True:
        name = input("Please enter a 4-digit stock symbol: ")
        stock = yf.Ticker(name)
        try:
            stock.info['currentPrice']
            print()
            return stock
        except KeyError:
            print("Invalid 4 digit symbol. Please try again")
            print("----------------------------------------")





if __name__ == "__main__":
    main()
