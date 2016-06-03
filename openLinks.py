import webbrowser
import re
import os
import time
try:
    import openpyxl

except:
    print("""There was an error importing required modules.
          If this is your first run, please run the command
          'pip install openpyxl' in order to get things working.""")
    exit()

def clear():
    try:
        os.name
        if os.name == 'nt':
            # windows systems
            try:
                os.system('cls')

                # print("User is running Windows")
            except:
                print("error trying to clear the console")

        else:
            os.system('clear')

            # print("User is running Unix")

    except:
        print("error checking operating system")


def main():
    clear()
    workbook = raw_input("""Which workbook are you using?
Please enter the full filename with extension
(xlsm/xlsx)\n""")
    wb = openpyxl.load_workbook(workbook)
    clear()
    sheets = wb.get_sheet_names()
    for sheet in sheets:
        print(sheet + '\n')

    sheet = raw_input("""Which client are you working on? Enter the
                      Client name as seen above \n""")
    sheet = wb.get_sheet_by_name(sheet)
    clear()
    count = 0
    empty_row = 0
    for row in sheet.iter_rows('A2:Z100'):
        time.sleep(3)
        empty_cell = 0
        for cell in row:
            if str(cell.value).startswith('http'):
                webbrowser.open(cell.value)
                count = count + 1
                empty_cell = 0
            if not cell.value:
                empty_cell = empty_cell + 1
                if empty_cell == 26:
                    empty_row = empty_row + 1
                    print("Empty Row " + str(empty_row))
                    if empty_row > 1:
                        clear()
                        print("Opening " + str(count) + " links now")
                        exit()


main()
