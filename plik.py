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

# funkcja 5 (do poprawy):
def flatten_list(nested_list):
    new_list = []
    for num in nested_list:
        new_list.append(num)
    return new_list

print(flatten_list([1, [2, 3], [4, [5]]]))

