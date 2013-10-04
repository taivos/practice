def Year():
  x = raw_input("Enter year you want to know:")
  x = int(x)
  if x%400 == 0:
    print ("Yes")
  else:
    if x%100 == 0:
      print ("No")
    else:
      if x%4 == 0:
        print ("Yes")
      else:
        print ("No")
Year()