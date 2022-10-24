from collections import deque
milligramsOfCaffeine = deque([int(x) for x in input().split(", ")])
energyDrinks = deque([int(x) for x in input().split(", ")])
stamatTotalCaffeine = 0

while (milligramsOfCaffeine and energyDrinks):
    if stamatTotalCaffeine + milligramsOfCaffeine[-1] * energyDrinks[0] <= 300:
        try:
            stamatTotalCaffeine += milligramsOfCaffeine.pop() * energyDrinks.popleft()
        except IndexError:
            break
    else:
        milligramsOfCaffeine.pop()
        energyDrinks[0], energyDrinks[-1] = energyDrinks[-1], energyDrinks[0]
        if stamatTotalCaffeine - 30 > 0:
            stamatTotalCaffeine -= 30
        
finalStr = ""
if energyDrinks:
    for i in range(len(energyDrinks)):
        finalStr += str(energyDrinks[i]) + ", "
    finalStr = finalStr[:-2]
    print(f"Drinks left: {finalStr}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.") 
print(f"Stamat is going to sleep with {stamatTotalCaffeine} mg caffeine.")       
    




