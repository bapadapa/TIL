warNum = int(input())

for i in range(warNum):
    army = list(map(int, input().split()))
    armyCnt = army[0]
    army = army[1:]    
    armyDict ={}
    for j in army:
        if str(j) in armyDict:
            armyDict[str(j)] +=1
        else:
            armyDict[str(j)] =1
    flag = True
    for key,val in armyDict.items():
        if val > armyCnt/2:
            print (key)
            flag =False
            break
    if flag :
        print('SYJKGW')