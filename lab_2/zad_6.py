# zad_6
def lists(a: list, b: list) -> list:
    result = set(a + b)
    result2 = []
    for i in result:
        result2.append(i**3)
    return result2


print(lists([1, 2, 3, 4], [4, 4, 2, 5, 6]))
