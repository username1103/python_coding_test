from bisect import bisect_left, bisect_right


# a : 정렬된 배열
# left_value : 구간의 시작 값
# right_vlaue : 구간의 끝 값
def count_by_range(a, left_value, right_value):
    right_value = bisect_right(a, right_value)
    left_value = bisect_left(a, left_value)
    return right_value - left_value


if __name__ == "__main__":
    print("-----------Number-----------")
    a = sorted([1, 3, 5, 7, 2, 3, 1, 6, 4, 2, 8, 5, 3, 9])
    print("A :", a)
    left_value = 2
    right_value = 4
    print("Find value :", left_value, "~", right_value)
    print("Answer :", count_by_range(a, left_value, right_value))

    print("-----------String-----------")
    a = sorted(["book", "love", "tree", "bali", "lion", "base", "ball"])
    print("A :", a)
    left_value = "baaa"
    right_value = "bzzz"
    print("Find value :", left_value, "~",
          right_value, "즉, b로 시작하는 모든 단어의 개수를 찾겠다.")
    print("Answer :", count_by_range(a, left_value, right_value))
    print("문자열의 개수를 찾을 때는 문자열의 길이를 고려해서 사용해야 한다.")
