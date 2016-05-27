# python-files
Python files I've written to simplify some of my daily tasks

openLinks:
This was created to go through an excel workbook/sheet and open links within the sheet. 
Opening links manually in order to confirm that they are working was tedious and time consuming, and sometimes even perfectly good working links did not work from within excel due to limitations within it.

This program does require the openpyxl module 
It also requires that the spreadsheet you are going through be in the same folder.

Upon starting the program will ask which workbook you are using where you will then enter the filename of the spreadsheet

Once the spreadsheet has been opened it will give you a list of the sheets available in the workbook and allow you to enter which sheet you want to run through.

By default it only searches columns a-z and rows 2-100, this can be changed at line 47

Also after reaching two empty rows it will stop searching, if you need to allow for more empty rows you can change the value at line 60

Once completed the program opens all links in your default browser and tells you how many tabs should have been opened.
