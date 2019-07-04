import sys
sys.path.append("../../")
from exercises.data import get_data
import random

data = get_data(5)
users = [{'name': items['name']} for items in data]

hobbies = [
    'football',
    'strongman',
    'mario',
    'tekken-3',
    'beach',
    'soccer',
    'bacon',
    'pool',
    'dodge ball'
]

hobbies2 = [
    'star wars',
    'star trek',
    'mario cart',
    'draw',
    'manga artist',
    'ogre slayer',
    'porn star',
    'high five guy!',
    'idan hakimi'
]

def add_random_hobby(users):
    for user in users:
        user['hobby'] = random.choice(hobbies)


def count_hobbies(users):
    count = {hobby: 0 for hobby in hobbies}
    for user in users:
        count[user['hobby']] += 1
    for hobby in count:
        print(hobby, count[hobby])

def add_second_hobby(users):
    for user in users:
        hobby2 = random.choice(hobbies)
        # hobby2 = random.choice(hobbies2) if (hobby2 == user['hobby'])
        if (hobby2 == user['hobby']):
            hobby2 = random.choice(hobbies2)
        user['hobby2'] = hobby2
    print(f'{users}')


if __name__ == "__main__":
    add_random_hobby(users)
    count_hobbies(users)
    add_second_hobby(users)
    