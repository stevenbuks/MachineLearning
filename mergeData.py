import os
import json
import csv
from collections import defaultdict
with open("MIpodData.csv") as file:
    podFileReader = csv.DictReader(file, dialect=csv.unix_dialect)
    ticketPod = defaultdict(list)
    for item in podFileReader:
        #temp = {}
        for pod in eval(item["tenants"]):
            ticketPod[pod].append(item["ticket_id"])
#print(ticketPod)
with open("ticket_data.csv") as file:
    ticketFileReader = csv.DictReader(file)
    ticketFileReader.fieldnames.append("Pod")
    #print(ticketPod)
    for pod in ticketPod:
        tickets = ticketPod[pod]
        print(tickets)
        break
        for i in range(len(tickets)):
            for item in ticketFileReader:
                print(tickets[i], item["Issue Key"])
                if item["Issue Key"] == tickets[i]:
                    print("$$$$$$$$$$$$")
                    ticketPod[pod][i] = item
        print(ticketPod[pod])

        