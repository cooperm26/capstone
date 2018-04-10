import random
import math
runnerPosition = []
defenderPosition = []
radius = 100
distanceToRunner = 25
verticalBoundary = 500
popSize = 1000
t = 0
terms = 14
max = 2
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
def tackle(theList, radius = radius):
    centerDistance = math.sqrt(((theList[0]-theList[2])*(theList[0]-theList[2])) + ((theList[1]-theList[3])*(theList[1]-theList[3])))
    if (2*radius) >= centerDistance:
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
        number = max*random.random()-(max//2)
        functionList += [number]
    return functionList
def generatePopulation(n = popSize):
    population=[]
    i = 0
    while i < n:
        population += [generateList()]
        i+=1
    return population
def updatePosition(theList,previousPosition = [0,0,0,100], t = t):
    runnerXList = theList[0:6]
    runnerYList = theList[7:13]
    defenderXList = theList[14:20]
    defenderYList = theList[21:27]
    tList = tFunction()
    runnerX = previousPosition[0] #Needs to update with movement
    runnerY = previousPosition[1] #Needs to update with movement
    defenderX = previousPosition[2] #Needs to update with movement
    defenderY = previousPosition[3] #Needs to update with movement
    for i in range(0,6):
        runnerX += (tList[i]*runnerXList[i])
        runnerY += (tList[i]*runnerYList[i])
        defenderX += (tList[i]*defenderXList[i])
        defenderY += (tList[i]*defenderYList[i])
    return [runnerX, runnerY, defenderX, defenderY]
population = generatePopulation()
print(population)
t = 0
theTuple = [0,0,0,100]
tackleCount = 0
boundaryCount = 0
totalCount = 0
for i in population:
    while t < 10:
        theTuple = updatePosition(i, theTuple)
        if outofbounds(theTuple):
            boundaryCount += 1
            break
        if tackle(theTuple):
            tackleCount +=1
            break
        t +=1
    totalCount +=1
    t=0
print(str(tackleCount) + " , " + str(boundaryCount) )
print(totalCount)
