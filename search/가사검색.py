from bisect import bisect_left, bisect_right

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]


def findIndex(query, direction):
    if direction == 'r':
        result = len(query)
    else:
        result = 0

    start = 0
    end = len(query)
    while start <= end:
        mid = (start + end) // 2
        if mid == len(query):
            result = len(query)
            break
        if query[mid] == '?':
            if mid >= 0 and direction == 'r' and query[mid - 1] != '?':
                result = mid
                break
            elif mid < (len(query)-1) and direction == 'l' and query[mid + 1] != '?':
                result = mid
                break
            if direction == 'r':
                end = mid - 1
            else:
                start = mid + 1
        else:
            if direction == 'r':
                start = mid + 1
            else:
                end = mid - 1

    return result


def solution(words, queries):
    answer = []
    words.sort(key=lambda x: (len(x), x))
    for query in queries:
        direction = 'r'
        if query[0] == '?':
            direction = 'l'
        index = findIndex(query, direction)
        u = query[:index] if direction == 'r' else query[index + 1:]
        count = 0
        if direction == 'r':
            for word in words:
                if word.startswith(u) and len(word) == len(query):
                    count += 1
        elif direction == 'l':
            for word in words:
                if word.endswith(u) and len(word) == len(query):
                    count += 1
        answer.append(count)

    return answer


print(solution(words, queries))
