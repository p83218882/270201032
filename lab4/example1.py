if 0 <= a < 10:
  print(a)

elif a == 10:
  print(1)

elif  10 < a <= 99 :
  print((a % 10) + ((a - (a % 10)) / 10))

elif a >= 100:
  print((a % 10) + ((a - a % 10)  / 10) % 10)  