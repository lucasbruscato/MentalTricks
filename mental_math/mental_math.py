
import os
import time
import numpy as np

############ CHANGE HERE ############
choice = 'multiplication' # multiplication division addition subtraction
number_of_practices = np.inf # np.inf for all random elements

# first number of operation
initial_range_1 = 6
final_range_1 = 10

# second number of operation
initial_range_2 = 5
final_range_2 = 10

time_for_response = 2 # in seconds
####################################

all_pairs = []
tried_pairs = []

for i in range(initial_range_1, final_range_1):
    for j in range(initial_range_2, final_range_2):
        all_pairs.append([i, j])

if number_of_practices == np.inf:
    number_of_practices = len(all_pairs)
else:
    number_of_practices += 1

print("Length of all_pairs: " + str(len(all_pairs)))
print("All pairs: \n")
print(all_pairs)

for times in range(1, number_of_practices):
    pair = np.random.randint(0, len(all_pairs))

    random_number_1, random_number_2 = all_pairs[pair]
    tried_pairs.append(all_pairs[pair])
    all_pairs.pop(pair)

    if choice == 'multiplication':
        answer = random_number_1 * random_number_2
        sign = ' x '
        voice = ' vezes '
    elif choice == 'division':
        answer = random_number_1 / random_number_2
        sign = ' / '
        voice = ' dividido '
    elif choice == 'addition':
        answer = random_number_1 + random_number_2
        sign = ' + '
        voice = ' mais '
    elif choice == 'subtraction':
        answer = random_number_1 - random_number_2
        sign = ' - '
        voice = ' menos '

    print('say ' + str(random_number_1) + sign + str(random_number_2))
    os.system('say ' + str(random_number_1) + voice + str(random_number_2))
    time.sleep(time_for_response)

    print('say ' + str(answer) + '\n')
    os.system('say ' + str(answer))


print("Tried pairs: \n")
print(sorted(tried_pairs, key=lambda x: (x[0], x[1])))

# personal study path
## multiplication 1-by-1
## addition 2-by-2, 3-by-2, 3-by-3
## subtraction 2-by-2, 3-by-2, 3-by-3
## multiplication 2-by-1, 3-by-1, 2-by-2
## division 3-by-1, 4-by-1, 3-by-2
