#Options - type: shot, efg. zone: 2PT, NC3, C3. team: A, B

import csv, math

type, zone, team = input("Enter type, zone, and team: ").split()

totalShotsB = scoredShotsB = totalShotsA = scoredShotsA = 0
twoPointsB = cornerThreeB = outsideThreeB = twoPointsA = cornerThreeA = outsideThreeA = 0
threesMadeA = threesMadeB = cornerThreeMadeA = cornerThreeMadeB = outsideThreeMadeA = outsideThreeMadeB = 0 
twosMadeA = twosMadeB = 0

with open("shots_data.csv", 'r') as file:
  csvreader = csv.reader(file)
  next(csvreader)
  for row in csvreader:
    x = float(row[1])
    y = float(row[2])
    hyp = math.hypot(x, y)

    if (x > 22 or x < -22) and y <= 7.8:
        pos = "cThree"
    elif y > 7.8 and hyp > 23.75:
        pos = "ncThree"
    else:
        pos = "two"

    if row[0] == "Team B":
        totalShotsB += 1
        if row[3] == "1":
            scoredShotsB += 1
        if pos == "two":
            twoPointsB += 1
            if row[3] == "1":
                twosMadeB += 1
        elif pos == "ncThree":
            outsideThreeB += 1
            if row[3] == "1":
                threesMadeB += 1
                outsideThreeMadeB += 1
        elif pos == "cThree":
            cornerThreeB += 1
            if row[3] == "1":
                threesMadeB += 1
                cornerThreeMadeB += 1

    if row[0] == "Team A":
        totalShotsA += 1
        if row[3] == "1":
            scoredShotsA += 1 
        if pos == "two":
            twoPointsA += 1
            if row[3] == "1":
                twosMadeA += 1
        elif pos == "ncThree":
            outsideThreeA += 1
            if row[3] == "1":
                outsideThreeMadeA += 1
        elif pos == "cThree":
            cornerThreeA += 1
            if row[3] == "1":
                cornerThreeMadeA += 1

threesMadeA = outsideThreeMadeA + cornerThreeMadeA

if team == "A":
    if type == "shot":
        if zone == "2PT":
            print(twoPointsA/totalShotsA)
        if zone == "NC3":
            print(outsideThreeA/totalShotsA)
        if zone == "C3":
            print(cornerThreeA/totalShotsA)
    if type == "efg":
        if zone == "2PT":
            efg = (twosMadeA + (.5 * threesMadeA))/twoPointsA
        if zone == "NC3":
            efg = (outsideThreeMadeA + (.5 * threesMadeA))/outsideThreeA
        if zone == "C3":
            print(cornerThreeA)
            print(cornerThreeMadeA)
            print(threesMadeA)
            efg = (cornerThreeMadeA + (.5 * threesMadeA))/cornerThreeA
        print(efg)

if team == "B":
    if type == "shot":
        if zone == "2PT":
            print(twoPointsB/totalShotsB)
        if zone == "NC3":
            print(outsideThreeB/totalShotsB)
        if zone == "C3":
            print(cornerThreeB/totalShotsB)
    if type == "efg":
        if zone == "2PT":
            efg = (twosMadeB + (.5 * threesMadeB))/twoPointsB
        if zone == "NC3":
            efg = (outsideThreeMadeB + (.5 * threesMadeB))/outsideThreeB
        if zone == "C3":
            efg = (cornerThreeMadeB + (.5 * threesMadeB))/cornerThreeB
        print(efg)
