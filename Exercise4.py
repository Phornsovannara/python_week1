# input 1 to n ,Formula sum = (n)(n+1)/2
num = input("Plase enter the number of integer : ")
sum_num = (int(num)*(int(num)+1))/2
if(int(num)>0):
    sum_number = f"sum 1 to {num} = {sum_num}"
    print(sum_number)
else:
    print(num+" This is nethve number \n please enter thepositive number")