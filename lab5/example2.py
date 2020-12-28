#lab5 ex2
n = int(input('How many numbers? : '))
a = []
while n > 0 :
    n = n - 1
    l = int(input('enter an integer: '))
    if l % 2 == 0 :
        a.append(0)
    else:
        l == 1
        a.append(1)

print(f"{(a.count(0)) / (len(a)) * 100} % ")
