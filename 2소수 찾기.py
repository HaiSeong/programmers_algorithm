from itertools import permutations


def is_prime(n):
    if n < 2:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


def solution(numbers):
    array = set()
    numbers = str(numbers)
    # print(list(permutations(numbers, 2)))
    for i in range(1, len(numbers) + 1):
        temp = list(permutations(numbers, i))
        # print(temp)
        for t in temp:
            # print(t)
            num = ''
            for j in range(i):
                num += t[j]
            array.add(int(num))
    array = list(array)

    cnt = 0
    for a in array:
        if is_prime(a) == 1:
            cnt += 1

    return cnt