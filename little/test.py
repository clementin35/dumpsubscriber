subscriberNumber = open("registeredSubscriberList.txt", "r+").readlines()

# Number of all registered subscribers in a system.
for line in subscriberNumber:
    if subscriberNumber[i] == subscriberNumber[i+1]:
        sameSubscriberCount += 1
    else:
        subscriberCount += 1

subscriberCount = subscriberCount - sameSubscriberCount
print(subscriberCount)
