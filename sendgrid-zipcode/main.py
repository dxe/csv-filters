import csv

output = []

# get user input
zipList = input("Enter zipcodes (comma-separated): ")
outputName = input("Enter output filename (w/o any spaces or extension): ")

# split by comma
zipList = zipList.split(',')

# trim whitespace
for i in range(len(zipList)):
    zipList[i] = zipList[i].strip()

with open('input.csv') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if row["POSTAL_CODE"] in zipList:
            output.append({"FIRST_NAME": row["FIRST_NAME"], "LAST_NAME": row["LAST_NAME"], "EMAIL": row["EMAIL"]})

if len(output) == 0:
    print("No matching entries found!")
    exit()

keys = output[0].keys()
with open('output/' + outputName + '.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(output)
