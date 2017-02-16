"""
@title:         Fibonacci Finder
@author:        Bret Wagner
@version:       0.1.0

===Description===
I like numbers and wanted to see if I could write something to go through
the fibbonacci sequence. I decided that I wanted to find the 'n'th number
in the squence. This will open a window with an entry box, enter an integer
and the program will tell you what number is in that spot.
"""

import Tkinter as tk
import locale

locale.setlocale(locale.LC_ALL, '')

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.text = tk.Label(self, text="""
            Find the nth number in the fibonacci sequence""")
        self.text.grid(column=0, row=0, sticky="W")
        self.entry = tk.Entry(self)
        self.entry.grid(column=1, row=0, stick="E")
        self.submit = tk.Button(self, text="Find", command=self.get_number)
        self.submit.grid(column=1, row=1, sticky="E")
        tk.Label(self, text="", width="5").grid(column=2, row=0, sticky="E")
        self.spacer = tk.Label(self, text="", width="20")
        self.spacer.grid(column=0, row=2, sticky="S")
        self.resultlabel = tk.Label(self, text="")
        self.resultlabel.grid(column=0,row=3,columnspan=2)

    def get_number(self):
        number = self.entry.get()
        try:
            if (int(number) > 0 and int(number) != 1):
                i = 1
                first = 0
                second = 1
                result = 0
                while (i <= (int(number) - 1)):
                    result = first + second
                    first = second
                    second = result
                    i = i + 1
            elif (int(number) <= 0):
                result = """
                There are no negative digits in the fibonacci sequence"""

            elif (int(number) == 1):
                result = 1
            self.display_result(result, number)
        except:
            self.clear_result()
            result = "The number entered was actually a string"
            tk.Label(self,
                     text="You didn't enter an integer").grid(column=0,
                                                              columnspan=2,
                                                              row=3,
                                                              sticky="S")

    def display_result(self, result, number):
        self.clear_result()
        number = str(locale.format("%d", int(number), grouping=True))
        result = locale.format("%d", result, grouping=True)
        self.resultlabel.config(text="The " + number + get_suffix(number) +
                                " number of the fibonacci squence is " +
                                str(result))
        self.resultlabel.grid(column=0, row=3, sticky="S", columnspan=2)
        print(result)


    def clear_result(self):
        self.resultlabel.config(text="")


def get_suffix(number):
    if number[(len(number) - 1)] == "1" and (10 > int(number) or int(number) > 14):
        return "st"
    elif number[(len(number) - 1)] == "2" and (10 > int(number) or int(number) > 14):
        return "nd"
    elif number[(len(number) - 1)] == "3" and (10 > int(number) or int(number) > 14):
        return "rd"
    else:
        return "th"


app = MainWindow()
app.title("Fibonacci Finder")
app.mainloop()
