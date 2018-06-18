import sys
import random

def hill_climbing(funcText, xmin, xmax, ymin, ymax):
    #starts at a random location
    x = random.randint(xmin, xmax)
    y = random.randint(ymin, ymax)

    for t in range(0,1000):
        # holds current maximum coordinates
        xtemp = x
        ytemp = y
        tempMax = my_func(x,y)
        
        xList = [x-1, x, x+1]
        yList = [y-1, y, y+1]
        #checks surrounding points, and compares values. If it breaks current maximum, overrrides current max's coordinates 
        for x in xList:
            if x >= xmin and x <= xmax:
                for y in yList:
                    if y >= ymin and y <= ymax:
                        if my_func(x,y) > tempMax:
                            xtemp = x
                            ytemp = y
                            tempMax = my_func(x,y)

        #set x and y to current max before restarting loop
        x = xtemp
        y = ytemp
        


    cord = [x, y]

    return cord


def main():
    sMax = [0,0]
    f = open(sys.argv[1], "r")
    funcText = f.read()

    f.close()
    tempHill = -1000 
    func = exec(funcText,globals())
    for x in range(0,100):
        tempMax = hill_climbing(funcText,int(sys.argv[2]),int(sys.argv[4]),int(sys.argv[3]),int(sys.argv[5]))
        if (my_func(tempMax[0],tempMax[1]) > tempHill):
            tempHill = my_func(tempMax[0], tempMax[1])
            sMax = tempMax
#if tempMax > sMax:
         #   sMax = tempMax
    print(sMax)

main()
