from random import randint

def create_numbers():
    num_list = []
    length = randint(0,9)
    for i in range(0, length):
        num_list.append(randint(0,10))
    return num_list

def display_num_list(numsList):
    if (numsList):
        print(f'here is the current list:\n{numsList}\n')
    else:
        print(f'list is empty: {numsList}')

def avg_num(num_list):
    sum = 0
    for num in num_list:
        sum += num
    
    return (sum/(len(num_list)))

def print_average(num_list):
    try:
        avg = avg_num(num_list)
        print(f'the average of {num_list} is {avg}')
    except Exception as err:
        if (type(err) == ZeroDivisionError or type(err) == TypeError):
            print(f'the error is:\n{err}')
        else:
            print(f'ERR: an unkown error has occured')
    return

if __name__ == "__main__":
    numbers = create_numbers()
    # display_num_list(numbers)
    print_average(numbers)
