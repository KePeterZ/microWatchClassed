#!/usr/bin/env python3

numberOfX = int(input("tell me max x: "))
numberOfY = int(input("tell me max y: "))

finalList = []

for y in range(numberOfY):
    xValues = list(input())
    for x in range(numberOfX):
        if xValues[x] == "x":
            print((x,y))
            finalList.append((x,y))

print(finalList)