import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import re


def main():
    """This will be the core of the project"""

    stock = get_stock()
    customized_data = customizer(stock)
    export_data(customized_data)
    print_graph(customized_data, stock.info["shortName"])

def get_stock() -> yf.Ticker: #Used try/except
    """Checks if the given stock symbol is valid, then return that ticker object,
    else the user will be reprompted until above statement is satisfied
    """
    
    print("----------------------------------------")
    while True:
        name = input("Please enter a stock Ticker symbol(MSFT, AAPL, etc): ")
        stock = yf.Ticker(name)
        try:
            stock.info['currentPrice']
            print("----------------------------------------")
            print()
            return stock
        except KeyError:
            print("--Invalid symbol--")
            print("----------------------------------------")

def get_file_name() -> str : #Used regular expression
    """Get a valid csv or excel file"""

    print("Choose the format to be downloaded:")
    print("1: csv")
    print("2: excel")

    #User picks which file type
    while True:
        user_choice = input("Enter a number: ")
        if user_choice == "1":
            to_csv = True
            break
        if user_choice == "2":
            to_csv = False
            break
        print("--Invalid response--")

    #User picks name for file
    while True:
        file_type = "excel"
        if to_csv == True:
            file_type = "csv"
        name = input(f"Enter a name for the {file_type} file: ")

        if to_csv == True:
            if re.search("^\w+(\.csv)?$", name):
                if ".csv" not in name:
                    name = name + ".csv"
                return name
        else:
            if re.search("^\w+(\.xlsx)?$", name):
                if ".xlsx" not in name:
                    name = name + ".xlsx"
                return name
        
        print("Invalid file name")

def customizer(stock: yf.Ticker) -> pd.DataFrame: #Used try/except
    """This function customizes how the data is collected"""
    
    periods = ["1 day", "5 days", "1 month", "3 months", "6 months", "1 year", "5 years", "max"]
    periods_translator = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "5y", "max"] #Translate into yf terms
    intervals = [
        ["1m", "5m", "15m", "30m", "1h"], # 1 day
        ["1m", "5m", "15m", "30m", "1h"], # 5 days
        ["5m", "15m", "30m", "1h", "1d"], # 1 month 
        ["1h", "1d", "1wk", "1mo"],       # 3 months
        ["1h", "1d", "1wk", "1mo"],       # 6 months
        ["1h", "1d", "1wk", "1mo"],       # 1 years
        ["1d", "1wk", "1mo"],             # 5 years
        ["1d", "1wk", "1mo"]              # max
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
           print("--Your number is not between 1 and 8--")
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

def export_data(file: pd.DataFrame) -> None: #Using pandas to export data
    """Exports the data into a csv or xlsx file"""

    file_name = get_file_name()

    #Download csv file, else excel
    if ".csv" in file_name:
        file.to_csv(file_name)
    else:
        file.index = file.index.tz_localize(None) # Localizes the time to be timezone unaware
        file.to_excel(file_name)
    print("File downloaded in current directory")

def print_graph(file: pd.DataFrame, name: str) -> None:
    """Prints a graph with range chosen by user, interval is per day"""
    
    plt.plot(file.index, file["Close"])
    plt.title(f"{name} Stock Performance")
    plt.xlabel("Date")
    plt.ylabel("Closing price ($)")
    plt.grid(True)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
