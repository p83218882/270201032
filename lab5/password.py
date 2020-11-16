psw = str(input('password: '))
password = 'abc123'
i = 0
while i < float("inf") :
    i+=1   

    if psw == password :
        print('welcome')
        break

    elif psw == 'help' :
        print(password[0])
        break
       
    elif psw!= password and psw != 'help' :
    
            print('wrong, try again ')
            psw = str(input('password: '))