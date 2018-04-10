import random
import math
#Values Necessary, can be changed with one exception
radius = 15
fix = .5*radius
distanceToRunner = 50
verticalBoundary = 50
popSize = 1000
t = 0
#Changing terms will cause error
terms = 14
max = 1.25
initialX = 0
initialRunnerY = 0
initialDefenderY = initialRunnerY + distanceToRunner
runnerPosition = [initialX, initialRunnerY]
defenderPosition = [initialX, initialDefenderY]
initialPositions = [runnerPosition[0], runnerPosition[1], defenderPosition[0], defenderPosition[1]]
rightMin = 0
rightMax = 100
mutationrate = .05
def translate(value, leftMin, leftMax, rightMin = rightMin, rightMax = rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)
#Determines values that random numbers will be multiplied against
def tFunction(t= t):
    tList = []
    for i in range(1,((terms//2)-2)+1):
        tList += [t^i]
    sine = math.sin(t)
    cosine = math.cos(t)
    tList.append(sine)
    tList.append(cosine)
    return tList
    #determines if a runner has been tackled
def tackle(theList, radius = radius, fix = fix):
    centerDistance = math.sqrt(((theList[0]-theList[2])*(theList[0]-theList[2])) + ((theList[1]-theList[3])*(theList[1]-theList[3])))
    if (2*radius + fix ) >= centerDistance:
        return True
    else:
        return False
def outofbounds(theList, radius = radius, boundary = verticalBoundary):
    leftmost = theList[0] - radius
    rightmost = theList[0] + radius
    if (boundary <= rightmost) or (-boundary>=leftmost):
        return True
    else:
        return False

def generateList(terms = terms, max = max):
    functionList= []
    for  i in range(1,(2*terms)+1):
        number = max*random.random()-(max/2)
        functionList += [number]
    return functionList
def generatePopulation(n = popSize):
    population=[]
    i = 0
    while i < n:
        population += [generateList()]
        i+=1
    return population
def updatePosition(a_list, t = t):
    tList =  tFunction()
    runnerX = a_list[0:6]
    runnerY = a_list[7:13]
    defenderX = a_list[14:20]
    defenderY = a_list[21:27]
    runnerXDelta = 0
    runnerYDelta = 0
    defenderXDelta = 0
    defenderYDelta = 0
    for i in range(0,len(tList)-1):
        runnerXDelta += (i*runnerX[i])
        runnerYDelta += (i*runnerY[i])
        defenderXDelta += (i*defenderX[i])
        defenderYDelta += (i*defenderY[i])
    delta = [runnerXDelta,runnerYDelta,defenderXDelta,defenderYDelta]
    return delta
def getPosition(a_list, initialPositions, t = t):
    delta = updatePosition(a_list)
    position = []
    for i in range(0,len(initialPositions)):
        position += [delta[i]+initialPositions[i]]
    return position
def runnerFitness(format):
    return 1
def defenderFitness(dFormat):
    return 1
t = .1
oldPosition = initialPositions
sample = 1
tackleCount = 0
boundaryCount = 0
def fitness(population, initialPositions = initialPositions, t = t):
    oldPosition = initialPositions
    returnList= []
    for i in population:
        while t<4:
            position = getPosition(i,oldPosition, t)
            runner = position[0:2]
            defender = position [2:]
            if tackle(position):
                break
            if outofbounds(position):
                break
            oldPosition = position
            t+= .1
        returnList +=[[ runner[1],t]]
        t=.1
        oldPosition = initialPositions
    return returnList
def findMinMax(fitnessList):
    minY = 0
    maxY = 0
    for i in fitnessList:
        if i[0] > maxY:
            maxY = i[0]
        if i[0] < minY:
            minY = i[0]
    return (minY, maxY)
def arrangePopForRunners(population, initialPositions = initialPositions, t = t, rightMin = rightMin, rightMax = rightMax):
    arrangedrunnerpop = []
    fitnesslist  = fitness(population)
    (minY,maxY) = findMinMax(fitnesslist)
    for i in fitnesslist:
        i[0] = translate(i[0],minY,maxY)
    for j in range(0,len(population)):
        arrangedrunnerpop += int(fitnesslist[j][0])*[population[j]]
    return arrangedrunnerpop
def arrangePopForDefenders(population, initialPositions = initialPositions, t = t, rightMin = rightMin, rightMax = rightMax):
    arrangeddefenderpop = []
    fitnesslist = fitness(population)
    for i in fitnesslist :
        i[0] = 1/i[0]
        (minY,maxY) = findMinMax(fitnesslist)
        i[0] = translate(i[0],minY,maxY)
    for j in range(0,len(population)):
        arrangeddefenderpop += int(fitnesslist[j][0])*[population[j]]
    return arrangeddefenderpop
def newPopulation(population, initialPositions = initialPositions, t = t, rightMin = rightMin, rightMax = rightMax, popSize = popSize):
    runnerarrng = arrangePopForRunners(population)
    defenderarrng = arrangePopForDefenders(population)
    newpop = []
    child = []
    while len(newpop) < popSize :
        rparent1 = runnerarrng[random.randint(0,len(runnerarrng)-1)]
        rparent2 = runnerarrng[random.randint(0,len(runnerarrng)-1)]
        dparent1 = defenderarrng[random.randint(0,len(defenderarrng)-1)]
        dparent2 = defenderarrng[random.randint(0,len(defenderarrng)-1)]
        for i in range(0,14):
            randomnumber = random.random()
            if randomnumber < .5:
                child += [rparent1[i]]
            else:
                child += [rparent2[i]]
        for j in range(14,28):
            randomnumber = random.random()
            if randomnumber < .5:
                child += [dparent1[i]]
            else:
                child += [dparent2[i]]
        newpop += [child]
        child = []
    return newpop
def mutation(population, mutationrate = mutationrate, max = max):
    for i in population:
        for j in i:
            if random.random() <= mutationrate:
                j = max*random.random()-(max/2)
    return population

generation = 0
population = generatePopulation()
t =  .1
while generation < 100:
    print(generation)
    fitnessL = fitness(population)
    total = 0
    sum = 0
    for i in fitnessL:
        sum += i[0]
        total +=1
    print(sum/total)
    total = 0
    sum = 0
    population = newPopulation(population)
    population = mutation(population)
    generation += 1
