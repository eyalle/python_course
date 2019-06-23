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



names = []
for item in data:
    names.append(item['name'])

list(set(names))

output = []
for item in names:
    output.append((item, list(map(lambda item: item, getAddr(item)))))

print(output)
    

# sorted_list = sorted(sorted_list)
# print(sorted_list)
# for item in sorted_list:
#     print(f'{item[0]}, {item[1]}')
