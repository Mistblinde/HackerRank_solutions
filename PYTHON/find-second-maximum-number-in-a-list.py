if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()[:n])
    arr = list(arr)

    arr.sort()
    # arr_new = []
    # arr2 = [arr_new[i] for i in arr if i not in arr_new]

    arr_new = []
    for num in arr:
        if num not in arr_new:
            arr_new.append(num)

    arr_new_len = len(arr_new)
    print(arr_new)
    print(arr_new_len)
    print(arr_new[arr_new_len-2])

#Q:
#What is map in our case?
#What is the aim of using it?