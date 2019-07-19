import jsonlines


with jsonlines.open('epic.json', 'r') as reader:
    for obj in reader:
        #for x in range(len(obj['markets'])):
            # print(x)

        print(obj['markets'][0])#['epic'])

