#importing all nessasary libraries
import datetime
import calendar
import customtkinter
import json

#making the window
Calendar = customtkinter.CTk()
Calendar.title("Calender")
Calendar.geometry("400x300")


button = customtkinter.CTkButton(Calendar, text="Click me")
button.pack()

Calendar.mainloop()