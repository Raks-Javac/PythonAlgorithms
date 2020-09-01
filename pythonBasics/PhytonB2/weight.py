weight = float(input("weight : "))
conversion = input(" (L)bs or (K)g : ")

if conversion == "L" or conversion == "l":
    print(f"You are {weight * 0.435} lbs ")
elif conversion == "K" or conversion == "k":
    print(f" You are {weight* 1000} kg ")
else: 
    print(f"input a valid conversion")