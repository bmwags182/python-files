# python-files
Python files I've written to simplify some of my daily tasks

openLinks:
This was created to go through an excel workbook/sheet and open links within the sheet. Eventually linkchecker-gui was created for others to be able to use the script in the office

Opening links manually in order to confirm that they are working was tedious and time consuming, and sometimes even perfectly good working links did not work from within excel due to limitations within it.

This program does require the openpyxl module

It also requires that the spreadsheet you are going through be in the same folder.

Upon starting the program will ask which workbook you are using where you will then enter the filename of the spreadsheet

Once the spreadsheet has been opened it will give you a list of the sheets available in the workbook and allow you to enter which sheet you want to run through.

By default it only searches columns a-z and rows 2-100, this can be changed at line 47

Also after reaching two empty rows it will stop searching, if you need to allow for more empty rows you can change the value at line 60

Once completed the program opens all links in your default browser and tells you how many tabs should have been opened.

linkchecker-gui:
This was built off the origial openLinks file which was console/terminal based and others tend to be afraid of the console so I worked towards building them something with buttons to click which not only made it easier for them to use, but reduced the amount of time I spent showing them how to make it work.

This one will allow you to choose any workbook anywhere on your computer through use of a browse button. This meant users in my office were able to save their workbooks in the same place they always did, and leave a shortcut to this script on their desktop for easy access when they needed it.

ipchecker:
This simple program will do exactly what it says, and then some.

Originally written because my router did not cooperate with dyndns, and I need to know my IP address when I am out and about sometimes.

Before running you will need to install the pip module ipgetter, as well as go into the file and set the values of the variables from lines 25-35

Once that is completed you can run this and it will begin checking your ip address. On first run you should get an email with your current IP address as well as two new files in the directory called iplog.txt and ipaddress.txt

These will be updated as the script runs, it will check your IP once an hour and send you an email if it changes from one hour to the next. you can change the amount of wait time in lines 88 and 95
