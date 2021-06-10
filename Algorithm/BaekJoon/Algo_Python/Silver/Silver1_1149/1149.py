#### import sys

def checkNum(preNum,rgbList):
    if preNum == 0: #이전값이 R  
        return min(rgbList[1], rgbList[2])
    elif preNum == 1:#이전값이 G
        return min(rgbList[0], rgbList[2])
    else :#이전값이 B
        return min(rgbList[0], rgbList[1])

def pickColor(rgbSum,picked,rgbL):
    minNum = checkNum(picked,rgbL)
    picked = rgbL.index(minNum)
    return minNum+rgbSum , picked

hCnt = int(input())
aSum ,bSum, cSum = map(int, input().split())
aPick,bPick, cPick = 0,1,2

for i in range(hCnt-1):
    rgbL = list(map(int, input().split()))
    aSum,aPick=pickColor(aSum,aPick,rgbL)
    bSum,bPick=pickColor(bSum,bPick,rgbL)
    cSum,cPick=pickColor(cSum,cPick,rgbL)

print(min(min(aSum,bSum),cSum))
