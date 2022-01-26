import json

f = open('../data/labels/labels.json')
label = json.load(f)

print(label)
print(type(label))
print(len(label))

print(label[0])
print(type(label[0]))

print(label[0].keys())
print(label[0]['attributes'])
print(type(label[0]['attributes']))

print(label[0]['labels'])
print(type(label[0]['labels']))

for label in label[0]['labels']:
    print(label.keys())
