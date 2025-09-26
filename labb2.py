import numpy as np

punkter = []

with open(r"datapoints.txt") as file:
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
                print(f"Please enter a positive number for {prompt}!\n")
                continue
            break
        except ValueError:
            print("You must enter a number!\n")
    return info

while True:
    w = get_userinput("Width: ")
    h = get_userinput("Height: ")

    print(f"You entered width= {w} cm, height= {h} cm")
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
        nn10_list.sort(key=lambda x: x[0]) #sorting on distance
    
    else:
         if dist < nn10_list[-1][0]: #Comparing distance in last element of list
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
    nearest_label = nn10_list[0][1] # Collecting the label in the first element 
    if nearest_label == 0:
        print("But the nearest neighbor is a Pichu")
    else:
        print("But the nearest neighbor is a Pikachu")