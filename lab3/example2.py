num1 = int(input('num1: '))
num2 = int(input('num2: '))
num3 = int(input('num3: '))

if num1 < num2 and num1 < num3 :
  print(f"{num1} is the smallest")

elif num2 < num3 and num2 < num1 :
  print(f"{num2} is the smallest")

elif num3 < num2 and num3 < num1 :
  print(f"{num3} is the smallest")
