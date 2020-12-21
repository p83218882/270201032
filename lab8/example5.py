#lab8 exercise 5
numbers = ('0','1','2','3','4','5','6','7','8','9')
symbols = ('`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|',':',';','"',"'",'<',",",'>','.','?','/')
alph = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","V","X","Y","Z")


def password_level_checker(a):
 a = str(a)
 if " " in  a  or len(str(a)) < 8:
    print("level 0")
 elif " " not in a and len(str(a)) >= 8 :
    c = 0 
    for i in a:
        if i in numbers:
            c = c + 1
            break
    else:
        c = c + 0

    for i in a :
        if i in symbols:
            c = c + 1
            break
    else:
         c = c + 0

    for i in a:
        if i in alph:
            c = c + 1
            break
    else:
        c = c + 0

    print(f"level {c}")
j = str(input("enter a password to check >>>\n"))
password_level_checker(j)