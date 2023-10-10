import time

minutes = int (inout("Enter the number of minutes to focus")
seconds = minutes * 60

while Seconds:
  mins,secs = divmod(seconds,60)
  timer = '{:02d}:{:02d}'.format(mins,secs)
  print(timer,end="\r")
  time,sleep(1)
  seconds -= 1

  print("Time's up!")
