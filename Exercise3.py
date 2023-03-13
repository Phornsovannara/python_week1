# Area of a field
print("Area of a field")
print("Choose one : feet or meters")
print("1.feet \n2.meters")
Ch = input("Plase input your number :")
Choose =int(Ch)
if(Choose == 2):
    width = input("plase enter the width of the room(m) : ")
    hength = input("plase enter the hength of the room(m) : ")
    #100 squsre meters in an acre 
    area_field = (float(width)*float(hength))/100
    print(str(area_field)+" acre ")

elif(Choose == 1):
    width = input("plase enter the width of the room(feet) : ")
    hength = input("plase enter the hength of the room(feet) : ")
    #43560 squsre feet in an acre  
    area_field = (float(width)*float(hength))/43560
    field = round(area_field, 2)
    print(str(field)+" acres ")
else:
    print("plese enter number 1 or number 2 ")