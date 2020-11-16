

x = 412 # 6 hour + 52 minutes = 412 minutes



tempo1 = int(input("tempo1:"))
tempo1_time = 8*tempo1
tempo2  = int(input("tempo2: "))
tempo2_time =6*tempo2
y = tempo1_time + tempo2_time


t = y + 412

p = t//60
q = t%60

print(str(p) + ":" + str(q))



