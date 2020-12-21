# lab8 ex3
def get_rand_list(b,e,N):

    import random

    l = list(range(b,e+1))

    a =  set(random.sample(l, N))
    b =  set(random.sample(l, N))
    print("Calculating\n","----------------------")
    print(f"{list(a)} -> list a ")
    print(f"{list(b)} -> list b ")

def get_overlap(b,e,N):
    import random
    l = list(range(b,e+1))  

    a =  set(random.sample(l, N))
    b =  set(random.sample(l, N))
    print(f"{a.intersection(b)} is a intersection b")
        
get_rand_list(1,10,5)

get_overlap(1,10,5)

