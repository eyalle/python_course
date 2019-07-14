import sys, random, time
sys.path.append("../../")
from exercises.data import get_data

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

consolidated_hobbies = list(set(hobbies + hobbies2))
print(consolidated_hobbies)
def add_random_hobby(users):
    for user in users:
        user['hobby'] = random.choice(hobbies)
    time.sleep(1)

def count_hobbies(users):
    count = {hobby: 0 for hobby in hobbies}
    for user in users:
        if (user['hobby']):
            count[user['hobby']] += 1
        elif (user['hobby2']):
            count[user['hobby2']] += 1
    for hobby in count:
        print(hobby, count[hobby])
    time.sleep(1)

def add_second_hobby(users):
    for user in users:
        hobby2 = random.choice(hobbies)
        if (hobby2 == user['hobby']):
            hobby2 = random.choice(hobbies2) 
        user['hobby2'] = hobby2
    print(f'{users}')
    time.sleep(1)


if __name__ == "__main__":
    print('\n\nwelcome, adding random hobby')
    add_random_hobby(users)
    print('\ncounting hobbies..')
    count_hobbies(users)
    print('\n\nadding second hobby')
    add_second_hobby(users)
    print('\n\ncounting hobbies, now with seocnd hobby..')
    count_hobbies(users)