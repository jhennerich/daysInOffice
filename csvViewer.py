import tkinter as tk
from tkinter import filedialog
import csv
import os


class CSVViewer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.open_csv_on_launch()

    def create_widgets(self):
        self.text_area = tk.Text(self)
        self.text_area.pack(fill="both", expand=True)

    def open_csv_on_launch(self):

        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select CSV file",
                                              filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
        if filename:
            self.load_csv(filename)

    def load_csv(self, filename):
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            content = ""
            for row in csv_reader:
                content += ",".join(row) + "\n"


root = tk.Tk()
root.geometry("600x400")
app = CSVViewer(root)
root.mainloop()