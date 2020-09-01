sequence = [3,4,3,3,2,2]
min = sequence[1]

for seque in sequence:
    if seque < min:
        min = seque
print(min)


for seque in sequence:
    if seque > min:
        min = seque
print(min)