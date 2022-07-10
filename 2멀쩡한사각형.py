def solution(record):
    result = []
    answer = []
    table = dict()
    for r in record:
        if r[:5] == 'Enter':
            command, id, name = r.split()
            table[id] = name
            result.append([command, id])
        elif r[:6] == 'Change':
            command, id, name = r.split()
            table[id] = name
        else:
            command, id = r.split()
            result.append([command, id])

    for res in result:
        command, id = res
        if command == 'Enter':
            answer.append(table[id] + '님이 들어왔습니다.')
        elif command == 'Leave':
            answer.append(table[id] + '님이 나갔습니다.')

    return answer