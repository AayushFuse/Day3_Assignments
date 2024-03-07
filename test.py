import csv


with open('data.csv') as ifile,open('adults.csv','w') as ofile:

    reader = csv.DictReader(ifile) 
    fields = reader.fieldnames    
    writer = csv.DictWriter(ofile,fieldnames=fields)
    writer.writeheader()
    for row in reader:
        if int(row['Age'])>20:
            writer.writerow(row)
    
    
