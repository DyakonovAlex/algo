def find_simple(txt: str, pattern: str) -> int:
    # Обычный перебор
    result = -1

    txt_len = len(txt)
    pattern_len = len(pattern)
    t = 0
    last = pattern_len - 1
    while t < txt_len - last:
        p = 0
        while p <= last and txt[t + p] == pattern[p]:
            p += 1
        if p == pattern_len:
            return t
        t += 1

    return result


def rfind_simple(txt: str, pattern: str) -> int:
    # Обычный перебор. Правое вхождение
    rtxt = txt[::-1]
    rpattern = pattern[::-1]

    result = -1

    txt_len = len(rtxt)
    pattern_len = len(rpattern)
    t = 0
    last = pattern_len - 1
    while t < txt_len - last:
        p = 0
        while p <= last and rtxt[t + p] == rpattern[p]:
            p += 1
        if p == pattern_len:
            return txt_len - (t + pattern_len)
        t += 1

    return result


def find_reverse(txt: str, pattern: str) -> int:
    # Оптимизация 1: поиск начинаем с последнего
    result = -1

    t = 0
    last = len(pattern) - 1
    txt_len = len(txt)
    while t < txt_len - last:
        p = last
        while p >= 0 and txt[t + p] == pattern[p]:
            p -= 1
        if p == -1:
            return t
        t += 1

    return result


def create_shift(pattern: str) -> list:
    # Создание массива сдвигов
    pattern_len = len(pattern)
    result = [pattern_len] * 128
    for p in range(pattern_len - 1):
        result[ord(pattern[p])] = pattern_len - p - 1
    return result


def find_shift(txt: str, pattern: str) -> int:
    # Алгоритм Бойера-Мура-Хорспула: для каждого символа прописываем смещение
    result = -1
    shift = create_shift(pattern)
    t = 0
    last = len(pattern) - 1
    txt_len = len(txt)
    while t < txt_len - last:
        p = last
        while p >= 0 and txt[t + p] == pattern[p]:
            p -= 1
        if p == -1:
            return t
        t += shift[ord(txt[t + last])]

    return result


def create_suffix(pattern) -> dict:
    # Создание словаря суффиксов
    result: dict = dict()
    pattern_len = len(pattern)
    all_suffix = dict()

    s = ""
    for p in range(pattern_len - 1, 0, -1):
        s = pattern[p] + s
        all_suffix[s] = pattern_len
        if not result.get(pattern[p], 0):
            result[pattern[p]] = pattern_len - p - 1

    for k in all_suffix:
        v = rfind_simple(pattern[0: pattern_len - 1], k)
        # Ключи извлекаются в том же порядке, что и добавлялись
        # Если ключа в строке нет, то можно больше не проверять
        if v == -1:
            break
        result[k] = pattern_len - len(k) - v

    return result


def find_suffix(txt: str, pattern: str) -> int:
    # Алгоритм Бойера Мура: используем суффиксы.
    result = -1
    suffix = create_suffix(pattern)
    t = 0
    last = len(pattern) - 1
    txt_len = len(txt)
    while t < txt_len - last:
        p = last
        search_suffix = ""
        while p >= 0 and txt[t + p] == pattern[p]:
            search_suffix = txt[t + p] + search_suffix
            p -= 1
        if p == -1:
            return t
        # ------------------------------------
        shift_value = 0
        if not search_suffix:
            shift_value = suffix.get(txt[t + last], 0)
        while search_suffix and shift_value == 0:
            shift_value = suffix.get(search_suffix, 0)
            search_suffix = search_suffix[1:]
        # -----------------------------------
        t += shift_value if shift_value > 0 else last + 1

    return result


def main():
    print()
    print("START")
    # x = find_simple("substring", "string")
    # x = find_reverse("substring", "string")
    # x = find_shift(".kololokolokolokol.", "kolokol")
    x = find_suffix(
        ".kololokolokolokol.bc.abc.bc.c.tbcvbvc.abc.bc.c.abcbc.abc.bc.c.abc",
        "bc.abc.bc.c.abc",
    )
    print(x)
    print("END")


if __name__ == "__main__":
    main()
