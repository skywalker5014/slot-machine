#slot machine project

import random

#global constant 
MAX_LINES = 3
MAX_BET =  100
MIN_BET = 1
#number of rows and columns in our slot machine
ROWS = 3
COLS = 3

symbol_count ={    # a dictionary representing the symbol value and its frequency
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8

}

symbol_value ={    # a dictionary representing the symbol value and its frequency
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2

}


def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line+1)
    return winnings, winning_lines




def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []    #empty list
    for symbol, symbol_count in symbols.items(): #parsing a dictionary
        for _ in range(symbol_count):              # '_' is an anoynemous variable in python, when
            all_symbols.append(symbol)             #  we dont care about loop count we can use it 


    columns = []   #nested list
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # "[:]" represnts to only copy the list not reference it
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns



def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):   #enumerate returns both values and its position in the list 
            if i != len(columns) - 1:
                print(column[row], end=" | ")  # usually end = \n i.e ends with a line break  
            else:                               # here end = | ends the line with "|"
                print(column[row], end=" ")

        print() # empty print statement for skipping to next line for the next iteration of the loop






#defining a function called deposit
def deposit():
    while True: #keep looping until the condition is true
        amount = input("What would you like to deposit? ")
        #making sure amount is a number
        if amount.isdigit():
            amount = int(amount)  # convert the amount number into integer form 
            if amount > 0:
                break       #if amount is greater than 0 then break out of the loop and go to last 
            else:           # instruction , here it is "return amount"
                print("amount must be grater than 0.")
        else:
            print("Please enter a number.")  # if the amount is not a number print this message

    return amount

# a function to define the number of lines the user wants to bet on 
def get_number_of_lines():
    while True:
        lines = input("enter the number if lines to bet on(1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter a valid number of lines.")
        else:
            print("please enter a numebr.")
    return lines
          


def get_bet():
    while True: #keep looping until the condition is true
        amount = input("what would you like to bet on each line?  ")
            #making sure amount is a number
        if amount.isdigit():
            amount = int(amount)  # convert the amount number into integer form 
            if MIN_BET<= amount <= MAX_BET:
                break       #if amount is greater than 0 then break out of the loop and go to last 
            else:           # instruction , here it is "return amount"
                    print(f"amount must be between {MIN_BET} - {MAX_BET}.")
        else:
                print("Please enter a number.")  # if the amount is not a number print this message

    return amount 


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"yo do not have the enough to bet that amount, your current balance is {balance}")
        else:
            break
    
    
    print(f"you are bettng {bet} on {lines} llines. Total bet is equal to : {total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won {winnings}.")
    print(f"you won on lines: ", *winning_lines)  # * is called splat operator or unpack operator

    return winnings - total_bet



def main():
#calling all the functions defined
    balance = deposit()
    while True:
        print(f"current balance is {balance}")
        answer = input("press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"you left with {balance}")



main()


