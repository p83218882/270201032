a  = float(input("ax^2's a: "))
b  = float(input("bx's b: "))
c  = float(input("cx's c: "))

if ((b**2) - 4*a*c < 0) :
  print('there are two complex roots')

elif ((b**2) - 4*a*c > 0) :
  print('there are two real roots')

else:
  print('there is one real root')
