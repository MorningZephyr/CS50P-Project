import yfinance as yf
import pandas as pd
import re


def main():
    """This will be the core of the project"""
    stock = get_stock()
    export_data(stock.income_stmt, get_file_name())



def get_stock() -> yf.Ticker: #Used try/except
    """Checks if the given stock symbol is valid, then return that ticker object,
    else the user will be reprompted until above statement is satisfied
    """

    print("----------------------------------------")
    while True:
        name = input("Please enter a 4-digit stock symbol: ")
        stock = yf.Ticker(name)
        try:
            stock.info['currentPrice']
            print("----------------------------------------")
            print()
            return stock
        except KeyError:
            print("Invalid 4 digit symbol")
            print("----------------------------------------")


def get_file_name() -> str : #Used regular expression
    """Get a valid csv file"""
    while True:
        name = input("Please enter a name for the  csv file: ")

        if match := re.search("^\w+(\.csv)?$", name):
            if ".csv" not in name:
                name = name + ".csv"
            return name
        print("Invalid file name")

def export_data(file: pd.DataFrame):
    """Exports the data into a csv file"""
    file.to_csv(get_file_name())


if __name__ == "__main__":
    main()
