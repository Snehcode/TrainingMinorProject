import csv



def get_names():
    f=open('tasktrainingdata.csv')
    content=csv.reader(f)
    
    names=[]
  

    for row in content:
        names.append(row[0])
     
    
    return names
 

def get_emails():
    f=open('tasktrainingdata.csv')
    content=csv.reader(f)
    
    emails=[]

    for row in content:
        emails.append(row[1])
     
    
    return emails


