if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split()[:n])
    integer_list = tuple(integer_list)

    integer_list_h = hash(integer_list)

    print(integer_list_h)
