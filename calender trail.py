#importing all nessasary libraries
import datetime
import calendar
import customtkinter
import json

#making the window
Calendar = customtkinter.CTk()
Calendar.title("Calender")
Calendar.geometry("400x300")

#labling the months
month_label = customtkinter.CTkLabel(Calendar, text="June 2026", font=("Arial", 20))
month_label.grid(row=0, column=0, columnspan=7, pady=10)

# Day headers
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for column, day in enumerate(days):
    customtkinter.CTkLabel(Calendar, text=day).grid(row=1, padx=5)

Calendar.mainloop()