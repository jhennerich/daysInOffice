import os
import csv
import calendar
import holidays
from datetime import date
import tkinter as tk
from tkinter import *
from tkinter import ttk
import sv_ttk
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename

from PIL.ImageOps import expand
from tkcalendar import Calendar

def cal_time(year,month):
    months = []
    for i in range(1, 13):
        months.append(calendar.month_name[i])
    return calendar.month(year, month)

def get_working_days(year, month):
    us_holidays = holidays.US()
    working_days = []
    cal = calendar.Calendar()

    for day in cal.itermonthdays2(year, month):
        if day[0] != 0 and day[1] < 5:  # 0 is day of month, 1 is weekday (0-6, Mon-Sun)
            day_to_check = str(month) +'/' + str(day[0]) + '/' + str(year)
            if day_to_check not in us_holidays:
                working_days.append(day[0])
    return working_days

def min_days_in_office(working_days):
    if (len(working_days) % 2):
       min_days = str((len(working_days) + 1) / 2)
    else:
       min_days = str(len(working_days) /2)
    return min_days

def save_to_file():
    file1 = asksaveasfile(initialfile='Untitled.txt',
                          defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    #    file1 = open('./users.txt', "w")
    """
    for user in users:
        file1.writelines(f'{user.uid}, {user.user_name}, {user.email}, {user.create_time}\n')
    """
    file1.close()


def open_file():
    filename = askopenfilename( defaultextension=".csv", filetypes=[("All Files", "*.*"), ("CSV Documents", "*.csv")])
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        content = ""
        for row in csv_reader:
            content += ",".join(row) + "\n"
"""            
    text1 = open(filename, 'r')
    for line in text1:
        line_array = line.split(',')
    text1.close()
"""

def grad_date():
    date.config(text="Selected Date is: " + cal.get_date(),font="Arial 24")

def insert_text(event):
    text_box.insert("1.0",cal.get_date())

if __name__ == '__main__':

    runtime_date = date.today()
#    print(cal_time(runtime_date.year,runtime_date.month))

    working_days = get_working_days(runtime_date.year, runtime_date.month)
    print('Min days in office needed= ', min_days_in_office(working_days))


    root = tk.Tk()
    root.geometry("900x900")
    root.maxsize(900, 900)
    root.title("Days In Office Tracker")
    root.config(bg="light grey")

    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=open_file)
    filemenu.add_command(label="Save", command=save_to_file)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    left_frame = Frame(root, width=500, height=500)
#    left_frame = Frame(root)
    left_frame.grid(row=0, column=0, padx=10, pady=5)

#    right_frame = Frame(root, width=900, height=400)
#    right_frame = Frame(root)
#    right_frame.grid(row=1, column=0, padx=10, pady=5)

#    cal = Calendar(left_frame,font="Arial 24", selectmode='day', year=runtime_date.year, month=runtime_date.month, day=runtime_date.day)
    cal = Calendar(left_frame, showothermonthdays=False, font="Arial 24", selectmode='day', year=runtime_date.year, month=runtime_date.month, day=runtime_date.day)
    cal.pack(side=TOP, expand=True)
    cal.calevent_create(date(2025,1,1), "New Years", 'holiday')
    cal.calevent_create(date(2025,2,17), "Presidents Day", 'holiday')
    #calevent_create('1/1/2025', "New Years", tags=[])
    cal.tag_config('holiday', background='red', foreground='red')

    # Add Button and Label
    Button(left_frame, text="Get Date", command=grad_date).pack(pady=20)

    date = Label(left_frame, text="")
    date.pack(side=TOP, pady=20)

    text_box = tk.Text(left_frame, height=2, width=30, font="Arial 24")
    text_box.pack(side=BOTTOM, expand=True)

    cal.bind("<<CalendarSelected>>", insert_text)
    # Inserting text
#    text_box.insert("1.0",  'Min days in office needed= ' + min_days_in_office(working_days))
#    text_box.insert("1.0", cal.get_date())

    #    display_button = Button(left_frame, text="Display Users", command=lambda: min_days_in_office(working_days), height=2, bg="dark grey")
#    display_button.pack(pady=2, expand=True, side=LEFT)

#    button = ttk.Button(root, text="Click me!")
#    button.pack()

    root.config(menu=menubar)

#    sv_ttk.set_theme("dark")
    root.mainloop()