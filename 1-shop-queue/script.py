

def queueTime(clientsList, tillN, debug=True):
    #initiali array that contains array as many as are available tills
    tills = []
    for i in range(tillN):
        tills.append([])
    t = 0
    clientIndex = 0
    completed = False
    
    while not completed:
        
        allClientsServiced = clientIndex == len(clientsList)
        if debug:
            print("\n" + ("*" * 40))
            print("%d second" % t)
        for i in range(tillN):
            
            if allClientsServiced:
                if (debug):
                    print (" * No clients in queue. Service in progress.")
                break
            
            tillNumber = i+1
            clientTime = clientsList[clientIndex]
            if debug:
                print(" * Process  till #%d" % (tillNumber))

            if t >= sum(tills[i]):
                if (debug):
                    print("   - Service client (%d s) in till #%d" % (clientTime, tillNumber))
                tills[i].append(clientTime)
                clientIndex += 1
                allClientsServiced = clientIndex == len(clientsList)
            else:
                if debug:
                    print("   - Till #%d services client at this moment. %d seconds to complete order." % (tillNumber, sum(tills[i])-t))
            
        t += 1
        if debug:
            print(("*" * 40))
        
        if allClientsServiced:
            checkComplete = True
            for i in range(tillN):
                checkComplete = checkComplete and (sum(tills[i]) <= t)
            if checkComplete:
                completed = True
                if (debug):
                    print("\r\n")
                    print("*** ALL CLIENTS SERVICES. IT TOOK %d s ***" % t)
        
    return t
        
    

#should be 10
time = queueTime([10,2,3,3], 2, True)

print("Time: %s" % time)