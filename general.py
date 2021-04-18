import random


def update_symbol(text1: bytearray, j: int, new_liter: int):
    text2 = text1
    if len(text2) == 0:
        pass
    elif len(text2) == 1:
        text2 = new_liter
    else:
        text1[j] = new_liter
    return text2


def update_symbol_text(text1: str, j: int, new_liter: str):
    text2 = text1
    if len(text2) == 0:
        pass
    elif len(text2) == 1:
        text2 = new_liter
    else:
        if j == 0:
            text2 = new_liter + text2[1:]
        elif j == text2[len(text2) - 1]:
            text2 = text2[0: len(text2) - 1] + new_liter
        else:
            text2 = text2[0: j] + new_liter + text2[j + 1:]
    return text2


def list_to_str(array: list):
    res = ''
    for i in range(len(array)):
        res += str(array[i])
        res += ' '
    return res


def reading(path: str):
    filename = path
    # with open(filename, 'r', encoding="utf-8") as file:
    with open(filename, 'rb') as file:
        local_text = file.read()
    local_text = bytearray(local_text)
    file.close()
    return local_text


def reading_text(path: str):
    filename = path.encode("ISO-8859-1")
    with open(filename, 'r', encoding="utf-8") as file:
        local_text = file.read()
    file.close()
    return local_text


def writing_main(path: str, text: bytearray):
    filename = path
    print()
    with open(filename, 'wb') as file:
        file.write(text)
    file.close()


def writing(path: str, text: bytearray):
    print("Перазаписать изначальный файл?")
    print("0 - нет")
    print("1 - да")
    print("2 - записать результат в другой файл")
    users_answer = int(input())
    new_path = ''
    if users_answer == 2:
        print("Введите путь к файлу вывода:")
        new_path = input()
    elif users_answer == 1:
        new_path = path
    else:
        return
    writing_main(new_path, text)


def writing_main_text(path: str, text: str):
    filename = path.encode("ISO-8859-1")
    print(10)
    print(text)
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
    file.close()


def writing_text(path: str, text: str):
    print("Вывести результат в тот же файл, откуда он считан (изначальное содежимое удаляется)?")
    print("0 - Вывести в другой файл")
    print("1 - Вывести в тот же файл")
    print("2 - Никуда не выводить")
    users_answer = int(input())
    new_path = ''
    if users_answer == 0:
        print("Введите путь к файлу вывода:")
        new_path = input()
    elif users_answer == 1:
        new_path = path
    else:
        return
    writing_main_text(new_path, text)


def caesar_chiefer_main_cycle(local_text, local_shift_pattern, local_alphabet_liter_number, local_alphabet_number_liter):
    size = len(local_alphabet_number_liter)
    for i in range(len(local_text)):
        symbol = local_text[i]
        if symbol in local_alphabet_liter_number:
            number = local_alphabet_liter_number[symbol]
            new_number = (number + (local_shift_pattern % size)) % size
            if new_number % size == 0:
                new_number = size
            new_symbol = local_alphabet_number_liter[new_number]
            local_text = update_symbol(local_text, i, new_symbol)
    return local_text


def caesar_chiefer_main_cycle_text(local_text, local_shift_pattern, local_alphabet_liter_number, local_alphabet_number_liter):
    size = len(local_alphabet_number_liter)
    for i in range(len(local_text)):
        symbol = local_text[i]
        if symbol in local_alphabet_liter_number:
            number = local_alphabet_liter_number[symbol]
            new_number = (number + (local_shift_pattern % size)) % size
            if new_number % size == 0:
                new_number = size
            new_symbol = local_alphabet_number_liter[new_number]
            local_text = update_symbol_text(local_text, i, new_symbol)
    return local_text


def print_or_not_print(local_text, flag1):
    if flag1:
        print("Вывести байтовый код переданного файла?")
    else:
        print("Вывести результат работы?")
    print("1 - да")
    print("0 - нет")
    users_answer = int(input())
    if users_answer == 1:
        if flag1:
            print("БАйтовый код переданного файла:")
        else:
            print("Результат работы:")
        print(local_text)


