with open ("weather.txt", "r") as f:
    data = f.read().split("\n")

stations = {}

for station in data:
    try:
        int(station.split(" ")[-1])
        sky = False
    except:
        sky = True
        
    if len(station) > 3:
        statData = station.split(" ")
        statName = station.split(":")[0]
        if sky:
            stations[statName] = {
                "morning": statData[-4],
                "afternoon": statData[-3],
                "evening": statData[-2],
                "sky": statData[-1],
                "average": round((int(statData[-4]) + int(statData[-3]) + int(statData[-2]))/3, 1),
                "max": min([int(statData[-4]), int(statData[-3]), int(statData[-2])]),
                "min": min([int(statData[-4]), int(statData[-3]), int(statData[-2])]),
            }
        else:
            stations[statName] = {
                "morning": statData[-3],
                "afternoon": statData[-2],
                "evening": statData[-1],
                "average": round((int(statData[-3]) + int(statData[-2]) + int(statData[-1]))/3, 1),
                "max": min([int(statData[-3]), int(statData[-2]), int(statData[-1])]),
                "min": min([int(statData[-3]), int(statData[-2]), int(statData[-1])]),
            }
        
maxTemp = [list(stations.keys())[0], stations[list(stations.keys())[0]]["max"]]
minTemp = [list(stations.keys())[0], stations[list(stations.keys())[0]]["min"]]
overallAverage, sunny, cloudy, overcast = 0, 0, 0, 0

print(f"There are {len(stations)} stations: ")
for stat in stations:
   
    print(f"{stat} - average temperature: {stations[stat]['average']}")
    
    if stations[stat]["max"] > maxTemp[1]:
        maxTemp = [stat, stations[stat]["max"]]
        
    if stations[stat]["min"] > minTemp[1]:
        maxTemp = [stat, stations[stat]["min"]]
    
    overallAverage += int(stations[stat]["average"])
    
    try: 
        if sky:
            if stations[stat]["sky"] == "S":
                sunny += 1
            elif stations[stat]["sky"] == "C":
                cloudy += 1
            if stations[stat]["sky"] == "O":
                overcast += 1
    except:
        continue
    
print(f"The highest temperature: {maxTemp[1]} in {maxTemp[0]}")
print(f"The lowest temperature: {minTemp[1]} in {minTemp[0]}")
print(f"Overall average temperature: {round(overallAverage/len(stations), 1)}")
print(f"sunny: {sunny}, cloudy: {cloudy}, overcast: {overcast}")
