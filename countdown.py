import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  #calculating minutes and seconds
        time_format = '{:02d}: {:02d}'.format(mins, secs)  #MM:SS format
        print(time_format, end= '\r')
        time.sleep(1)    #delay
        seconds -= 1
    print("00:00 \n Times Up!")

#User input for Timer
total_seconds = int(input("Enter time in seconds for Countdown:"))
countdown_timer(total_seconds)
