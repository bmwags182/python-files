from Tkinter import *
import tkFileDialog
import ttk
import openpyxl
import time
import webbrowser


"""
once you select file refresh the window to get sheets
checkboxes for sheets, each sheet should get it's own new window in browser
"""

def browse():
    print("testing browse button")
    file = tkFileDialog.askopenfilename()
    file_entry.delete(0, END)
    file_entry.insert(0, file)
    print file
    return file


def check():
    # print("checking file")
    file = file_entry.get()
    # print(file)
    workbook = openpyxl.load_workbook(file)
    # print(workbook)
    sheets = workbook.get_sheet_names()
    # print(sheets)
    # sheets_list = ttk.Label(mainframe, text=sheets)
    # sheets_list.grid(column=1, row=4)
    sheet_window = Tk()
    sheet_window.title("Client List")
    sheetframe = ttk.Frame(sheet_window, padding="10 10 10 10")
    sheetframe.grid(column=0, row=0, sticky="N,W,E,S")
    sheetframe.columnconfigure(0, weight=1)
    sheetframe.rowconfigure(0, weight=1)
    window.destroy()
    row_count = 1
    column_count = 1
    clients = dict()
    var = 0
    for sheet in sheets:
        sheet = ttk.Checkbutton(sheetframe,
                                text=sheet,
                                variable = var)
        sheet.grid(column=column_count, row=row_count, sticky="N,W,E")
        column_count = column_count + 1
        if column_count % 4 == 0:
            row_count = row_count + 1
            column_count = 1

        # print(sheet)
    row_count = row_count + 2
    check_button = ttk.Button(sheetframe, text="Check Links", command=check_links)
    check_button.grid(column=2, row=row_count, sticky=S)

def check_links():
    print("Checking links now...")


def openlink():
    print("Opening links")


#def main():
window = Tk()
window.title("Link Checker")
window.geometry("420x75+150+150")
mainframe = ttk.Frame(window, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
# main_window = Window("MAin Window")

file = " "
file_entry = ttk.Entry(mainframe, width=50, textvariable=file)
browse_button = ttk.Button(mainframe, text="Browse...", command=browse)
browse_button.grid(column=1, row = 2, sticky=E)
label = ttk.Label(mainframe, text="Import file: ")
label.grid(column=1, row=1, sticky="S,W")
file_entry.grid(column=1, row=2, sticky=W)
check_button = ttk.Button(mainframe, text="Check File", command=check)
check_button.grid(column=1, row=3, sticky=S)

window.mainloop()


# main()
