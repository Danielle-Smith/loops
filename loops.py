# for in loop for dictionary
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']
players = ('Altuve', 'Bregman', 'Correa', 'Gattis')

for player in players:
  print(player)

players = {
  '2b': 'Altuve',
  '3b': 'Bregman',
  'ss': 'Correa',
  'dh': 'Gattis'
}

for position, player in players.items():
  print('Position', position)
  print('Player', player)

# for in loop with a string

alphabet = 'abcdef'

for letter in alphabet:
  print(letter)

# for in loop range

for num in range(1, 10):
  print(num)

for num in range(1, 10, 2):
  print(num)

# break and continue
usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

for username in usernames:
  if username == 'cersei':
    print(f'Sorry, {username}, you are not allowed')
    continue
  else:
    print(f'{username} is allowed')

for username in usernames:
  if username == 'cersei':
    print(f'{username} was found at index {usernames.index(username)}')
    break
  print(username)

  # while loops

nums = list(range(1, 100))

while len(nums) > 0:
  print(nums.pop())

# guessing game using while loop
def guessing_game():
  while True:
    print('What is your guess?')
    guess = input()

    if guess == '42':
      print('You correctly guessed it!')
      return False
    else:
      print(f"No, {guess} isn't the answer, please try again\n")

guessing_game()

# how to combine lists with for in loop

legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

raw_db = [legacy_customers, new_customers]

print(raw_db)

for legacy_customer in legacy_customers:
  new_customers.append(legacy_customer)

print(new_customers)

# list comprehension

num_list = range(1, 11)
cubed_nums = []

# when you want to do something to each item in the range
for num in num_list:
  cubed_nums.append(num ** 3)
            #|         |                   |
cubed_nums = [num ** 3 for num in num_list]

print(cubed_nums)

# when you are picking out items in a range
even_numbers = []

for num in num_list:
  if num % 2 == 0:
    even_numbers.append(num)
             #|    |                   |               |        
even_numbers = [num for num in num_list if num % 2 == 0]

print(even_numbers)