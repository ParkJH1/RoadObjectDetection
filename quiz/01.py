import json

f = open('../data/labels/labels.json')
j = json.load(f)

file_name = input()

for l in j:
    if l['name'] == file_name:
        for label in l['labels']:
            if 'box2d' in label:
                print(label['category'], label['box2d'])
