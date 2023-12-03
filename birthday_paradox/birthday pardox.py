import random 
import datetime

def getBirthDays(numOfBirthDay):
    birthdays = []
    for i in range(numOfBirthDay):
        startOfYear = datetime.date(2001 , 1 , 1)
        randomNumOfDays = datetime.timedelta(random.randint(0,365))
        birthday = startOfYear + randomNumOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    for a , birthdayA in enumerate(birthdays):
        for b , birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA

print('''
    The Birthday Paradox shows us that in a group of N people, the odds
    42. that two of them have matching birthdays is surprisingly large.
    43. This program does a Monte Carlo simulation (that is, repeated random
    44. simulations) to explore this concept.
''')

Months = ('Jan' , 'Feb' , 'Mar' , 'Apr' ,
          'May' , 'June' , 'July' , 'Aug' ,
          'Sep' , 'Oct' , 'Nov' , 'Dec')

while True:
    print('How many birthday shall I generate? (Max 100): ')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numDays = int(response)
        break
    else:
        print('Invalid!')

print()
        
print('Here are' , numDays , 'Birthdays:')

birthdays = getBirthDays(numDays)

for i , birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end = '')
    monthName = Months[birthday.month - 1]
    datetext = f'{monthName} {birthday.day}'
    print(datetext)

print()
print()

match = getMatch(birthdays)

if match != None:
    monthName = Months[match.month - 1]
    datetext = f'{monthName} {match.day}'
    print('Multiple people have a birthday on: ' , datetext)
else:
    print('There are no matching birthdays!')

print() 

print('Generating' , numDays , 'random birthdays 100_000 times...')
print('Press Enter to begin...')

simMatch = 0
for i in range(100_000):
    if i % 100_000 == 0:
        print(i , 'simulation run...')
    birthdays = getBirthDays(numDays)
    if getMatch(birthdays) != None:
        simMatch += 1
print('100,000 simulations run.')

probability = round(simMatch / 100_000 * 100 , 2)

print(f'''
      Out of 100,000 simulations of {numDays} people, there was a 
      matching birthday in that group {simMatch} times. This means that
      {numDays} people have a {probability}% chance of having a matching
      birthday in their group. 
      That\'s more than you think!
      ''')
        