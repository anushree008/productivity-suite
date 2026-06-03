#importing all nessasary libraries
import datetime
import calendar
import customtkinter
import json

#making the window
Calendar = customtkinter.CTk()
Calendar.title("Calender")
Calendar.geometry("400x300")

#defining months and year
current_month = 6
current_year = 2026

#defing the frame
calendar_frame = customtkinter.CTkFrame(Calendar)
calendar_frame.grid(row=2, column=0, columnspan=7)

#defining prev_month and next_month
def update_calendar():
    # destroy all old day buttons
    for widget in calendar_frame.winfo_children():
        widget.destroy()
    # then redraw with new month/year

def prev_month():
    global current_month, current_year
    current_month -= 1
    if current_month == 0:
        current_month = 12
        current_year -= 1
    update_calendar()

def next_month():
    global current_month, current_year
    current_month += 1
    if current_month == 0:
        current_month = 12
        current_year += 1

#changing month view
prev_button = customtkinter.CTkButton(Calendar, text="<", width=30, command=prev_month)
prev_button.grid(row=0, column=0)

next_button = customtkinter.CTkButton(Calendar, text=">", width=30, command=next_month)
next_button.grid(row=0, column=6)

#labling the months and year
month_label = customtkinter.CTkLabel(Calendar, text="June 2026", font=("Arial", 20))
month_label.grid(row=0, column=0, columnspan=7, pady=10)

# Day headers
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for column, day in enumerate(days):
    customtkinter.CTkLabel(Calendar, text=day).grid(row=1, column=column, padx=5)#always pass the variables in the .grid

# Date buttons
month_days = calendar.monthcalendar(current_year, current_month)  # returns a grid of weeks
for row_num, week in enumerate(month_days):
    for column_num, day in enumerate(week):
        if day == 0:  # 0 means no day (empty cell)
            customtkinter.CTkLabel(Calendar, text="").grid(row=row_num+2, column=column_num)#always pass the variables in the .grid
        else:
            customtkinter.CTkButton(Calendar, text=str(day), width=40, height=40).grid(row=row_num+2, column=column_num, padx=2, pady=2)#always pass the variables in the .grid

Calendar.mainloop()