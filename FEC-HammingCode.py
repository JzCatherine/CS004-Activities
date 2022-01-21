# Forward Error Correction, Hamming code and Hamming distance

# The process used by the sender to encode the message includes the following three steps:
#   1. Calculation of total numbers of redundant bits.
#   2. Checking the position of the redundant bits.
#   3. Lastly, calculating the values of these redundant bits.
def sender(data):
    print('=' * 90, "\nSENDER")
    print(" Data: ", data)
    posList, dataList = appendParityBits(data)
    dataList = calcParityBits(dataList, posList)
    print(" Data with parity bits:", ("{}"*len(dataList)).format(*dataList))
    return posList

# SENDER Step 1: Calculate the total number of redundant data bits to be added to the data'
# Number of parity bits will be calculated by using the data bits. 
# This relation is given but the formula: 2^P >= n + P +1 
#   where,  n = number of bits in the data string
#           p = number of parity bits
def noParityBits(n):
    for p in range(n):
        if(2**p >= n + p + 1):
            return p
# SENDER Step 2: Append parity position in the data
def appendParityBits(data):
    n = noParityBits(len(data)) #no of parity bits required for given length of data
    i = 0 #loop counter
    p = 0 #no of parity bits
    d = 0 #no of data bits
    posList = [] # position of the data bits and redundant bits
    dataList = [] # data bits and parity bits
    while i < n+len(data):
        if i== (2.**p -1):
            posList.append('P'+str(i+1))
            dataList.append(0) # 0 is initially placed to the parity bits position
            p+=1
        else:
            posList.append('D'+str(i+1))
            dataList.append(data[d]) # data bits are appended
            d+=1
        i+=1
    return posList, dataList

# SENDER Step 3: Calculate the parity value of the redundant bits
def calcParityBits(dataList, posList):
    r = noParityBits(len(data)) 
    n = len(dataList)
    print("\t ", '-'*len(dataList)*(3+2))
    for i in range(r):
        parityString = '' # stores the parity string
        parity = 0 # value of parity
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                if (dataList[j-1] == 0):
                    print("\t ", posList[j-1], ":", end=' ')
                parityString += str(dataList[j-1])
                # Even 1s = 0, Odd 1s = 1
                parity = parity ^ int(dataList[1 * j-1])
                print(posList[j-1], end=' ')
        # Insert Parity value in dataList
        for k in range(0, n):      
            if (dataList[k-1] == 0):
                dataList[k-1] = str(parity)
                break
        if(parity == 0):
            print("→", parityString, "=", parity, "[Even 1s]", end=' ')
        elif(parity == 1):        
            print("→", parityString, "=", parity, "[Odd 1s]", end=' ')
        print("")
    print("\t ", '-'*len(posList)*(3+2), "\n\t", ("|{:4}"*len(posList)).format(*posList), "|")
    print("\t ", '-'*len(posList)*(3+2), "\n\t", ("|{:4}"*len(dataList)).format(*dataList), "|")
    print("\t ", '-'*len(posList)*(3+2))
    return dataList             




# Receiver gets incoming messages and performs recalculation with the following steps:
#   1. Counting the number of redundant bits.
#   2. identifying the positions of all the redundant bits.
#   3. Parity check
def receiver(receivedData):
    print('=' * 90, "\nRECEIVER")
    print(" Received Data: ", receivedData)
    
    print(" ERROR DETECTION [0 = no error, 1 = error]")
    posList, receivedDataList = posParityBits(receivedData)
    errorLocation, error = errorDetection(receivedData, receivedDataList, posList)
    
    if(error == True):
        print(" ERROR CORRECTION")
        # change the bit that is damaged
        if(receivedDataList[errorLocation-1] == '1'):
            receivedDataList[errorLocation-1] = '0'
        elif(receivedDataList[errorLocation-1] == '0'):
            receivedDataList[errorLocation-1] = '1'
        print("\tData with parity bits: ", ("{}"*len(receivedDataList)).format(*receivedDataList))
    else:
        print(" NO ERROR DETECTED")
        
    # DECODE
    print("\tTransmitted Data: ", end = " ")
    for i in range(len(receivedDataList)+1):
        if (posList[i-1] == 'D'+str(i)):
            print(receivedDataList[i-1], end='')
  
        
# RECEIVER Step 1: Calculate the total number of redundant data bits in the data
def noOfParityBitsInData(n):
    for p in range(n):
        if(2**p >= n + 1):
            return p

# RECEIVER Step 2: identify the positions of all the redundant bits.
def posParityBits(receivedData):
    n = noOfParityBitsInData(len(receivedData)) #no of parity bits required for given length of data
    i = 0 #loop counter
    p = 0 #no of parity bits
    d = 0 #no of data bits
    posList = [] # position of the data bits and redundant bits
    receivedDataList = [char for char in receivedData]
    while i < n+(len(receivedData)-n):
        if i== (2.**p -1):
            posList.append('P'+str(i+1))
            p+=1
        else:
            posList.append('D'+str(i+1))
            d+=1
        i+=1
    # display data
    print("\t ", '-'*len(posList)*(3+2), "\n\t", ("|{:4}"*len(posList)).format(*posList), "|")
    print("\t ", '-'*len(posList)*(3+2), "\n\t", ("|{:4}"*len(receivedDataList)).format(*receivedDataList), "|")
    print("\t ", '-'*len(posList)*(3+2))
    return posList, receivedDataList
    
# RECEIVER Step 3: Parity Check
def errorDetection(receivedData, receivedDataList, posList):
    r = noOfParityBitsInData(len(receivedData))
    n = len(receivedDataList)
    error = False
    detectionResult = ''
    locParity = ''
    for i in range(r):
        parityString = '' # stores the parity string
        parity = 0 # value of parity
        # get the value of the parity bits
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                if (posList[j-1] == 'P'+str(j)):
                    locParity +=  ' P'+str(j)
                    print("\t ", posList[j-1], ":", end=' ')
                parityString += str(receivedDataList[j-1])
                # Even 1s = 0, Odd 1s = 1
                parity = parity ^ int(receivedDataList[1 * j-1])
                print(posList[j-1], end=' ')
        
        # Check value of Parity bits
        for k in range(0, n):
            if(parity == 0):
                detectionResult = str(parity) + detectionResult
                print("→", parityString, "=", parity, "[No Error]", end=' ')
                break
            elif(parity == 1):
                error = True     
                detectionResult = str(parity) + detectionResult   
                print("→", parityString, "=", parity, "[Error Detected]", end=' ')
                break
        print("")
    # Location of the Error
    errorLocation = int(detectionResult, 2)
    if(error == True):
        print("\t ", '-'*len(posList)*(3+2))
        print("\t  Error: ", locParity, "→", detectionResult, "=", errorLocation)
        print("\t  Location of the error: ", "Bit", errorLocation)
    print("\t ", '-'*len(posList)*(3+2))
    return errorLocation, error



# Driver Code of the Program
print('=' * 90, "\n\t\t\tF O R W A R D  E R R O R  C O R R E C T I O N")
print('-' * 90)
data = input(" Enter the data to be transmitted: ")
sender(data)
print('=' * 90, "\nNOTE: To simulate a single-bit error, Change a bit from the data")
print('-' * 90)
receivedData = input("Enter Data with parity bits: ")
receiver(receivedData)
print("\n", '=' * 90, sep='')