def print_or_not_print_text(local_text, flag1):
    if flag1:
        print("Вывести переданный текст?")
    else:
        print("Вывести результат работы?")
    print("0 - нет")
    print("1 - да")
    users_answer = int(input())
    if users_answer == 1:
        if flag1:
            print("Введённый текст:")
        else:
            print("Результат работы:")
        print(local_text)


def caesar_cipher(flag, alphabet_liter_number, alphabet_number_liter):
    size = len(alphabet_liter_number)
    print("Выбранный шифр - шифр Цезаря")
    print("Введите сдвиг")
    shift_pattern = int(input())
    print()
    # print("Enter the path to the file")
    # print("Введите текст")
    # local_text = input()
    print("Введите путь к файлу:")
    path = input()
    local_text = reading(path)
    # print("type", type(local_text))
    local_text = bytearray(local_text)
    print_or_not_print(local_text,True)
    if flag:
        local_text = caesar_chiefer_main_cycle(local_text, shift_pattern, alphabet_liter_number, alphabet_number_liter)
    else:
        local_text = caesar_chiefer_main_cycle(local_text, -shift_pattern, alphabet_liter_number, alphabet_number_liter)
    # print("Вывести результат работы?")
    # users_answer = bool(input())
    print_or_not_print(local_text, False)
    writing(path, local_text)
    print("Количество символов равно ", len(local_text), ', ', "сдвиг равен ", shift_pattern, sep='')


def caesar_cipher_without_talks(flag, alphabet_liter_number, alphabet_number_liter, shift_pattern, local_text):
    size = len(alphabet_liter_number)
    if flag:
        local_text = caesar_chiefer_main_cycle(local_text, shift_pattern, alphabet_liter_number, alphabet_number_liter)
    else:
        local_text = caesar_chiefer_main_cycle(local_text, -shift_pattern, alphabet_liter_number, alphabet_number_liter)
    return local_text


def caesar_cipher_without_talks_text(flag, alphabet_liter_number, alphabet_number_liter, shift_pattern, local_text):
    size = len(alphabet_liter_number)
    if flag:
        local_text = caesar_chiefer_main_cycle_text(local_text, shift_pattern, alphabet_liter_number, alphabet_number_liter)
    else:
        local_text = caesar_chiefer_main_cycle_text(local_text, -shift_pattern, alphabet_liter_number, alphabet_number_liter)
    return local_text



def get_opposite_word(word, alphabet_liter_number, alphabet_number_liter):
    res = list([])
    size = len(alphabet_number_liter)
    # print(word)
    for i in range(len(word)):
        letter = word[i]
        if letter in alphabet_liter_number:
            letter_number = alphabet_liter_number[letter]
            new_letter_number = ((size - (letter_number - 1)) + 1) % size
            if new_letter_number == 0:
                new_letter_number = size
            new_letter = alphabet_number_liter[new_letter_number]
            res.append(new_letter)
    return res


def vigenere_cipher_main_cycle(alphabet_liter_number, alphabet_number_liter, text: bytearray, key: list):
    res = bytearray([])
    length = len(key)
    size = len(alphabet_liter_number)
    for i in range(length):
        # print(text[i], text[i] in alphabet_liter_number)
        if text[i] in alphabet_liter_number:
            text_liter_number = alphabet_liter_number[text[i]] - 1
            key_liter_number = alphabet_liter_number[key[i]] - 1
            res_liter_number = (text_liter_number + key_liter_number) % size + 1
            res.append(alphabet_number_liter[res_liter_number])
        else:
            res.append(text[i])
    return res


def reading_array():
    s = input()
    s = list(s.split())
    for i in range(len(s)):
        s[i] = int(s[i])
    return s


def reading_key():
    print("Введите ключевое слово (последовательность чисел из отрезка [0: 255] через пробел")
    key = reading_array()
    print()
    return key


