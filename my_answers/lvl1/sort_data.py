from random import randint
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

def add_random_postal(names_with_addresses):
    num = randint(0,9)*10000 + randint(0,9)*1000 + randint(0,9)*100 + randint(0,9)*10 + randint(0,9)
    return (names_with_addresses, (f'{num}'))


names = set()
for item in data:
    names.add(item['name'])



output = []
for name in names:
    output.append((name, list(map(lambda name: name, getAddr(name)))))
    print(output[-1])

# print(output)

for name_with_addresses in output:
    name_with_addresses = add_random_postal(name_with_addresses)
    print(name_with_addresses)


