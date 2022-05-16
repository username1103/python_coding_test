# 2020 카카오 신입 공채 1차
# [본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]

# 친구들로부터 천재 프로그래머로 불리는 프로도는
# 음악을 하는 친구로부터 자신이 좋아하는 노래 가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는지 궁금하니
# 프로그램으로 개발해 달라는 제안을 받았습니다.
# 그 제안 사항 중, 키워드는 와일드카드 문자중 하나인 '?'가 포함된 패턴 형태의 문자열을 뜻합니다.
# 와일드카드 문자인 '?'는 글자 하나를 의미하며, 어떤 문자에도 매치된다고 가정합니다.
# 예를 들어 "fro??"는 "frodo", "front", "frost" 등에 매치되지만 "frame", "frozen"에는 매치되지 않습니다.

# 가사에 사용된 모든 단어들이 담긴 배열 words와 찾고자 하는 키워드가 담긴 배열 queries가 주어질 때,
# 각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환하도록 solution 함수를 완성해 주세요.

# 가사 단어 제한사항
# words의 길이(가사 단어의 개수)는 2 이상 100,000 이하입니다.
# 각 가사 단어의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
# 전체 가사 단어 길이의 합은 2 이상 1,000,000 이하입니다.
# 가사에 동일 단어가 여러 번 나올 경우 중복을 제거하고 words에는 하나로만 제공됩니다.
# 각 가사 단어는 오직 알파벳 소문자로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.
# 검색 키워드 제한사항

# queries의 길이(검색 키워드 개수)는 2 이상 100,000 이하입니다.
# 각 검색 키워드의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
# 전체 검색 키워드 길이의 합은 2 이상 1,000,000 이하입니다.
# 검색 키워드는 중복될 수도 있습니다.
# 각 검색 키워드는 오직 알파벳 소문자와 와일드카드 문자인 '?' 로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.
# 검색 키워드는 와일드카드 문자인 '?'가 하나 이상 포함돼 있으며, '?'는 각 검색 키워드의 접두사 아니면 접미사 중 하나로만 주어집니다.
# 예를 들어 "??odo", "fro??", "?????"는 가능한 키워드입니다.
# 반면에 "frodo"('?'가 없음), "fr?do"('?'가 중간에 있음), "?ro??"('?'가 양쪽에 있음)는 불가능한 키워드입니다.

# 입출력 예
# ["frodo", "front", "frost", "frozen", "frame", "kakao"]
# ["fro??", "????o", "fr???", "fro???", "pro?"]

# [3, 2, 4, 1, 0]


from bisect import bisect_left, bisect_right

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

# words를 길이 별로 구분하여 담을 list
array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]


def count_by_range(a, left_value, right_value):
    right_value = bisect_right(a, right_value)
    left_value = bisect_left(a, left_value)
    return right_value - left_value


def solution(words, queries):
    answer = []

    # words를 각각으 길이에 맞게 분류하여 list에 담아줌
    # reveresd_array는 O????와 같은 query를 해결하기 위함
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    # 길이 별로 분류된 모든 word들을 오름차순으로 정렬
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    # 모든 쿼리들에 대해서
    for query in queries:
        # ?로 시작하는 경우에는 길이가 같은 word들을 모아논 array에서 query에 ?를 a로 변환한 것과 z로 변환한 것이 들어갈
        # 인덱스의 차이를 얻어옴
        if query[0] != '?':
            res = count_by_range(array[len(query)], query.replace(
                '?', 'a'), query.replace('?', 'z'))
        # ?로 시작하지 않는 경우 reversed_array를 이용해 query를 뒤집어 같은 방식으로 진행
        else:
            res = count_by_range(reversed_array[len(
                query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))

        answer.append(res)

    return answer


print(solution(words, queries))
