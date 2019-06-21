from typing import NewType

def hobbies(name, age: int, hobby, optional_hobbies = None, other = None):
    if (not optional_hobbies):
        optional_hobbies = ""
    if (not other):
        other = ""
    while (type(age) != int):
        try:
            int(age)
            break
        except TypeError:
            age = input('age must be a number, please enter a valid age\n')
            

    output = f'my name is {name}, my age is {age}.\nI like {hobby} {optional_hobbies}.'
    return output

if __name__ == "__main__":
    
    print(hobbies('eyal', input('please enter you age\n'), 'playing', ['basketball', 'guitar']))