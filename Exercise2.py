# Area room
print("Area room")
print("Choose one : feet or meters")
print("1.feet \n2.meters")
Ch = input("Plase input your number :")
Choose =int(Ch)
if(Choose == 2):
    width = input("plase enter the width of the room(m) : ")
    hength = input("plase enter the hength of the room(m) : ")
    area_room = float(width)*float(hength)
    print(str(area_room)+" m^2 ")

elif(Choose == 1):
    width = input("plase enter the width of the room(feet) : ")
    hength = input("plase enter the hength of the room(feet) : ")
    area_room = float(width)*float(hength)
    print(str(area_room)+" feet^2 ")
else:
    print("plese enter number 1 or number 2 ")
