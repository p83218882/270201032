age = int(input('age: '))

if  (0 < age < 6)  or (age > 60):
  print('Ticket price is free')

elif (6 <= age < 18) :
  print('Ticket price is 1.5 TL')

else:
  print('Ticket price is 3.0 TL')