import csv 
import os

# Get the current working  
# directory (CWD)  
cwd = os.getcwd()  
    
# Print the current working   
# directory (CWD)  
print("Current working directory:", cwd)  

with open('./Python/OOP/items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            print(items)
        