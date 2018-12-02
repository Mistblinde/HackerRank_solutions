# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#

# Without list comprehensions:
# x = int(input())
# y = int(input())
# n = int(input())
#
# ar = []
# p = 0
#
# for i in range(x + 1):
#     for j in range(y + 1):
#         if i + j != n:
#             ar.append([])
#             ar[p] = [i, j]
#             p += 1
#             print(ar)


x = int(input())
y = int(input())
z = int(input())
n = int(input())

print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ((i + j +k) != n)])

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

col2 = [row[1] for row in M if row[1] % 2 == 0]
print(col2)
