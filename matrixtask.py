import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

#read the matrix
result = ""
for i in range(m):
    for j in range(n):
        result += matrix[j][i]

# Replace the special characters between two alphanumeric characters with a single space
final_result = re.sub(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', ' ', result)   

# Print the result
print(final_result)