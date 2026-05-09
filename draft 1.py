import time

#trial 1 to display time
current_time_Human_format = time.strftime("%H:%m")
print(f"Current time:\n{current_time_Human_format}")

#trial 2 for countdown
# 1500 sec in 25 min
min,sec = divmod(1500,60)
print(f"{min:02d}:{sec:02d}")