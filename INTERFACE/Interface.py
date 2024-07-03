# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'Gpu database.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()


menu_choice = ''
while menu_choice != 'Z':
    menu_choice = input('This is a database for GPUS, and we have some premade view for you!\n\n'
                        'Type the letter for the information you desire:\n'
                        'A: Model, Clock speed, VRAM, and price of all $900 or cheaper GPUS\n'
                        'B: Make, model, VRAM, Wattage, Clock Speed and Release date of all Non-Intel 1500 MHz GPUS\n'
                        "C: Everything on RTX-30's and RTX-40's or Intel GPUS\n"
                        'D: Make, Series, Model, Price, VRAM, and Clock speed of all AMD 2000 MHz GPUS\n'
                        "E: Everything of GPUS within a $500-$1000 range and producing less than 90 C\n"
                        "F: Make, model, wattage, clock speed, and price of all GPUS with 16GB of VRAM\n"
                        "G: Make, Series, Model, price, and release date of all GPUS with 1800 MHz\n"
                        "Z: Exit\n\nType option here: ")
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('Cheapest gpus')
    elif menu_choice == 'B':
        print_query('High end non-intel')
    elif menu_choice == 'C':
        print_query('Intel/RTX 30 40')
    elif menu_choice == 'D':
        print_query('AMD and 2000')    
    elif menu_choice == 'E':
        print_query('($500 - $1000) + 90 C')
    elif menu_choice == 'F':
        print_query('16GB vRAM')
    elif menu_choice == 'G':
        print_query('1800 MHz')
    elif menu_choice == 'z':
        print("Initiating detonation seqeunce")