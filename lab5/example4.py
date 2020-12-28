#lab 5 ex4
psw = "abc123"
a = input('write: ')

while  psw !=a :
    if a =='help':
        print(psw[0])
        a = input('write: ')  
    else :
        print('wrong')
        a = input('write: ')
while psw ==a :
    print('welcome')
    break