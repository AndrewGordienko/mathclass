from copy import deepcopy
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

LOOKING_FOR = 1 # the end result the code looks for
MAX_NUMBER = 1000 # from 1 to this number are searched through

x = 0
visited = []
new_x = 0
index = 0
solved = []

def get_digit(number, n):
    return number // 10**n % 10

for i in range(1, MAX_NUMBER):
    if x == LOOKING_FOR:
        solved.append(i-1)
    
    x = i
    visited = []
    new_x = 0
    index = 0
    visited.append(x)

    while x != 4 and x != 1:
        index += 1
        for i in range(len(str(x))):
            new_x += get_digit(x, i)**2

        x = new_x
        new_x = 0

        visited.append(x)

new_solved = (solved)
numbers_to_remove_1 = []
numbers_to_remove_2 = []

for i in range(len(solved)):
    temporary = str(solved[i])
    final = temporary.replace("0", "")
    solved[i] = deepcopy(int(final))

for i in range(len(solved)):
    first_number = solved[i]
    for j in range(len(solved)):
        second_number = solved[j]
    
        if first_number != second_number and len(str(first_number)) == len(str(second_number)):
            counter = 0
            for p in range(len(str(first_number))):
                for k in range(len(str(second_number))):
                    if str(first_number)[p] == str(second_number)[k]:
                        counter += 1
                        break
                
            if counter == len(str(first_number)):
                numbers_to_remove_1.append(first_number)
                numbers_to_remove_2.append(second_number)
            
        
        if len(str(first_number)) == 1 and first_number not in new_solved:
            print(first_number)
            new_solved.append(first_number)

for i in range(len(numbers_to_remove_1)):
    if numbers_to_remove_1[i] in new_solved and numbers_to_remove_2[i] in new_solved:
        new_solved.remove(numbers_to_remove_1[i])

temporary = []
for i in range(len(new_solved)):
    if new_solved[i] not in temporary:
        temporary.append(new_solved[i])
new_solved = temporary

print("-----")
print(new_solved)


tree = {}
visited = []
new_x = 0
index = 0

for j in range(len(new_solved)):
    if x == LOOKING_FOR:
        another_visited = []
        for p in range(len(visited)):
            x = list(str(visited[p]))
            if '0' in x:
                x.remove('0')

            for m in range(5):
                for i in range(1, len(x)):
                    if int(x[i]) < int(x[i - 1]):
                        temp = x[i - 1]
                        x[i - 1] = x[i]
                        x[i] = temp

            x = int("".join(x))
            if x != LOOKING_FOR:
                another_visited.append(x)
        another_visited.append(LOOKING_FOR)


        print("--")
        print("started as {} ended up as {} the journey was {}".format(new_solved[j-1], LOOKING_FOR, another_visited))

        for m in range(len(another_visited)-2, -1, -1):
            if another_visited[m+1] not in tree:
                tree[another_visited[m+1]] = []
                tree[another_visited[m+1]].append(another_visited[m])

            if another_visited[m+1] in tree:
                if another_visited[m] not in tree[another_visited[m+1]]:
                    tree[another_visited[m+1]].append(another_visited[m])

    x = new_solved[j]
    visited = []
    new_x = 0
    index = 0
    visited.append(x)

    while x != 4 and x != 1:
        index += 1
        for i in range(len(str(x))):
            new_x += get_digit(x, i)**2

        x = new_x
        new_x = 0

        visited.append(x)

node = LOOKING_FOR
step = 0
indent = " " * 4

def tree_printing(number, step):
    step += 1
    if number in tree:
        for i in range(len(tree[number])):
            print(indent * step + "↑- " + str(tree[number][i]))
            tree_printing(tree[number][i], step)

print("--")
print(LOOKING_FOR)
tree_printing(LOOKING_FOR, step)

go_to_1 = deepcopy(new_solved)

LOOKING_FOR = 4 # the end result the code looks for
MAX_NUMBER = 1000 # from 1 to this number are searched through

x = 0
visited = []
new_x = 0
index = 0
solved = []

def get_digit(number, n):
    return number // 10**n % 10

for i in range(1, MAX_NUMBER):
    if x == LOOKING_FOR:
        solved.append(i-1)
    
    x = i
    visited = []
    new_x = 0
    index = 0
    visited.append(x)

    while x != 4 and x != 1:
        index += 1
        for i in range(len(str(x))):
            new_x += get_digit(x, i)**2

        x = new_x
        new_x = 0

        visited.append(x)

new_solved = (solved)
numbers_to_remove_1 = []
numbers_to_remove_2 = []

for i in range(len(solved)):
    temporary = str(solved[i])
    final = temporary.replace("0", "")
    solved[i] = deepcopy(int(final))

for i in range(len(solved)):
    first_number = solved[i]
    for j in range(len(solved)):
        second_number = solved[j]
    
        if first_number != second_number and len(str(first_number)) == len(str(second_number)):
            counter = 0
            for p in range(len(str(first_number))):
                for k in range(len(str(second_number))):
                    if str(first_number)[p] == str(second_number)[k]:
                        counter += 1
                        break
                
            if counter == len(str(first_number)):
                numbers_to_remove_1.append(first_number)
                numbers_to_remove_2.append(second_number)
            
        
        if len(str(first_number)) == 1 and first_number not in new_solved:
            print(first_number)
            new_solved.append(first_number)

for i in range(len(numbers_to_remove_1)):
    if numbers_to_remove_1[i] in new_solved and numbers_to_remove_2[i] in new_solved:
        new_solved.remove(numbers_to_remove_1[i])

temporary = []
for i in range(len(new_solved)):
    if new_solved[i] not in temporary:
        temporary.append(new_solved[i])
new_solved = temporary

print("-----")
print(new_solved)


tree = {}
visited = []
new_x = 0
index = 0

for j in range(len(new_solved)):
    if x == LOOKING_FOR:
        another_visited = []
        for p in range(len(visited)):
            x = list(str(visited[p]))
            if '0' in x:
                x.remove('0')

            for m in range(5):
                for i in range(1, len(x)):
                    if int(x[i]) < int(x[i - 1]):
                        temp = x[i - 1]
                        x[i - 1] = x[i]
                        x[i] = temp

            x = int("".join(x))
            if x != LOOKING_FOR:
                another_visited.append(x)
        another_visited.append(LOOKING_FOR)


        print("--")
        print("started as {} ended up as {} the journey was {}".format(new_solved[j-1], LOOKING_FOR, another_visited))

        for m in range(len(another_visited)-2, -1, -1):
            if another_visited[m+1] not in tree:
                tree[another_visited[m+1]] = []
                tree[another_visited[m+1]].append(another_visited[m])

            if another_visited[m+1] in tree:
                if another_visited[m] not in tree[another_visited[m+1]]:
                    tree[another_visited[m+1]].append(another_visited[m])

    x = new_solved[j]
    visited = []
    new_x = 0
    index = 0
    visited.append(x)

    while x != 4 and x != 1:
        index += 1
        for i in range(len(str(x))):
            new_x += get_digit(x, i)**2

        x = new_x
        new_x = 0

        visited.append(x)

node = LOOKING_FOR
step = 0
indent = " " * 4

def tree_printing(number, step):
    step += 1
    if number in tree:
        for i in range(len(tree[number])):
            print(indent * step + "↑- " + str(tree[number][i]))
            tree_printing(tree[number][i], step)

print("--")
print(LOOKING_FOR)
tree_printing(LOOKING_FOR, step)

go_to_4 = deepcopy(new_solved)
