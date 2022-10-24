squareMatrix = int(input())
racingNum = int(input())
kilometres = 0
wholeMatrix = []
carLocation = [0, 0]
finished = False
for i in range(squareMatrix):
    rowsOfMatrix = [x for x in input().split(" ")]
    wholeMatrix.append(rowsOfMatrix)
tCoordinates = []
for i in range(len(wholeMatrix)):
    for k in range(len(wholeMatrix[i])):
        if wholeMatrix[i][k] == "T":
            tCoordinates.append([i, k])
while True:
    direction = input()
    if direction == "End":
        wholeMatrix[carLocation[0]][carLocation[1]] = "C"
        if not finished:
            print(f"Racing car {racingNum} DNF.")
            print(f"Distance covered {kilometres} km.")
            break
        break
    if direction == "left":
        carLocation[1] -= 1
        if wholeMatrix[carLocation[0]][carLocation[1]] == ".":
            kilometres += 10
        elif wholeMatrix[carLocation[0]][carLocation[1]] == "T":
            kilometres += 30
            wholeMatrix[tCoordinates[0][0]][tCoordinates[0][1]] = "."
            wholeMatrix[tCoordinates[1][0]][tCoordinates[1][1]] = "."
            if carLocation == tCoordinates[0]:
                carLocation = tCoordinates[1]
            else:
                carLocation = tCoordinates[0]
        elif wholeMatrix[carLocation[0]][carLocation[1]] == "F":
            finished = True
            wholeMatrix[carLocation[0]][carLocation[1]] = "C"
            kilometres += 10
            print(f"Racing car {racingNum} finished the stage!")
            print(f"Distance covered {kilometres} km.")
    elif direction == "right":
        carLocation[1] += 1
        if wholeMatrix[carLocation[0]][carLocation[1]] == ".":
            kilometres += 10
        elif wholeMatrix[carLocation[0]][carLocation[1]] == "T":
            kilometres += 30
            wholeMatrix[tCoordinates[0][0]][tCoordinates[0][1]] = "."
            wholeMatrix[tCoordinates[1][0]][tCoordinates[1][1]] = "."
            if carLocation == tCoordinates[0]:
                carLocation = tCoordinates[1]
            else:
                carLocation = tCoordinates[0]
        elif wholeMatrix[carLocation[0]][carLocation[1]] == "F":
            finished = True
            wholeMatrix[carLocation[0]][carLocation[1]] = "C"
            kilometres += 10
            print(f"Racing car {racingNum} finished the stage!")
            print(f"Distance covered {kilometres} km.")         
    elif direction == "up":
        carLocation[0] -= 1
        if wholeMatrix[carLocation[0]][carLocation[1]] == ".":
            kilometres += 10
        elif wholeMatrix[carLocation[0]][carLocation[1]] == "T":
            kilometres += 30
            wholeMatrix[tCoordinates[0][0]][tCoordinates[0][1]] = "."
            wholeMatrix[tCoordinates[1][0]][tCoordinates[1][1]] = "."
            if carLocation == tCoordinates[0]:
                carLocation = tCoordinates[1]
            else:
                carLocation = tCoordinates[0]
        elif wholeMatrix[carLocation[0]][carLocation[1]] == "F":
            finished = True
            wholeMatrix[carLocation[0]][carLocation[1]] = "C"
            kilometres += 10
            print(f"Racing car {racingNum} finished the stage!")
            print(f"Distance covered {kilometres} km.")
    elif direction == "down":
        carLocation[0] += 1
        if wholeMatrix[carLocation[0]][carLocation[1]] == ".":
            kilometres += 10
        elif wholeMatrix[carLocation[0]][carLocation[1]] == "T":
            kilometres += 30
            wholeMatrix[tCoordinates[0][0]][tCoordinates[0][1]] = "."
            wholeMatrix[tCoordinates[1][0]][tCoordinates[1][1]] = "."
            if carLocation == tCoordinates[0]:
                carLocation = tCoordinates[1]
            else:
                carLocation = tCoordinates[0]
        elif wholeMatrix[carLocation[0]][carLocation[1]] == "F":
            finished = True
            wholeMatrix[carLocation[0]][carLocation[1]] = "C"
            kilometres += 10
            print(f"Racing car {racingNum} finished the stage!")
            print(f"Distance covered {kilometres} km.")
            
for i in range(len(wholeMatrix)):
    for k in range(len(wholeMatrix[i])):
        print(wholeMatrix[i][k], end="")
    print()

