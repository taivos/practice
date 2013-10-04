def Dict():
  d = {"pi":3.141592653589,"e":2.718281828459,"y":0.577215664901,
  "k":0.915965594177,"a": 1.2824271291006}
  x = raw_input("Enter your constant,precision: ")
  r = x.split(",")
  c = r[0]
  p = int(r[1])
  print (c,"=",round(d[c],p))
Dict()