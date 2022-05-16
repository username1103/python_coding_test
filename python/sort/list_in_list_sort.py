array = [("바나나", 2), ("딸기", 1), ("포도", 3)]


def setting(data):
    return data[1]


result = sorted(array, key=setting)
print(result)
