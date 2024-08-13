import project
import yfinance as yf


def test_get_stock():
    #Remember to use pytest -s test_project.py in terminal

    print()
    print("***  Entering \"MSFT\" (Case insensitive) is right answer for this test case, any other is wrong ***")
    print()
    assert project.get_stock().ticker == "MSFT"


def test_get_file_name():
    #Remember to use pytest -s test_project.py in terminal

    #Testing csv
    print()
    print("***  Choose option 1 and enter \"a\"   ***")
    print()
    assert project.get_file_name() == "a.csv"

    #Testing xlsx
    print()
    print("***  Choose option 2 and enter \"a\" ***")
    print()
    assert project.get_file_name() == "a.xlsx"

    #Testing nonalphanumeric 
    print()
    print("***  Choose option 1 and enter any non-alphanumeric strings; enter \"a\" to pass ***")
    print()
    assert project.get_file_name() == "a.csv"

def test_customizer():
    #Remember to use pytest -s test_project.py in terminal

    print()
    print("***  Entering 1 then 1 will pass the test, any other given numbers will fail ***")
    print("***  You can enter any numbers that's out of range or any characters to test edge cases  ***")
    print()
    assert project.customizer(yf.Ticker("MSFT")).equals(yf.Ticker("MSFT").history(interval="1m", period="1d")) == True

    


