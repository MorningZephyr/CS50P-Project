import yfinance as yf
import pandas as pd
import re


def main():
    """This will be the core of the project"""
    
    stock = get_stock()
    customized_data = customizer(stock)
    export_data(customized_data)

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
            print("--Invalid 4 digit symbol--")
            print("----------------------------------------")


def get_file_name() -> str : #Used regular expression
    """Get a valid csv file"""
    
    while True:
        name = input("Please enter a name for the  csv file: ")

        if re.search("^\w+(\.csv)?$", name):
            if ".csv" not in name:
                name = name + ".csv"
            return name
        
        print("Invalid file name")

def customizer(stock: yf.Ticker) -> pd.DataFrame: #Used try/except
    """This function customizes how the data is collected"""
    
    periods = ["1 day", "5 days", "1 month", "3 months", "6 months", "1 year", "5 years", "max"]
    periods_translator = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "5y", "max"] #Translate into yf terms
    intervals = [
        ["1m", "2m", "5m", "15m", "30m", "1h"], # 1 day
        ["1m", "2m", "5m", "15m", "30m", "1h"], # 5 days
        ["2m", "5m", "15m", "30m", "1h"],       # 1 month 
        ["1h", "1d", "5d", "1wk", "1mo"],       # 3 months
        ["1h", "1d", "5d", "1wk", "1mo"],       # 6 months
        ["1h", "1d", "5d", "1wk", "1mo"],       # 1 years
        ["1d", "5d", "1wk", "1mo"],             # 5 years
        ["1d", "5d", "1wk", "1mo"]              # max
            ]

    #Prints the available periods
    print("Select the period of data you want:")
    for i in range(len(periods)):
        print(f"{i+1}:", periods[i])

    #Picks a valid period choice
    while True:
        try:
            period_choice = int(input("Enter a number: ")) -1   #Important variable
            if period_choice < 0 or period_choice >= len(periods):
                raise IndexError
            break

        except IndexError:
            print("--Your number is not between 1 and 9--")
        except ValueError:
            print("--You inputted a non numeric value--")
    
    #Prints the valid time intervals based on period choice
    print("Choose your time intervals: ")
    for i in range(len(intervals[period_choice])):
        print(f"{i+1}:", intervals[period_choice][i])

    #Picks a valid time interval based on period choice
    while True:
        try:
            interval_choice = int(input("Enter a number: ")) -1 #Important variable
            if interval_choice < 0 or interval_choice >= len(intervals[period_choice]):
                raise IndexError
            break

        except IndexError:
            print(f"--Your number is not between 1 and {len(intervals[period_choice])}--")
        except ValueError:
            print("--You inputted a non numeric value--")

    return stock.history(interval=intervals[period_choice][interval_choice], period=periods_translator[period_choice])

def export_data(file: pd.DataFrame) -> str: #Using pandas to export data
    """Exports the data into a csv file"""
    
    file.to_csv(get_file_name())
    print("File downloaded in current directory")

if __name__ == "__main__":
    main()
