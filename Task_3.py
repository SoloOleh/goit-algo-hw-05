import timeit

def boyer_moore(text, pattern):
    def build_shift_table(pattern):
        table = {}
        length = len(pattern)
        for index, char in enumerate(pattern[:-1]):
            table[char] = length - index - 1
        table.setdefault(pattern[-1], length)
        return table
    
    shift_table = build_shift_table(pattern)
    i = 0
    
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))
    return -1

def kmp(main_string, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    
    lps = compute_lps(pattern)
    i = j = 0
    while i < len(main_string):
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(main_string) and pattern[j] != main_string[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def rabin_karp(main_string, substring):
    def polynomial_hash(s, base=256, modulus=101):
        n = len(s)
        hash_value = 0
        for i, char in enumerate(s):
            power_of_base = pow(base, n - i - 1, modulus)
            hash_value = (hash_value + ord(char) * power_of_base) % modulus
        return hash_value
    
    substring_length = len(substring)
    main_string_length = len(main_string)
    base = 256
    modulus = 101
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)
    h_multiplier = pow(base, substring_length - 1, modulus)
    
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i+substring_length] == substring:
                return i
        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus
    return -1


# Зчитування вмісту статей
with open("шлях до стаття 1.txt", "r", encoding="iso-8859-1") as f:
    text1 = f.read()

with open("шлях до стаття 2.txt", "r", encoding="iso-8859-1") as f:
    text2 = f.read()

# Два різних підрядки для пошуку
real = "алгоритм"
fake = "qwerty"
pattern1 = real
pattern2 = fake

# Виміри часу для статті 1
print("Стаття 1:")
print(f"Бойєр-Мур ('{pattern1}'):    ", timeit.timeit(lambda: boyer_moore(pattern1, text1), number=1000))
print(f"Кнут-Морріс-Пратт ('{pattern1}'):", timeit.timeit(lambda: kmp(pattern1, text1), number=1000))
print(f"Рабін-Карп ('{pattern1}'):       ", timeit.timeit(lambda: rabin_karp(pattern1, text1), number=1000))
print(f"Бойєр-Мур ('{pattern2}'):    ", timeit.timeit(lambda: boyer_moore(pattern2, text1), number=1000))
print(f"Кнут-Морріс-Пратт ('{pattern2}'):", timeit.timeit(lambda: kmp(pattern2, text1), number=1000))
print(f"Рабін-Карп ('{pattern2}'):       ", timeit.timeit(lambda: rabin_karp(pattern2, text1), number=1000))

# Виміри часу для статті 2
print("\nСтаття 2:")
print(f"Бойєр-Мур ('{pattern1}'):    ", timeit.timeit(lambda: boyer_moore(pattern1, text2), number=1000))
print(f"Кнут-Морріс-Пратт ('{pattern1}'):", timeit.timeit(lambda: kmp(pattern1, text2), number=1000))
print(f"Рабін-Карп ('{pattern1}'):       ", timeit.timeit(lambda: rabin_karp(pattern1, text2), number=1000))
print(f"Бойєр-Мур ('{pattern2}'):    ", timeit.timeit(lambda: boyer_moore(pattern2, text2), number=1000))
print(f"Кнут-Морріс-Пратт ('{pattern2}'):", timeit.timeit(lambda: kmp(pattern2, text2), number=1000))
print(f"Рабін-Карп ('{pattern2}'):       ", timeit.timeit(lambda: rabin_karp(pattern2, text2), number=1000))