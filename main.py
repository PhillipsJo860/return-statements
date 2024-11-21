# Joshua Phillips
# 11/19/24
# Return statement pracrtice

def describe_vacation(destination, activety, season='Summer'):
    print(f'I will visit {destination} in order to do some {activety}, while the {season} is in the air.')

destination1 = describe_vacation('44 Miller Road', 'Ghost Hunting')

destination2 = describe_vacation('13 Willow Street', 'Ghost Hunting', 'Blood Moon')


def show_major(first_name, university, major='Sports Medicine'):
    person = (f'{first_name} attends the {university} and is majoring in {major}.')
    return None

person1 = show_major('Carlos', 'University of Miller', 'Ghosties')
print(person1)

person2 = show_major('Usato', 'University of Llinger Kingdom')
print(person2)
