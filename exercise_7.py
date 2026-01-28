#magic cube

cube = [
    [5, 5, 4],
    [4, 5, 6],
    [6, 5, 4]
]


sum_list = [sum(row) for row in cube]
print("Sum of each row:", sum_list)

col_sum = 0
for row in range(len(cube)):
    for col in range(len(cube)):
        print(cube[col][row])
        col_sum += cube[col][row]
    sum_list.append(col_sum)
    col_sum = 0

print("Sum updated:", sum_list)

diagonal_sum = 0
for row in range(len(cube)):
    for col in range(len(cube)):
        if row == col:
            print(cube[col][row])
            diagonal_sum += cube[col][row]
    
sum_list.append(diagonal_sum)
diagonal_sum = 0

print("Sum updated:", sum_list)


for row in range(len(cube)-1,-1,-1):
    for col in range(len(cube)):
        if row + col == len(cube) - 1:
            print("last sum", cube[row][col])
            diagonal_sum += cube[row][col]
    
sum_list.append(diagonal_sum)
print("Sum updated:", sum_list)

print("len ", len(cube))

min = min(sum_list)
max = max(sum_list)


cost_min = 0
cost_max = 0
for element in sum_list:
    cost_min += abs(min - element)
    cost_max += abs(max - element)

min_costs = [cost_min, cost_max]
