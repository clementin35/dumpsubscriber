import re
# read file
def reParser():
    subscriberData = open("dump_subscriber_data.txt", "r+")
    subscriberList = open("subscriber_list.txt", "w+")
    registeredSubscriberList = open("registeredSubscriberList.txt", "w+")

    # read all subscriber in a file
    subscriber_starter =  "[PTY:"
    subscriber_finisher = "[ROOTDOM:"
    isFound = False

    for line in subscriberData:
        #print(line)
        allSubscriber = re.findall(r'\[PTY: <sip:(.*?)>]\[ROOTDOM:', line)
        onlineSubscriber = re.findall(r'\[REGDEST', line)
        # IF statement after search() tests if it succeeded
        if allSubscriber:
            subscriberList.write(str(allSubscriber) + "\n")
        elif onlineSubscriber:
            onlineSubscriber = re.findall(r'([\w\.-]+@[\w\.-]+)', line)
            registeredSubscriberList.write(str(onlineSubscriber) + "\n")

    registeredSubscriberList.close()

    # Subscriber number variables
    subscriberNumber = open("registeredSubscriberList.txt", "r+").readlines()

    i = 0
    subscriberCount = 0
    sameSubscriberCount = 0

    # Number of all registered subscribers in a system.
    for line in subscriberNumber:
        if i == len(subscriberNumber)-1:
            break
        elif str(subscriberNumber[i]) == str(subscriberNumber[i+1]):
            sameSubscriberCount += 1
        else:
            subscriberCount += 1
        i += 1

    # All registered subscriber number
    print("All registered subscriber number: ", subscriberCount)
    # Total device number
    print("Total device number: ", len(subscriberNumber))

    subscriberList.close()
