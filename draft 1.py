import time

#trial 1 to display time
current_time_Human_format = time.strftime("%H:%m")
print(f"Current time:\n{current_time_Human_format}")

#trial 2 for countdown
# 1500 sec in 25 min
min,sec = divmod(1500,60)
print(f"{min:02d}:{sec:02d}")

#trail 3 changing countdown 
#total seconds
time_left = 10 
for i in range(time_left):
    #recalculate min/sec from the total time left
    mins, secs = divmod(time_left, 60)
    print(f"{mins:02d}:{secs:02d}")
    #wait and then subtract from the total
    time.sleep(1)
    time_left -= 1 
print("00:00")