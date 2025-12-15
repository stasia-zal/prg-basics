import csv

org='books.csv' #name of original file

with open(org,'r',newline='') as file:
    reader=csv.DictReader(file)
    genres=[]
    for row in reader:
        if row['Genre'] not in genres:
            genres.append(row['Genre'])

def read_org():
    with open(org,'r',newline='') as file:
        return list(csv.DictReader(file))

def write_file(genre):
    content=read_org()
    with open('4.12.'+genre+'.txt','w',newline='') as file:
        if content:
            fieldnames=content[0].keys()
            writer=csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader()
        for row in content:
            if row["Genre"] ==genre:
                writer.writerow(row)

def finale():
    for item in genres:
        write_file(item)
    print('All details have been written to files')

finale()






