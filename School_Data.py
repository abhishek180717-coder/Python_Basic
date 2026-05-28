
#Student Average Score
sd = {}
while True:
    name = input("Enter Students name:")
    if name == "":
        break
    score = int(input(f"Enter {name}'s score:")) 
                      
    if score not in range(1,11):
        break
    if name in sd:
        sd[name] += (score, )
    else:
        sd[name] = (score, )        

print(sd)  

for name, mark in sd.items():
    sum = 0
    #print(name,"->") 
    for m in mark:
        #print(m)
        sum += m
    print(name, "->",sum/len(mark)) 