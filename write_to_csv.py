import csv

fields = ["Name", "Branch", "Year", "CGPA"]

rows = [
    ["Nikhil", "COE", "2", "9.0"],
    ["Sanchit", "COE", "2", "9.1"],
    ["Aditya", "IT", "2", "9.3"],
    ["Sagat", "SE", "1", "9.4"],
    ["Prateek", "MCE", "3", "7.8"],
    ["Sahil", "EP", "2", "9.1"],
]

filename = "university_records.csv"

with open(filename, "w") as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

mydict = [
    { "Branch": "COE", "Year": "2", "CGPA": "7.0", "Name": "Nikhil"},
    {"Name": "Sanchit",  "Year": "2", "CGPA":"9.1", "Branch": "COE"},
    {"Name": "Aditya", "Year": "2", "CGPA":"9.3", "Branch": "IT"},
    {"CGPA":"9.4", "Name": "Sagat", "Branch": "SE", "Year": "1"},
    {"Name": "Prateek", "Branch": "MCE", "Year": "3", "CGPA":"7.8"},
    {"Name": "Sahil", "Branch": "EP", "Year": "2", "CGPA":"9.1"},
]

fields = ["Name", "Branch", "Year", "CGPA"]

with open(filename, "w") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    writer.writeheader()
    writer.writerows(mydict)