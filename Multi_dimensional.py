# temps = [[0.0 for h in range(24)] for d in range(31)]
# temp1 = 30
# temp2 = 32
# count = 0
# for days in temps:
#     if count == 0:
#         days[11] = temp1
#         count = 1
#     else:
#        days[11] = temp2
#        count = 0
# for element in temps:   
#     print(element)
# total = 0.0
# for days in temps:
#        total += days[11]
# average = total / 31
# print("Average temperature:", average)




# temps = [[0.0 for h in range(24)] for d in range(31)]
# temp1 = 19
# temp2 = 32
# count = 0
# for days in temps:
#     if count == 0:
#         days[11] = temp1
#         count = 1
#     else:
#        days[11] = temp2
#        count = 0
# for element in temps:   
#     print(element)
# total = 0.0
# for days in temps:
#        total += days[11]
# average = total / 31
# print("Average temperature:", average)

# highest = -100.0
# for days in temps:
#     for temp in days:
#         if temp > highest:
#             highest = temp
# print("The Highest temperature is:", highest)

# hot_days = 0
# for day in temps:
#     if day[11] > 20.0:
#         hot_days += 1
# print(hot_days, "days were hot days in the month.") 

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

print(rooms)