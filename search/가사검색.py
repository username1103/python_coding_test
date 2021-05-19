from bisect import bisect_left, bisect_right

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]


def solution(words, queries):
    result = []
    for i in range(len(queries)):
        query = queries[i]
        index = query.find("?")
        isReverse = False
        if index == 0:
            isReverse = True
            query = query[::-1]
            index = query.find("?")
        count = 0
        for word in words:
            if isReverse:
                if len(word) == len(query) and (word[::-1])[:index] == query[:index]:
                    count += 1
            else:
                if len(word) == len(query) and word[:index] == query[:index]:
                    count += 1

        result.append(count)

    return result


print(solution(words, queries))
