#importing all nessasary libraries
import datetime
import calendar
import customtkinter
import json

#making the window
Calendar = customtkinter.CTk()
Calendar.title("Calender")
Calendar.geometry("400x300")

#labling the months and year
month_label = customtkinter.CTkLabel(Calendar, text="June 2026", font=("Arial", 20))
month_label.grid(row=0, column=0, columnspan=7, pady=10)

# Day headers
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for column, day in enumerate(days):
    customtkinter.CTkLabel(Calendar, text=day).grid(row=1, column=column, padx=5)#always pass the variables in the .grid

# Date buttons
month_days = calendar.monthcalendar(2026, 6)  # returns a grid of weeks
for row_num, week in enumerate(month_days):
    for column_num, day in enumerate(week):
        if day == 0:  # 0 means no day (empty cell)
            customtkinter.CTkLabel(Calendar, text="").grid(row=row_num+2, column=column_num)#always pass the variables in the .grid
        else:
            customtkinter.CTkButton(Calendar, text=str(day), width=40, height=40).grid(row=row_num+2, column=column_num, padx=2, pady=2)#always pass the variables in the .grid

Calendar.mainloop()