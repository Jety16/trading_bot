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
    pass

def get_stocks():
    pass


run = True
while run:
    user_input = show_main_menu()

    if user_input == 0:
        check_specific_stock()
    elif user_input < 2:
        get_stocks()
    else:
        run = False
