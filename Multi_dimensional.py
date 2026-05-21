temps = [[0.0 for h in range(24)] for d in range(31)]
temp1 = 30
temp2 = 32
count = 0
for days in temps:
    if count == 0:
        days[11] = temp1
        count = 1
    else:
        days[11] = temp2
        count = 0
for element in temps:
        print(element)
total = 0.0
for days in temps:
        total += days[11]
average = total / 31
print("Average temperature:", average)