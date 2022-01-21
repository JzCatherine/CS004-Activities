# Arithmetic Checksum

def sender(SentMessage, n):
    # The message is divided into frames/packets of n bit length.
    SentMessageList = []
    print("Sent Message: ", end="")
    for i in range(int(len(SentMessage)/n)):
        SentMessageList.append(str(SentMessage[n*i:n*i+n]))
        print(SentMessage[n*i:n*i+n], " ", end="")
    print("\n")

    # Display packets
    for i in range(len(SentMessageList)):
        print("\t", SentMessageList[i], "\t→ Frame {} ".format(i+1), "\t")

    # All the packets of Sender's Data are added together to get the Sum.
    Sum = 0
    for i in range(len(SentMessageList)):
        Sum += int(SentMessageList[i], 2)
    Sum = bin(Sum)[2:]
    print("\t", '-'*50, "\n\t", Sum, "\t→ Sum")
    
    # if Sum is greater than the bit length, wrap the Sum by adding the overflow bits
    if(len(Sum) > n):
        x = len(Sum)-n
        Sum = bin(int(Sum[0:x], 2)+int(Sum[x:], 2))[2:]
    if(len(Sum) < n):
        Sum = '0'*(n-len(Sum))+Sum
    print("\t", Sum, "\t→ Wrapped Sum")

    # The sum is complemented and becomes the Checksum.
    # Calculating the complement of sum
    SenderChecksum = ''
    for i in Sum:
        if(i == '1'):
            SenderChecksum += '0'
        else:
            SenderChecksum += '1'
    print("\t", '-'*50, "\n\t", SenderChecksum, "\t→ Sender Checksum")

    return SenderChecksum
    


def receiver(ReceivedMessage, n, SenderChecksum):
    # The message is divided into frames/packets of n bit length.
    ReceivedMessageList = []
    print("Received Message: ", end="")
    for i in range(int(len(ReceivedMessage)/n)):
        ReceivedMessageList.append(str(ReceivedMessage[n*i:n*i+n]))
        print(ReceivedMessage[n*i:n*i+n], " ", end="")
    print("\n")

    # Display frames
    for i in range(len(ReceivedMessageList)):
        print("\t", ReceivedMessageList[i], "\t→ Frame {} ".format(i+1), "\t")
    print("\t", SenderChecksum, "\t→ Sender Checksum")

    # All the frames of Reciever's Data and Sender's Checksum are added together to get the Sum.
    Sum = 0
    for i in range(len(ReceivedMessageList)):
        Sum += int(ReceivedMessageList[i], 2)
    Sum += int(SenderChecksum, 2)
    Sum = bin(Sum)[2:]
    print("\t", '-'*50, "\n\t", Sum, "\t→ Sum")
    
    # if Sum is greater than the bit length, wrap the Sum by adding the overflow bits
    if(len(Sum) > n):
        x = len(Sum)-n
        Sum = bin(int(Sum[0:x], 2)+int(Sum[x:], 2))[2:]
    if(len(Sum) < n):
        Sum = '0'*(n-len(Sum))+Sum
    print("\t", Sum, "\t→ Wrapped Sum")

    # The sum is complemented and becomes the Recievers Checksum.
    ReceiverChecksum = ''
    for i in Sum:
        if(i == '1'):
            ReceiverChecksum += '0'
        else:
            ReceiverChecksum += '1'
    print("\t", '-'*50, "\n\t", ReceiverChecksum, "\t→ Sender Checksum")

    return ReceiverChecksum


def arithmeticChecksum(SentMessage, ReceivedMessage, n):
    # sender() function will generate the checksum on the Sender side and perform the following steps:
    #     1. The message will be divided into frames/packets of n bit length.
    #     2. All the frames/packets of Sender's Data are added together to get the Sum.
    #     3. The sum will be complemented and becomes the Checksum.
    #     4. The checksum will be sent with the data to the receiver side.
    print('=' * 90, "\nSENDER")
    SenderChecksum = sender(SentMessage, n)
    
    # receiver() function will recieve the message from the sender along with the checksum and perform the following steps:
    #     1. The message will be divided into frames/packets of n bit length.
    #     2. All frames/packets are added together to get the sum.
    #     3. The checksum generated from the sender is added to the sum of all frames/packets.
    #     4. The resulting sum is complemented.
    print('=' * 90, "\nRECEIVER")
    ReceiverChecksum = receiver(ReceivedMessage, n, SenderChecksum)

    # Check the Reciever Checksum if Erroir is detected
    # If reciever checksum is equivalent to 0 then there is no error detected
    # Otherwise, Error is detected
    print('=' * 90, "\n\nERROR DETECTION RESULT\n")
    if(int(ReceiverChecksum, 2) == 0):
        print("\tSTATUS: MESSAGE ACCEPTED")
        print("\t\t> Receiver Checksum '", ReceiverChecksum , 
              "' is equal to 0.\n\n", '=' * 90, sep = '')
    else:
        print("\tSTATUS: ERROR DETECTED")
        print("\t\t> Receiver Checksum '", ReceiverChecksum , 
              "' is not equal to 0.\n\n", '=' * 90, sep = '')

# Driver Code of the Program
print('=' * 90, "\n\t\t\tA R I T H M E T I C   C H E C K S U M")
print('=' * 90)
SentMessage = input(" Enter Sent Message : ")
ReceivedMessage = input(" Enter Received Message : ")
n = int(input(" Enter frame/packet bit length : "))
# Call arithmeticChecksum() function to perform Arithmetic Checksum Error Detection
arithmeticChecksum(SentMessage, ReceivedMessage, n)
