import matplotlib.pyplot as plt
import numpy as np

punkter = []

with open(r"C:\Users\jacob\Kod_vscode\Labb2\datapoints.txt") as file:
    next(file)
    for rad in file:
        w, h, l = rad.strip().split(",")
        punkt = float(w),float(h),int(l)
        
        punkter.append(punkt)

def euclidean(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    return np.sqrt(dx*dx + dy*dy) 

print("Give me the width and height in cm of your unknown yellow Pokemon and i will tell you what it is:")


def get_userinput(prompt):
    while True:
        try:
            info = float(input(prompt))
            if info <= 0:
                print("Please enter a positive number for width!\n")
                continue
            break
        except ValueError:
            print("You must enter a number!\n")
    return info

while True:
    w = get_userinput("Width: ")
    h = get_userinput("Height: ")

    print(f"You entered width={w} cm, height={h} cm")
    confirm = input("Is this correct? (y/n): ").strip().lower()

    if confirm == "y":
        break
    else:
        print("Okay, lets try again!")

print(f"Final values: width= {w} cm, height= {h} cm")
userinput = (w,h)

nn10_list = []

# Making a list with the 10 NN sorting and always removes the biggest distance
for wtrain , htrain , label in punkter:
    dist = euclidean(userinput,(wtrain,htrain))
    if len(nn10_list) < 10:
        nn10_list.append((dist,label))
        nn10_list.sort(key=lambda x: x[0])
    
    else:
         if dist < nn10_list[-1][0]:
            nn10_list[-1] = (dist, label)
            nn10_list.sort(key=lambda x: x[0]) 
            

pichucount = 0
pikachucount = 0

for _, label in nn10_list:
    if label == 0:
        pichucount +=1
    else:
        pikachucount+=1

if pikachucount < pichucount:
    print("Your yellow little thing is a Pichu")
elif pikachucount > pichucount:
    print("Your yellow little thing is a Pikachu")
else:
    print("Its a tie between Pichu and Pikachu")
    if label in nn10_list[0] == 0:
        print("But the nearest neighbur is a Pichu")
    else:
        print("But the nearest neighbur is a Pikachu")
    
## kan lÄgga in så att man får nÄrmaste grannen i nn10_list som förslag

#Fixa så att dist inte lÄggs till i nn10_list, det enda du behöver Är label dÄr! 
#Har svårt att förstå vad rad 69-72 gör. Kanske förtydliga med kommentar!