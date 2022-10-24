
def forecast(*tpl: tuple):
    #first list are sunny locations, second are cloudy and third are rainy
    locationList = [[],[],[]]
    finalString = ""
    for i in tpl:
        if i[1] == "Sunny":
            locationList[0].append(i)
        elif i[1] == "Cloudy":
            locationList[1].append(i)
        else:
            locationList[2].append(i)
        locationList[0].sort()
        locationList[1].sort()
        locationList[2].sort()
    for i in range(len(locationList)):
        for k in range(len(locationList[i])):
            finalString += locationList[i][k][0] + " - " + locationList[i][k][1] + "\n"
    return finalString
