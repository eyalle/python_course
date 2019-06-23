import sys
sys.path.append("../../")
from exercises.data import get_data

def getName(dic):
    return dic['name']

data = get_data(20)
sorted_list = []
for item in data:
    sorted_list.append((item['name'],item['address']))

sorted_list = sorted(sorted_list)
print(sorted_list)
# for item in sorted_list:
#     print(f'{item[0]}, {item[1]}')
