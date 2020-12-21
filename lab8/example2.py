# lab8 ex2 
def is_prime(number):
    isprimen = True

    if (number == 1):
        isprimen = False

    for i in range(2,number):
        if (number % i == 0):
            isprimen = False
            break

    if isprimen:
        print(f"{number} is prime number.")
    else:
        print(f"{number} is not prime number.")

k = int(input("enter a number >>> "))
is_prime(k)


def print_primes_between(a,b):


  for number in range(a+1,b):
      if number > 1:
          for i in range(2,number):
              if number % i == 0:
                  print(f"{number} is not prime")
                  break
          else:
              print(f"{number} is prime ")
                
a = int(input("enter number1 >>> "))
b = int(input("enter number2 >>> "))
print_primes_between(a,b)