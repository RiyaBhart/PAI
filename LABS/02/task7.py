
temperatures = [30, 32, 35, 33, 31, 29, 34, 28, 36, 37, 32, 30, 29, 31, 35, 34, 33, 30, 28, 36, 31, 32, 34, 29, 37, 33, 35, 36, 30, 31]


def calculateaverage(temps):
    avgtemp = sum(temps) / len(temps)
    print("Average temperature for the month:", avgtemp)

def findhighest_lowest(temps):
    highesttemp = max(temps)
    lowesttemp = min(temps)
    print("Highest temperature:", highesttemp)
    print("Lowest temperature:", lowesttemp)


def sorttemperatures(temps):
    sortedtemps = sorted(temps)
    print("Temperatures in ascending order:", sortedtemps)
    return sortedtemps

def removetemperature(temps, day):
    if 1 <= day <= len(temps):
        removedtemp = temps.pop(day - 1)
        print("Temperature of day " ,day," removed: ",removedtemp)
    else:
        print("Invalid day number!")

calculateaverage(temperatures)
findhighest_lowest(temperatures)
sortedtemperatures = sorttemperatures(temperatures)

removetemperature(temperatures, 5)

print("Updated temperatures:", temperatures)
