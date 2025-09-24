import matplotlib.pyplot as plt
import numpy as np

punkter = []

with open(r"C:\Users\jacob\Kod_vscode\Labb2\datapoints.txt") as file:
    next(file)
    for rad in file:
        w, h, l = rad.strip().split(",")
        punkt = float(w),float(h),int(l)
        
        punkter.append(punkt)
    
        
    

#def graf():
    # pichu_x = []
    # pichu_y = []
    # pikachu_x = []
    # pikachu_y = []

    # for w, h, l in punkter:
    #     if l == 0: # 0 = pichu
    #         pichu_x.append(w)
    #         pichu_y.append(h)

    #     else:
    #         pikachu_x.append(w)
    #         pikachu_y.append(h)

    # plt.scatter(pichu_x, pichu_y, c= "red", label="Pichu")
    # plt.scatter(pikachu_x, pikachu_y, c= "blue", label= "Pikachu")


    # plt.xlabel("Width ")
    # plt.ylabel("Height ")



# testpoints = []

# with open(r"C:\Users\jacob\Kod_vscode\Labb2\testpoints.txt") as file:
    # next(file)
    # for rad in file:
    #     start = rad.find("(")
    #     end = rad.find(")")
    #     cords_text = rad[start+1:end]

    #     w_text, h_text = cords_text.split(",")

    #     w = float(w_text)  #string till float
    #     h = float(h_text)

    #     testpoints.append((w,h))



def euclidean(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    return np.sqrt(dx*dx + dy*dy)

print("Give me the width and height of your unknown yellow Pokemon and I'll tell you what it is:")


def get_userinput():
    while True:
        try:
            w = float(input("width: "))
            if w <= 0:
                print("Please enter a positive number for width!\n")
                continue
            break
        except ValueError:
            print("You must enter a number!\n")

    while True:
        try:
            h = float(input("height: "))
            if h <= 0:
                print("Please enter a positive number for height!\n")
                continue
            break
        except ValueError:
            print("You must enter a number!\n")

    return w, h


while True:
    w, h = get_userinput()
    print(f"You entered width={w}, height={h}")
    confirm = input("Is this correct? (y/n): ").strip().lower()

    if confirm == "y":
        break
    else:
        print("Okay, lets try again!")

print(f"Final values: width= {w}, height= {h}")
userinput = (w,h)



min_dist = 10000
nearest_label = None

for wtrain , htrain , label in punkter:
    dist = euclidean(userinput,(wtrain,htrain))
    if dist < min_dist:
        min_dist=dist
        nearest_label = label

nn10_list = []

for wtrain , htrain , label in punkter:
    dist = euclidean(userinput,(wtrain,htrain))
    if nn10_list < [9]:
        nn10_list.append(dist,label)

print(nn10_list)
# for wtrain, htrain, label in punkter:
#     dist = euclidean(userinput,(wtrain, htrain))
#     if dist < 10 nearest neighburs ad to 10nn_list
#     if 10_nn list < index[9] add to list

#     min_dist = 10nn_ist[9]
def psudo():
    # Skapa en tom lista 10nn_list

    # För varje träningspunkt (w_train, h_train, label) i punkter:
    #     beräkna dist = euclidean(userinput, (w_train, h_train))

    #     om 10nn_list har färre än 10 element:
    #         lägg till (dist, label) i 10nn_list
    #         sortera listan på dist

    #     annars om dist < största dist i 10nn_list:
    #         byt ut den med störst dist mot (dist, label)
    #         sortera listan på dist

    # När loopen är klar:
    #     räkna hur många av de 10 närmaste har label 0 (Pichu) och label 1 (Pikachu)
    #     om flest är 0 → klassificera som Pichu
    #     annars → klassificera som Pikachu





# if nearest_label == 0:
#     print("It is a Pichu!")
# else:
#     print("It is a Pikachu!")    











# min_dist = float("inf")
# nearest_label = None

# for testpunkt in testpoints:
#     min_dist = float("inf")
#     nearest_label = None
    
#     for w, h , label in punkter:
#         dist = euclidean(testpunkt , (w,h))

#         if dist < min_dist:
#             min_dist= dist
#             nearest_label = label

#     if nearest_label == 0:
#         print(testpunkt, "Pichu")
#     else:
#         print(testpunkt, "Pikachu")













# test_x, test_y = zip(*testpoints)  # packar upp tuplerna till två listor
# plt.scatter(test_x, test_y, c="green", marker="x", label="Testpoints")
# plt.legend()
# plt.show()