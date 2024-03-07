# Implement a program that reads a CSV file named "data.csv," containing columns "Name" and "Age." 
# Create a new CSV file called "adults.csv" with only the rows of individuals who are 18 years or older.

#Using pandas
import pandas as pd


info = pd.read_csv('files/data.csv')
info[info.Age>18].to_csv('files/adults.csv',index=None)

#from scratch using csv
import csv


with open('data.csv') as ifile,open('files/adults.csv','w') as ofile:

    reader = csv.DictReader(ifile) 
    fields = reader.fieldnames    
    writer = csv.DictWriter(ofile,fieldnames=fields)
    writer.writeheader()
    for row in reader:
        if int(row['Age'])>20:
            writer.writerow(row)
    

# Create a function add_to_json that takes a filename and a dictionary as input. 
# The function should read the JSON data from the file, add the new dictionary to it, and write the updated data back to the same file.
import json

def add_to_json(filename,in_dict):
    try:
        with open(filename,'r') as file:
            data = json.load(file) 
        
        data.append(in_dict)
        print(data)
        with open(filename,'w') as file:
            json.dump(data,file)
    except Exception as e:
        print(f"Exception: {e}")



data ={
    "name": "Laxman",
    "age": 20
  }
add_to_json('files/file.json',data)

