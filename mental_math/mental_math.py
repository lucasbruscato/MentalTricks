
import os
import time
import datetime
import numpy as np

############ CHANGE HERE ############
choice = 'addition' # multiplication division addition subtraction
number_of_practices = 30 # np.inf for all random elements
time_for_response = 2 # in seconds

# first number of operation
initial_range_1 = 3
final_range_1 = 9
# initial_range_1 = 11
# final_range_1 = 99

# second number of operation
initial_range_2 = 3
final_range_2 = 9
#initial_range_2 = 11
#final_range_2 = 99

# personal study path
## multiplication 1-by-1
## addition 1-by-1, 2-by-2, 3-by-2, 3-by-3
## subtraction 2-by-2, 3-by-2, 3-by-3
## multiplication 2-by-1, 3-by-1, 2-by-2
## division 3-by-1, 4-by-1, 3-by-2
####################################

all_pairs = []
tried_pairs = []

for i in range(initial_range_1, final_range_1 + 1):
    for j in range(initial_range_2, final_range_2 + 1):
        all_pairs.append([i, j])

if number_of_practices == np.inf or number_of_practices > len(all_pairs):
    number_of_practices = len(all_pairs) + 1
else:
    number_of_practices += 1

beginning_time = datetime.datetime.now()

print("Length of all pairs: " + str(len(all_pairs)))
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

    print(str(times) + ' - say ' + str(random_number_1) + sign + str(random_number_2))
    os.system('say ' + str(random_number_1) + voice + str(random_number_2))
    time.sleep(time_for_response)

    print('say ' + str(answer) + '\n')
    os.system('say ' + str(answer))

print("Length of tried pairs: " + str(len(tried_pairs)))
print("Tried pairs:")
print(sorted(tried_pairs, key=lambda x: (x[0], x[1])))
print('\n')

print("Begin: " + str(beginning_time))
ending_time = datetime.datetime.now()
print("End: " + str(ending_time))
print("Total time:" + str(ending_time - beginning_time))
print('\n')
