month= input("month:")
day = int(input("day:"))

if month=="june" or "august" and 1<=day<=31 and month=="july" and 1<=day<=30 :
  season= "Summer"
elif month=="march"or "may" and 1<=day<=30 and month=="april" and 1<=day<=31 :
  season="Spring"
elif month=="december" and 1<=day<=31 and month=="february" or "january" and 1<=day<=30:
  season  ="Winter"
elif month=="september" or "november" and 1<=day<=30 and month=="october" and 1<=day<=30:
  season ="Autumn"

print(season)