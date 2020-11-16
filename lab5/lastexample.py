psw = str(input('password: '))
password = 'abc123'
while  psw != password :
  print('wrong password')

if psw == 'help' :
  print(psw[0])

elif psw == True :
  print('welcome')