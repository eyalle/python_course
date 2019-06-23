import sys
sys.path.append("../../")
from exercises.data import get_data

data = get_data(20)

def getAddr(name):
    addresses = []
    for item in data:
        if (name == item['name']):
            addresses.append(item['address'])

    return addresses



names = set()
for item in data:
    names.add(item['name'])



output = []
for name in names:
    output.append((name, list(map(lambda name: name, getAddr(name)))))

print(output)
    
