# %%

def say_hello():
    print("hello")

say_hello()

# %%

def calculate_circle_area(r):
    area = 3.14 * (r ** 2)
    return area

def calculate_circle_circumference(r):
    return 2 * 3.14 * r

area = calculate_circle_area(788)
print(f"area: {area:.2f}")

circumference = calculate_circle_circumference(788)
print(f"circumference: {circumference:.2f}")

# %%

# need to complete sometime later
def transpose_matrix(matrix):
    pass

# %%

def transpose_matrix(matrix):
    transposed = []
    for i in range(4):
        tr = []
        for row in matrix:
            tr.append(row[i])
        transposed.append(tr)

    return transposed

def print_matrix(matrix = []):
    for el in matrix:
        print(el)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print("matrix:")
print_matrix(matrix)

print()
print("transposed matrix:")
res = transpose_matrix(matrix)
print_matrix(res)

# %%

def matrix_multiply_scalar(matrix, scalar = 1):
    res = []
    for row in matrix:
        res.append([cell * scalar for cell in row])

    return res

def print_matrix(matrix = []):
    for el in matrix:
        print(el)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print("matrix:")
print_matrix(matrix)

print()

print(f"matrix * scalar {1}:")
res1 = matrix_multiply_scalar(matrix)
print_matrix(res1)

print()

print(f"matrix * scalar {3}:")
res2 = matrix_multiply_scalar(matrix, scalar=3)
print_matrix(res2)

# %% optional, positional, keyword only argument

res3 = matrix_multiply_scalar(scalar=4)
print_matrix(res3)