def vigenere_cipher(flag, alphabet_liter_number, alphabet_number_liter):
    size = len(alphabet_liter_number)
    print("Выбранный шифр - шифр Вижинера")
    # print("Введите ключевое слово (последовательность чисел из отрезка [0: 255] через пробел")
    key = reading_key()
    # print(2)
    print("Введённое ключевое слово - ", list_to_str(key))
    old_key = key
    first_key_len = len(key)
    if not flag:
        key = get_opposite_word(key, alphabet_liter_number, alphabet_number_liter)
    # print("Введите текст")
    # text = input()
    print("Введите путь к файлу:")
    path = input()
    text = reading(path)
    first_text_len = len(text)
    # print("Введённый текст:")
    # print(text)
    print_or_not_print(text, True)
    print("type", type(key))
    if len(key) < len(text):
        i = 0
        while len(key) < len(text):
            key.append(key[i % first_key_len])
            i += 1
    elif len(key) > len(text):
        i = 0
        while len(text) < len(key):
            # text += text[i % first_text_len]
            text.append(i % first_text_len)
            i += 1
    length = len(text)
    res = vigenere_cipher_main_cycle(alphabet_liter_number, alphabet_number_liter, text, key)
    print_or_not_print(res[0: first_text_len], False)
    writing(path, res[0: first_text_len])
    print("Количество символов равно", first_text_len, ',', "ключевое слово -", list_to_str(old_key[0: first_key_len]), sep=' ')


def get_random_word(n, alphabet_number_liter):
    size = len(alphabet_number_liter)
    res = list([])
    for i in range(n):
        rand_number = random.randint(1, size)
        res.append(alphabet_number_liter[rand_number])
    return res


def vernam_cipher(flag, alphabet_liter_number, alphabet_number_liter):
    size = len(alphabet_number_liter)
    print("Выбранный шифр - шифр Вернама")
    # print("Введите текст")
    # text = input()
    print("Введите путь к файлу:")
    path = input()
    text = reading(path)
    print_or_not_print(text, True)
    big_key = ''
    if flag:
        key = get_random_word(len(text), alphabet_number_liter)
        length = len(text)
        res = vigenere_cipher_main_cycle(alphabet_liter_number, alphabet_number_liter, text, key)

        big_key = key
    else:
        # print("Введите ключевое слово")
        key = reading_key()
        key = get_opposite_word(key, alphabet_liter_number, alphabet_number_liter)
        res = vigenere_cipher_main_cycle(alphabet_liter_number, alphabet_number_liter, text, key)
        big_key = key
    print_or_not_print(res, False)
    writing(path, res)
    print("Количество символов равно", len(res), ',', "ключевое слово -", list_to_str(big_key), sep=' ')


def delta_count(frequencies, new_frequencies):
    res = 0
    for element in frequencies:
        value = frequencies[element]
        new_value = new_frequencies[element]
        # print(element, value, new_value)
        delta = abs(value - new_value)
        res += delta
    return res


def copy(a: bytearray):
    b = bytearray([])
    for i in range(len(a)):
        b.append(a[i])
    return b

def check_for_analysis(text1, key, frequencies, alphabet_liter_number, alphabet_number_liter):
    text = copy(text1)
    new_text = caesar_cipher_without_talks(True, alphabet_liter_number, alphabet_number_liter, key, text)
    new_frequencies = dict({})
    for element in frequencies:
        new_frequencies[element] = 0
    size = len(alphabet_number_liter)
    length = len(text)
    for i in range(length):
        symbol = new_text[i]
        if symbol in frequencies:
            new_frequencies[symbol] += 1
    for element in new_frequencies:
        new_frequencies[element] = (new_frequencies[element]) / length
    sum_delta = delta_count(frequencies, new_frequencies)
    # print(key, new_text, sum_delta, new_frequencies)
    return sum_delta


