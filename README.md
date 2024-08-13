# Stock Price Collector
#### Video Demo:  <URL HERE>
#### Description:
    This project is a stock price collector, built around of a library called yfinance. After a user enters a stock ticker symbol, they have the options to select how far back the data should include, as well as the time intervals between each stock price data. The data will then to downloaded to the current directory at which this code resides, and a graph will also be generated. The following breaks down each of the functions in the project:

    get_stock(): This function prompts the user for a stock ticker symbol; such as MSFT (Microsoft), AAPL (Apple), and AMZN (Amazon); and returns a yfinance.Ticker object, which will be used later for data collection. The function uses a try and except method to ensure that the user enters a valid symbol. To see if a given symbol is invalid, it is observed that a KeyError will be raised when invoking ticker_object.info['currentPrice'] for invalid yfinance.Ticker objects. The code will catch that error when encountered and prompt the user to re-enter.

    get_file_name(): This function gets a valid file name for the data file to be exported. First, the user will be given the choices between 1. csv or 2. xlsl format. To ensure that the user selects between the two choice, conditional statements and while loops are set to ensure valid input. Next is the file name, which can only contain alphanumerical characters. Regular expression and while loops were used to help with this task. The user has the option to enter the file extension (.csv or .xlsx), so the regular expression took that into consideration. However, the file extension must match the format chosen in the beginning of the function, or else it'll be invalid, and the user will have to re-enter the file name. 

    customizer(stock: yf.Ticker): This function allows user to configurate how far back and at what time interval the stock prices should be collected. yfinance.Ticker object has a .history() method which fetchs past stock prices, and 2 parameters of that method that are used are interval and period.



