

def queueTime(clientsList, tillN):
    #initiali array that contains array as many as are available tills
    tills = []
    for i in range(tillN):
        tills.append([])
    t = 0
    clientIndex = 0
    completed = False
    
    while not completed:
        
        allClientsServiced = clientIndex == len(clientsList)
        print("\n" + ("*" * 40))
        print("%d second" % t)
        for i in range(tillN):
            
            if allClientsServiced:
                print (" * No clients in queue. Service in progress.")
                break
            
            tillNumber = i+1
            clientTime = clientsList[clientIndex]
            print(" * Process  till #%d" % (tillNumber))

            if t >= sum(tills[i]):
                print("   - Service client (%d s) in till #%d" % (clientTime, tillNumber))
                tills[i].append(clientTime)
                clientIndex += 1
                allClientsServiced = clientIndex == len(clientsList)
            else:
                print("   - Till #%d services client at this moment. %d seconds to complete order." % (tillNumber, sum(tills[i])-t))
            
        t += 1
        print(("*" * 40))
        
        if allClientsServiced:
            checkComplete = True
            for i in range(tillN):
                checkComplete = checkComplete and (sum(tills[i]) <= t)
            if checkComplete:
                completed = True
                print("\r\n")
                print("*** ALL CLIENTS SERVICES. IT TOOK %d s ***" % t)
        
    return t
        
    

#should be 10
print(range(5))
time = queueTime([10,2,3,3], 2)

print("Time: %s" % time)