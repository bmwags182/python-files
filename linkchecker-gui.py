try:
    from Tkinter import *
    import ttk
    import webbrowser
    import openpyxl
    import time
    import tkFileDialog
    import tkFont


except:
    print("""You have not installed everything properly yet.
          You will need to have Bret install some python modules
          before you can use this program.""")


class MainWindow(ttk.Frame):
    def __init__(self, parent,file):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.label = ttk.Label(parent, width=30,
        text=" ")
        self.label.grid(column=1, row=3, sticky="W,E")
        browse_button = ttk.Button(parent, text="Browse...", command=browse)
        browse_button.grid(column=1, row = 4, sticky=S)

        # file_entry.insert(0,tkFileDialog.askopenfilename())
        self.file = file
        label = ttk.Label(parent, text="Click the browse button below to select your link spreadsheet")
        label.grid(column=1, row=2, sticky="S,W")
        label2 = ttk.Label(parent, text=" ")
        label2.grid(column=1, row=1, sticky="W,E")
        empty_space = ttk.Label(parent, text=" ")
        empty_space.grid(column=1, row=5)

        # check_button = ttk.Button(parent, text="Check File", command=check)
        # check_button.grid(column=1, row=4, sticky=S)

class ClientList(ttk.Frame):
    def __init__(self, parent, clients):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        # self.vars = []
        self.clients = clients[0]
        file = clients[1]
        # print(file)
        # print("print file above")
        row_count = 1
        column_count = 1
        for client in self.clients:
            # print(client)
            # print(file)
            client_button = ttk.Button(parent, text=client,
            command=lambda client=client:openLink(client, file))
            client_button.grid(column=column_count, row=row_count, sticky="W,E")
            column_count += 1
            if column_count % 4 == 0:
                row_count += 1
                column_count = 1





def openLink(client, file):
    # print(client)
    # print(file)
    wb = openpyxl.load_workbook(file)
    sheet = wb.get_sheet_by_name(client)
    count = 0
    empty_row = 0
    for row in sheet.iter_rows('A2:Z40'):
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
                        print("Opening " + str(count) + " links now")
                        # quit()
def browse():
    # print("testing browse button")
    file = tkFileDialog.askopenfilename()
    # print(file)
    # file_entry = ttk.Entry(root, width=50, textvariable=file)
    # MainWindow.file = file
    clients = check(file)
    client_list = Tk()
    # print(clients)
    # print(file)
    root.destroy()
    client_list.title("Client List")
    ClientList(client_list, clients=clients)
    client_list.mainloop()


    # MainWindow.root.file_entry.delete(0, END)
    # MainWindow.file_entry.insert(0, file)

def check(file):
    # print("Check file test")
    clients = []
    workbook = openpyxl.load_workbook(file)
    sheets = workbook.get_sheet_names()
    for client in sheets:
        # print(client)
        clients.append(client)
        # print(clients)

    return clients, file

if __name__ == "__main__":
    root = Tk()
    root.title("Choose a file")
    file_entry = ttk.Entry(master=None, width=50, textvariable=file)
    MainWindow(root, file)
    file = " "
    root.mainloop()
