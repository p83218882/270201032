# lab8 ex4.1
def binary_to_dec(a):
    k = 0
    a = str(a)
    for i in range(len(a)):
       k += int(a[-len(a) + i])*(2**(len(a)-i-1))
    print(f"{a}'s binary to decimal demonstrated state is\n{k}")

a = str(input("enter binary number >>> "))
binary_to_dec(a)
# lab8 ex4.2


def dec_to_binary(a):
    c = ""
    while a >= 1 :
        c = c + str(a % 2)
        a = a // 2
    print(f"{k}'s decimal to binary demonstrated state is\n{c[::-1]}")
k = int(input("enter decimal number >>> "))
dec_to_binary(k)