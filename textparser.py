class list:
    def __init__(self):
        print("Dump Subscriber Data is Parsing")

    def reParser(self):
        import re
        global subscriberCount, subscriberNumber

        subscriberData = open("dump_subscriber_data.txt", "r+")
        subscriberList = open("subscriber_list.txt", "w+")
        registeredSubscriberList = open("registeredSubscriberList.txt", "w+")

        # read all subscriber in a file
        subscriber_starter =  "[PTY:"
        subscriber_finisher = "[ROOTDOM:"
        isFound = False

        main_starter = "Bucket["
        main_finisher = "[LocationID:",

        dictionary = {}

        with open("dump_subscriber_data.txt", "r+") as dumpSubscribers:
            dumpSubscriberData = dumpSubscribers.read()
            listedData = re.findall(r'Bucket\[(.*?)\[LocationID:', dumpSubscriberData, re.MULTILINE|re.DOTALL)

        registeredSubscriberList = open("registeredSubscriberList.txt", "w+")

        for elements in listedData:

            allSubscriber = re.findall(r'\[PTY: <sip:(.*?)>]\[ROOTDOM:', str(elements))
            subscriberList.write(str(allSubscriber) + "\n")

            totalDeviceForPerSubscriber = re.findall(r'\[REGDEST', str(elements))

            dictionary[str(allSubscriber)] = len(totalDeviceForPerSubscriber)

            if len(totalDeviceForPerSubscriber) > 0:
                registeredSubscriberList.write(str(allSubscriber) + "\n")


        # Test
        ### print(listedData[0] + "\n")
        #         for line in subscriberData:
        #             #print(line)
        #             allSubscriber = re.findall(r'\[PTY: <sip:(.*?)>]\[ROOTDOM:', line)
        #             onlineSubscriber = re.findall(r'\[REGDEST', line)
        #             # IF statement after search() tests if it succeeded
        #             if allSubscriber:
        #                 subscriberList.write(str(allSubscriber) + "\n")
        #             elif onlineSubscriber:
        #                 onlineSubscriber = re.findall(r'([\w\.-]+@[\w\.-]+)', line)
        #                 registeredSubscriberList.write(str(onlineSubscriber) + "\n")

        global allSubscriberNumberFromDictionary
        global totalDeviceNumber

        # LCD Screen information
        with open("dictionary.txt", "w+") as dictionaryOutput:
            allSubscriberNumberFromDictionary = len(dictionary.keys())
            totalDeviceNumber = sum(dictionary.values())

#         for key in dictionary:
#             if dictionary[key] > 0:
#                 with open("registeredSubscriberList.txt", "a+") as registeredSubscriberList:
#                     registeredSubscriberList.write(key + "\n")



        # Write all susbscriber information to a csv file
        with open('my_file.csv', 'w') as f:
            [f.write('{0},{1}\n'.format(key, value)) for key, value in dictionary.items()]


        # Subscriber number variables -> Kac tane regdesti olan adam var
        subscriberNumber = open("registeredSubscriberList.txt", "r+").readlines()

        print("Done*******************")
        # All registered subscriber number
        print("All subscriber number: ", allSubscriberNumberFromDictionary)

        # Total device number
        print("Total device number: ", totalDeviceNumber)

        subscriberList.close()
        subscriberData.close()

    @property
    def p_subscriberCount(self):
        return allSubscriberNumberFromDictionary

    @property
    def p_subscribeNumber(self):
        return totalDeviceNumber
