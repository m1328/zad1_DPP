# funkcja 1:
def is_palindrome(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]


print(is_palindrome("Kaja k"))

# funkcja 2:
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence[n-1]

print(fibonacci(5))

# funkcja 3:
def count_vowels(text):
    suma = 0
    text = text.lower()
    for letter in text:
        if letter in "aeiouy":
            suma += 1
    return suma


print(count_vowels("Ala"))

# funkcja 4:
def calculate_discount(price, discount):
    if discount > 1 or discount < 0:
        raise ValueError("Wrong discount")
    return price * (1-discount)

print(calculate_discount(100,0.2))

# funkcja 5:
def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list += flatten_list(item)
        else:
            flat_list.append(item)
    return flat_list

print(flatten_list([1, [2, 3], [4, [5]]]))

# funkcja 6:
def word_frequencies(text):
    text = text.lower()
    text_cleaned = ''.join(ch if ch.isalpha() or ch.isspace() else ' ' for ch in text)

    words_dict = {}
    for word in text_cleaned.split():
        words_dict[word] = words_dict.get(word, 0) + 1
    return words_dict

print(word_frequencies("Tekst, tekst! Ala ma kota. Ala? KOTA!!! Ala ala"))

#funkcja 7:
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n % i ==0:
            return False
    return True

print(is_prime(8))
print(is_prime(9))
print(is_prime(3))


