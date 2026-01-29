#magic cube
import itertools

# 29/01/2026

cube = [
    [5, 5, 4],
    [4, 5, 6],
    [6, 5, 4]
]

# first approach to find sums of rows, columns and diagonals
# sum_list = [sum(row) for row in cube]
# print("Sum of each row:", sum_list)

# col_sum = 0
# for row in range(len(cube)):
#     for col in range(len(cube)):
#         print(cube[col][row])
#         col_sum += cube[col][row]
#     sum_list.append(col_sum)
#     col_sum = 0

# print("Sum updated:", sum_list)

# diagonal_sum = 0
# for row in range(len(cube)):
#     for col in range(len(cube)):
#         if row == col:
#             print(cube[col][row])
#             diagonal_sum += cube[col][row]
    
# sum_list.append(diagonal_sum)
# diagonal_sum = 0

# print("Sum updated:", sum_list)


# for row in range(len(cube)-1,-1,-1):
#     for col in range(len(cube)):
#         if row + col == len(cube) - 1:
#             print("last sum", cube[row][col])
#             diagonal_sum += cube[row][col]
    
# sum_list.append(diagonal_sum)
# print("Sum updated:", sum_list)
# #[14, 15, 15, 15, 15, 14, 14, 15]

# print("len ", len(cube))

# #get the min and max from the sums
# min = min(sum_list)
# max = max(sum_list)


# cost_min = 0
# cost_max = 0
# for element in sum_list:
#     cost_min += abs(min - element)
#     cost_max += abs(max - element)

# min_costs = [cost_min, cost_max]


def compute_cost(cube, target_cube):
    total_cost = 0
    for i in range(len(cube)):
        for j in range(len(cube)):
            total_cost += abs(cube[i][j] - target_cube[i][j])
    return total_cost


def generate_magic_squares():
    magic_squares = []
    for perm in itertools.permutations(range(1, 10)):
        square = [list(perm[0:3]), list(perm[3:6]), list(perm[6:9])]
        rows = [sum(row) for row in square]
        cols = [sum([square[i][j] for i in range(3)]) for j in range(3)]
        diag1 = sum([square[i][i] for i in range(3)])
        diag2 = sum([square[i][2-i] for i in range(3)])
        if all(s == 15 for s in rows + cols + [diag1, diag2]):
            magic_squares.append(square)
    return magic_squares

magic_squares = generate_magic_squares()
print("Generated magic squares:", magic_squares)

#[[[2, 7, 6], [9, 5, 1], [4, 3, 8]], [[2, 9, 4], [7, 5, 3], [6, 1, 8]], [[4, 3, 8], [9, 5, 1], [2, 7, 6]], [[4, 9, 2], [3, 5, 7], [8, 1, 6]], [[6, 1, 8], [7, 5, 3], [2, 9, 4]], [[6, 7, 2], [1, 5, 9], [8, 3, 4]], [[8, 1, 6], [3, 5, 7], [4, 9, 2]], [[8, 3, 4], [1, 5, 9], [6, 7, 2]]]

costs = []
for magic_square in magic_squares:
    cost = compute_cost(cube, magic_square)
    costs.append(cost)
    
print("Costs to convert to each magic square:", costs)
min_cost = min(costs)
print("Minimum cost to convert to a magic square:", min_cost)