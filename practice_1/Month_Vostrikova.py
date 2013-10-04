def Month():
  d = {"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,
  "july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
  x = raw_input("Enter month (in low register): ")
  if d.has_key(x) == True:
    print ("Number of month: ", d[x])
  else:
    print ("You entered wrong month, please try again")
Month()