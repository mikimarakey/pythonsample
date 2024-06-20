import csv
with open('financialyear.csv','r') as csv_file:
    f=csv.reader(csv_file)
    for fi in f:
        print(fi)