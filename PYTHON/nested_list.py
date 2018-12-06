# if __name__ == '__main__':
#     range_loop = int(input())
#     lst = [[str, float] for _ in range(range_loop)]
#     for i in range(range_loop):
#         name = input()
#         score = float(input())
#         lst[i][0] = name
#         lst[i][1] = score
#     print(lst)
#     lst_sorted = sorted(lst, key=lambda x: x[1])
#     print(lst_sorted)
#
#     # check if there are the same score
#     for i in range(range_loop - 1):
#         if lst_sorted[i][1] == lst_sorted[i + 1][1]:
#             print(lst_sorted[i][0])
#             print(lst_sorted[i + 1][0])
#
#     print(lst_sorted[1][0])
if __name__ == '__main__':
    lst = []
    range_input = int(input())
    for _ in range(range_input):
        name = input()
        score = float(input())
        lst.append([name, score])

    second_score_lst = sorted(lst, key=lambda x: x[1])
    print(second_score_lst)
    second_score = [score for name, score in second_score_lst][1]
    print(second_score)
    print('\n'.join([a for a, b in sorted(lst) if b == second_score]))

"""
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
"""
# marksheet = []
# for _ in range(0, int(input())):
#     marksheet.append([input(), float(input())])
#
# second_highest = sorted(list(set([marks for name, marks in marksheet])))
# print(second_highest)
# print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))
