from PIL.Image import new
from asyncio import open_connection
import csv

# with open("sample.csv", "r") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)
        

# with open("sample.csv", "r") as file:
#     reader = csv.DictReader(file)
    
#     for row in reader:
#         print(row["id"] , "\t" , row["name"])
        

# def read_batches(file,batch_szie=1000):
#     reader = csv.DictReader(file)
    
#     batch = []
    
#     for row in reader:
#         batch.append(row)
        
#         if len(batch) == batch_szie:
#             yield batch
#             batch = []
    
#     if batch:
#         yield batch

# with open('sample.csv','r') as file:
#     for batch in read_batches(file,10):
#         print('Processing : ' , len(batch))


with open('sample.csv' , 'r') as file:
    reader = csv.DictReader(file)
    
    with open('high_sal.csv' , 'w' , newline="") as out_file:
        
        writter = csv.DictWriter(
            out_file,
            fieldnames=reader.fieldnames
        )
        
        writter.writeheader()
        
        for row in reader: 
            if int(row['salary']) > 80000:
                writter.writerow(row)
        
        