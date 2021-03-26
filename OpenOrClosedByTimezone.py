# This project takes in three different timezones from pytz and run a conditional statement to see if it is between 9 and 17 (military time)



import datetime
from pytz import timezone
from datetime import time 


tUTC = datetime.datetime.now(datetime.timezone.utc)
LT = timezone('Europe/London')
NYC = timezone('America/New_York')
PT = timezone('America/Los_Angeles') 
tNYC = tUTC.astimezone(NYC)
tPT = tUTC.astimezone(PT)
tLT = tUTC.astimezone(LT)
now = datetime.datetime.now()
Open = datetime.datetime(year= 1, month= 1, day = 1, hour=9, minute=0, second=0)
Close = datetime.datetime(year= 1, month= 1, day = 1, hour=17, minute=0, second=0)
nT = (int(tNYC.strftime("%H")))
pT = (int(tPT.strftime("%H")))
lT = (int(tLT.strftime("%H")))
C = (int(Close.strftime("%H")))
O = (int(Open.strftime("%H")))
print(O, C, lT, pT, nT)


if nT >= O and nT <= C:
    print("Yes, this is open")
else:
    print("No, this is not open")

if pT >= O and pT <= C:
    print("Yes, this is open")
else:
    print("No, this is not open")

if lT >= O and lT <= C:
    print("Yes, this is open")
else:
    print("No, this is not open")

