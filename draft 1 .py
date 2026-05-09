#timer logic
import time
class FocusTimer:
    def __init__ (self,min):
        self.time_left =  min * 60
        self.is_running = False

    def start_countdown(self):
        self.is_running = True
        while self.time_left >= 0:
            min, sec = divmod(self.time_left, 60)
            print(f"Time remaining: {min:02d}:{sec:02d}")
            
            time.sleep(1)
            self.time_left -= 1
        
        self.is_running = False
        print("Time's up! Great job focusing.")
#asking user for the activity they wish to do
class ActivityChoice:
    def __init__ (self,activity_choice):
        self.activity_choice = activity_choice
    def status(self):
        if self.activity_choice == "timer":
            user_choice = int(input("How many minutes? "))
            my_timer = FocusTimer(user_choice)
            my_timer.start_countdown()
        else:
            print("test")

activity = input("What do you want to do?:\n")
my_choice = ActivityChoice(activity)
my_choice.status()