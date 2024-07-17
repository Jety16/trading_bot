from stock import Stock

def show_main_menu():
    print("Welcome to the Trade Bot. \n")
    print("0. Check specific Stock.")
    print("1. Get all your Stock Data. ")
    print("Anything else. Exit")
    
    while True:
        try:
            return int(input(">> "))
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_specific_stock():
    stock_symbol = input("Enter the stock symbol you want to check: ").upper()
    stock = Stock(id=stock_symbol, name=stock_symbol)
    stock.update_stock()

def get_stocks():
    stock_symbols = input("Enter the stock symbols you want to check, separated by commas: ").upper().split(',')
    for symbol in stock_symbols:
        stock = Stock(id=symbol.strip(), name=symbol.strip())
        stock.update_stock()

run = True
while run:
    user_input = show_main_menu()

    if user_input == 0:
        check_specific_stock()
    elif user_input == 1:
        get_stocks()
    else:
        run = False
