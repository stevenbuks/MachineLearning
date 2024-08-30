import os
import json
import csv
data = []

for file in os.listdir('/Users/sbuks/Downloads/jira-incidents'):
    with open("/Users/sbuks/Downloads/jira-incidents/"+file, 'r', encoding='utf-8') as f:
        for item in json.load(f)["items"]:
            dumb = {}
            dumb['ticket_id'] = item['ticket_id']
            dumb['tenants'] = []
            for tenant in item['impacted_tenant']:
                dumb['tenants'].append(tenant['tenant_name'])
            data.append(dumb)
    with open("MIpodData.csv", 'w', encoding="utf-8") as csvfile:
        fieldNames = ["ticket_id", "tenants"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
        writer.writeheader()
        for item in data:
            if "FA" in item["ticket_id"]:
                writer.writerow(item)   

    f.close
