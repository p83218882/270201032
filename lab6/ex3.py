province_with_coordinates = dict()

txt = open("provinces.txt")

lines = txt.readline()

while lines != "":
   province_name = lines.split(",")[0]
   province_coordinates = lines.split(",")[1] , lines.split(",")[2]
   province_with_coordinates[province_name] = province_coordinates
   lines = txt.readline()

txt.close()

Departure_province = input("Departure province:\n")

Departure_province = Departure_province.upper()

i = 0

while i == 0 :
    if Departure_province == province_with_coordinates.keys():
     break
    elif Departure_province not in province_with_coordinates.keys():
        print("Province not found!")
        possible_province = []
        for i in province_with_coordinates.keys():
            if Departure_province == i[:len(Departure_province)]:
             possible_province.append(i)
        
        if len(possible_province)!=0:
            if len(possible_province) == 1 :
                print("Possible province:" + ",".join(possible_province))
            elif len(possible_province)> 1:
                possible_province.sort()
                print("Possible provinces:"+",".join(possible_province))

        Departure_province = input("Departure province:\n")


Arrival_province = input("Arrival province:\n")
Arrival_province = Arrival_province.upper()

while i==0:
    if Arrival_province == province_with_coordinates.keys():
        break
    elif Arrival_province not in province_with_coordinates.keys():
        print("Province not found!")
        possible_province = []
        for i in province_with_coordinates.keys():
            if Arrival_province == i[:len(Arrival_province)]:
             possible_province.append(i)
        
        if len(possible_province) != 0:
            if len(possible_province) == 1 :
                print("Possible province:" + ",".join(possible_province))
            elif len(possible_province)> 1:
                possible_province.sort()
                print("Possible provinces:"+",".join(possible_province))
    elif  Arrival_province.upper() == Departure_province.upper():
        print("Enter a different province!")

    Arrival_province = input("Arrival province:\n")

travel_type_list = ["CAR","BICYCLE","MOTORCYCLE"]
travel_type = input("Enter travel type:\n")



while travel_type.upper() not in travel_type_list :
    travel_type = input("Enter travel type:\n")




print("\nI am calculating the distance between", Departure_province.upper(), "and", Arrival_province, "...\n")
#dx = x2 - x1
#dy = y2 - y1 
dx = province_with_coordinates[Arrival_province.upper()][0] - province_with_coordinates[Departure_province.upper()][0]
dy = province_with_coordinates[Arrival_province.upper()][1] - province_with_coordinates[Departure_province.upper()][1]

distance = (dx**2 + dy**2)**(1/2)

distance_km = distance*100

distance_for_output = round(distance_km, 2)

if travel_type.upper() == "CAR":
    time = distance_km/90
elif travel_type.upper() == "MOTORCYCLE":
    time = distance_km/80
elif travel_type.upper() == "BICYCLE":
    time = distance_km/25

time_hours = int(time)
time_minutes = int((time-time_hours)*60)

for i in province_with_coordinates.keys():
    rec_place_dx = province_with_coordinates[i][0] - provinces_locations[Departure_province.upper()][0]
    rec_place_dy = province_with_coordinates[i][1] - provinces_locations[Departure_province.upper()][1]
    rec_place_distance = distance = ((rec_place_dx*rec_place_dx)+(rec_place_dy*rec_place_dy))**(1/2)
    recommended_places[i] = rec_place_distance
    if i.keys() == 0 :
        recommended_places.pop(i)

closest_recs = []

while len(closest_recs) < 3 :
     closest_rec_places.append(recommended_places[min(recommended_places)])
     del recommended_places[min(recommended_places)]
    


closest_recs.sort()
print("Distance:", distance_for_output, "km")