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



names = {}
for item in data:
    names[item['name']] = item['name']



output = []
for name in names:
    output.append((name, list(map(lambda name: name, getAddr(name)))))

print(output)
    

# sorted_list = sorted(sorted_list)
# print(sorted_list)
# for item in sorted_list:
#     print(f'{item[0]}, {item[1]}')