def check_for_analysis_text(text, key, frequencies, alphabet_liter_number, alphabet_number_liter):
    new_text = caesar_cipher_without_talks_text(True, alphabet_liter_number, alphabet_number_liter, key, text)
    new_frequencies = dict({})
    for element in frequencies:
        new_frequencies[element] = 0
    size = len(alphabet_number_liter)
    length = len(text)
    for i in range(length):
        symbol = new_text[i]
        if symbol in frequencies:
            new_frequencies[symbol] += 1
    for element in new_frequencies:
        new_frequencies[element] = (new_frequencies[element]) / length
    sum_delta = delta_count(frequencies, new_frequencies)
    # print(key, new_text, sum_delta, new_frequencies)
    return sum_delta



print("Я вас категорически приветствую!")
frequencies = dict({})
while True:
    print("Выберите режим работы, введя соответствующую цифру:")
    print("1 - режим шифрования")
    print('2 - режим дешифрования')
    print('3 - режим взлома (для взлома доступен только шифр Цезаря)')
    mode = int(input())
    if not (mode in {1, 2, 3}):
        print("Неверный ввод")
        exit(0)
    alphabet_liter_number = dict({})
    alphabet_number_liter = dict({})
    frequencies = dict({})
    for i in range(256):
        alphabet_liter_number[i] = i + 1
    size = 256
    alphabet_number_liter = dict({})
    for item in alphabet_liter_number.items():
        alphabet_number_liter[item[1]] = item[0]

    if mode == 1:
        print("Выберите режим шифрования, введя соответствущую цифру:")
        print('1 - шифр Цезаря')
        print('2 - шифр Виженера')
        print('3 - шифр Вернама')
        operating_mode = int(input())

        if operating_mode == 1:  # Caesar
            caesar_cipher(True, alphabet_liter_number, alphabet_number_liter)

        elif operating_mode == 2:
            vigenere_cipher(True, alphabet_liter_number, alphabet_number_liter)

        elif operating_mode == 3:
            vernam_cipher(True, alphabet_liter_number, alphabet_number_liter)

        else:
            print("Неверный ввод")

    elif mode == 2:
        print("Выберите режим дешифрования, введя соответствущую цифру:")
        print('1 - шифр Цезаря')
        print('2 - шифр Виженера')
        print('3 - шифр Вернама')
        operating_mode = int(input())

        if operating_mode == 1:
            caesar_cipher(False, alphabet_liter_number, alphabet_number_liter)

        elif operating_mode == 2:
            vigenere_cipher(False, alphabet_liter_number, alphabet_number_liter)

        elif operating_mode == 3:
            vernam_cipher(False, alphabet_liter_number, alphabet_number_liter)

        else:
            print("Неверный ввод")

    elif mode == 3:
        alphabet_liter_number = dict(
            {'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Д': 5, 'Е': 6, 'Ё': 7, 'Ж': 8, 'З': 9, 'И': 10, 'Й': 11, 'К': 12,
             'Л': 13, 'М': 14,
             'Н': 15, 'О': 16, 'П': 17, 'Р': 18, 'С': 19, 'Т': 20, 'У': 21, 'Ф': 22, 'Х': 23, 'Ц': 24, 'Ч': 25,
             'Ш': 26,
             'Щ': 27, 'Ъ': 28, 'Ы': 29, 'Ь': 30, 'Э': 31, 'Ю': 32, 'Я': 33, 'а': 34, 'б': 35, 'в': 36, 'г': 37,
             'д': 38,
             'е': 39, 'ё': 40, 'ж': 41, 'з': 42, 'и': 43, 'й': 44, 'к': 45, 'л': 46, 'м': 47, 'н': 48, 'о': 49,
             'п': 50, 'р': 51,
             'с': 52, 'т': 53, 'у': 54, 'ф': 55, 'х': 56, 'ц': 57, 'ч': 58, 'ш': 59, 'щ': 60, 'ъ': 61, 'ы': 62,
             'ь': 63,
             'э': 64, 'ю': 65, 'я': 66})
        frequencies = dict({'а': 8.01, 'б': 1.59, 'в': 4.54, 'г': 1.70,
                            'д': 2.98,
                            'е': 8.45, 'ё': 0.04, 'ж': 0.94, 'з': 1.65, 'и': 7.35, 'й': 1.21, 'к': 3.49, 'л': 4.40,
                            'м': 3.21, 'н': 6.70, 'о': 10.97,
                            'п': 2.81, 'р': 4.73,
                            'с': 5.47, 'т': 6.26, 'у': 2.62, 'ф': 0.26, 'х': 0.97, 'ц': 0.48, 'ч': 1.44, 'ш': 0.73,
                            'щ': 0.36, 'ъ': 0.04, 'ы': 1.90,
                            'ь': 1.74,
                            'э': 0.32, 'ю': 0.64, 'я': 2.01})
        for element in frequencies:
            value = frequencies[element]
            frequencies[element] = 0.01 * value
        size = len(alphabet_liter_number)

        print("Итак, ваш алфавит:")
        for item in alphabet_liter_number.items():
            print("{:<8}".format(item[0]), end=' ')
        print()
        for item in alphabet_liter_number.items():
            print("{:<8}".format(item[1]), end=' ')
        print()

        print("Мощность равна", size)
        alphabet_number_liter = dict({})
        for item in alphabet_liter_number.items():
            alphabet_number_liter[item[1]] = item[0]
        print("Предупреждение: теперь все буквы алфавита будут в одном регистре")
        size = len(alphabet_liter_number)
        # print("Выбранный шифр - шифр Цезаря")
        # print("Enter the path to the file")
        # print("Введите текст")
        # text = input()
        print("Введите путь к файлу:")
        path = input()
        text = reading_text(path)
        print_or_not_print_text(text, True)
        text = text.lower()
        print("Частотность букв общеупотребительного русского языка известна:")
        for item in frequencies.items():
            print("{:<8}".format(item[0]), end=' ')
        print()
        for item in frequencies.items():
            print("{:<8}".format(item[1]), end=' ')
        print()
        print("Содержит ли ваш текст большое количество необщеупотребительной лексики и(или) ваш текст содержит мало алфавитных символов?")
        print("1 - да")
        print("0 - нет")
        vocabulary_type = int(input())
        if vocabulary_type == 0:
            print("Скорее всего, анализ даст верный ответ")
        else:
            print("Велика вероятность, что анализ ошибётся")

        sum_delta = 0
        optimal_key = 0
        lowered_alphabet_liter_number = dict({})
        j = 0
        for element in alphabet_liter_number:
            if element.lower() == element:
                j += 1
                lowered_alphabet_liter_number[element] = j
        lowered_alphabet_number_liter = dict({})
        j = 0
        for element in alphabet_number_liter:
            liter = alphabet_number_liter[element]
            if liter.lower() == liter:
                j += 1
                lowered_alphabet_number_liter[j] = liter
        true_len = 0
        for i in range(len(text)):
            if text[i] in alphabet_liter_number:
                true_len += 1
        for k in range(len(alphabet_liter_number)):
            current_sum_delta = check_for_analysis_text(text, k, frequencies, lowered_alphabet_liter_number,
                                                   lowered_alphabet_number_liter)
            current_sum_delta = current_sum_delta / true_len
            if k == 0:
                sum_delta = current_sum_delta
            if current_sum_delta < sum_delta:
                optimal_key = k
                sum_delta = current_sum_delta
        res = caesar_cipher_without_talks_text(True, lowered_alphabet_liter_number, lowered_alphabet_number_liter,
                                          optimal_key, text)
        print_or_not_print_text(res, False)
        writing_text(path, res)
        print("Количество символов равно", len(res), ',', "предполагаемый  ключ равен", optimal_key, ',',
              "среднее отклонение по тексту равно (в долях 1)", sum_delta, sep=' ')
    else:
        print("Неверный ввод")

    print("Хотите продолжить работу?")
    print("0 - нет")
    print("1 - да")
    users_answer = int(input())
    if users_answer == 0:
        print("До свидания!")
        break
    else:
        print("Продолжаем работу...")
        continue
