
from datetime import datetime
from time import *



times = "2020-01-14 16:01:20" # String Data
time1 = datetime.strptime(times,"%Y-%m-%d %H:%M:%S") # Change to DateTime
print(time1)
print("*****")
sleep(3)

time2 = datetime.now() # waited a few minutes before pressing enter
print(time2)
dft = time2 - time1
print("*****")
print(dft)

showtiem = dft.seconds/3600  # one minus in second 60 x 60 
hourss = dft.seconds//3600
secondElse = dft.seconds%3600
minuss = secondElse//60
print(showtiem)
print(minuss)
dayss = dft.days


print(f"show day --->{dayss}")
print(f"show hour ---> {hourss}")
print(f"show minus --->{minuss}")
