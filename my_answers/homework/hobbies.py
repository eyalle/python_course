import sys, random
sys.path.append("../../")
from exercises.data import get_data
from statistics import median
import my_answers.homework.HW1_7_19


users = get_data(20)

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
allHobbies = list(set(hobbies + hobbies2))

def addHobby(hobbies_list):
    user_hobby = 'hobby'
    if (hobbies_list == hobbies2):
        user_hobby = 'hobby2'
    for user in users:
        random_hobby = allHobbies[random.randint(0, len(allHobbies)-1)]
        user[user_hobby] = random_hobby

def find_avg_age():
    avg = {'count': 0, 'sum': 0}
    for user in users:
        avg['sum'] += user['age']
        avg['count'] += 1

    print(f'the average age is: {avg["sum"]/avg["count"]}')

def common_name():
    names = {user['name']: 0 for user in users}
    for user in users:
        names[user['name']] += 1
    max_age = max(names.values())
    for k, v in names.items():
        if (v == max_age):
            print(f'most common name is {k}')
            break
    
def get_median_user():
    median_age = median(user['age'] for user in users)
    print(f'the median users age is {median_age}')

def count_hobbies(users):
    count = {hobby: 0 for hobby in allHobbies}
    for user in users:
        if (user['hobby']):
            count[user['hobby']] += 1
        elif (user['hobby2']):
            count[user['hobby2']] += 1
    for hobby in count:
        print(hobby, count[hobby])

if __name__ == "__main__":
    # print(users)
    addHobby(hobbies)
    # print(f'\n\n{users}')
    find_avg_age()
    common_name()
    get_median_user()
    count_hobbies(users)
    addHobby(hobbies2)
    count_hobbies(users)
