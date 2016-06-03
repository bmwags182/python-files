try:
    from Tkinter import *
    import ttk
    import webbrowser
    import openpyxl
    import time
    import tkFileDialog

except:
    print("""You have not installed everything properly yet.
          You will need to have Bret install some python modules
          before you can use this program.""")

class MainWindow(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        file_entry = ttk.Entry(parent, width=50, textvariable=file)
        file_entry.grid(column=1, row=2, sticky=W)
        browse_button = ttk.Button(parent, text="Browse...", command=tkFileDialog.askopenfilename)
        browse_button.grid(column=1, row = 3, sticky=E)
        file_entry.delete(0, END)
        file_entry.insert(0,tkFileDialog.askopenfilename())
        label = ttk.Label(parent, text="Import file: ")
        label.grid(column=1, row=1, sticky="S,W")
        check_button = ttk.Button(parent, text="Check File", command=check)
        check_button.grid(column=1, row=4, sticky=S)

class ClientList(ttk.Frame):
    def __init__(self, parent, clients = []):
        ttk.Frame.__init__(self, parent)
        self.vars = []
        row_count = 1
        column_count = 1
        for client in clients:
            var = Int()
            chk = ttk.Checkbutton(self, text=client, variable=var)
            chk.pack(column=coulumn_count, row=row_count)
            column_count += 1
            if column_count % 4 == 0:
                row_count += 1
                column_count = 1

        row_count += 1
        check_button = ttk.Button(parent, text="Check Links", command=check_links)
        check_button.grid(column=2, row=row_count, sticky=S)

def check_links():
    print("Checking Links Now")

def browse():
    print("testing browse button")
    file = tkFileDialog.askopenfilename()
    root.file_entry.delete(0, END)
    root.file_entry.insert(0, file)

def check():
    print("Check file test")


if __name__ == "__main__":
    root = Tk()
    root.title("Choose a file")
    MainWindow(root)
    file = " "
    root.mainloop()
