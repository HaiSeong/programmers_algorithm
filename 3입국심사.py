def solution(n, times):
    start = 0
    end = 9000000000000
    result = 0

    while start <= end:
        mid = (start + end) // 2

        person = 0
        for time in times:
            person += mid // time

        if person >= n:
            end = mid - 1
            result = mid
        else:
            start = mid + 1

    print(result)
    return result