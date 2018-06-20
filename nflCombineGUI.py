from tkinter import Tk, Label, Button
#!/usr/bin/python
import os


class combineGUI:
    def __init__(self, master):
        self.master = master
        master.title("NFL Combine Data")

        self.label = Label(master, text="This is a program that takes data from NFLCombineResults.com and puts it in an Excel spreadsheet.\n" + 
        "Please make sure that you have a working internet connection and have Microsoft Excel installed.\n" +
        "Click \"Run\" to generate spreadsheet of NFL Combine Data.\n")
        self.label.pack()

        self.run_button = Button(master, text="Run", command=self.run)
        self.run_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def run(self):
        os.system('NFLCombineWebScraper.py')

        
root = Tk()
my_gui = combineGUI(root)
root.mainloop()