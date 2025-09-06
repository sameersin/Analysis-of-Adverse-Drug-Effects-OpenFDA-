import requests
import json
import os

year_num = '2024'
num_of_files = 10

def generate_links(split_fileName):
    year = split_fileName[0]
    quarter = split_fileName[1].lower()
    part_1 = split_fileName[3]
    part_2 = split_fileName[5].split(")")[0]
    if len(str(part_1)) == 1:
        part_1 = "000"+str(part_1)
    else:
        part_1 = "00"+str(part_1)

    if len(str(part_2)) == 1:
        part_2 = "000"+str(part_2)
    else:
        part_2 = "00"+str(part_2)

    return "https://download.open.fda.gov/drug/event/{}{}/drug-event-{}-of-{}.json.zip".format(year,quarter,part_1,part_2)

def download_data(link):
    return requests.get(link)

def store_data(data,file_name):
    if os.path.exists('./Data/ZIP/{}.zip'.format(file_name)):
        print("{} exists".format(file_name))
        return
    with open('./Data/ZIP/{}.zip'.format(file_name), 'wb') as fd:
        for chunk in data.iter_content(chunk_size=128):
            fd.write(chunk)



f = open('./fileNames.json')
fileNames = json.load(f)
fileNames = fileNames["fileNames"]
counter = 0

for idx,file in enumerate(fileNames):
    split_fileName = file.split(" ")
    year = split_fileName[0]
    if year == year_num and counter<=num_of_files:
        print(counter,")",year)
        counter = counter+1
        link = generate_links(split_fileName)
        data = download_data(link)
        store_data(data,file)
    else:
        continue






