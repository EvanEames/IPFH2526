import random

def load_functions():
    return [
        {
            "function": "def add_numbers(a, b):\n    result = _____ + _____\n    return result\n\nprint(add_numbers(____, ____))",
            "options": ["a", "b", "a=3", "4"],
            "solutions": ["a", "b", "a=3", "4"]
        },
        {
            "function": "def count_elements(lst):\n    count = 0\n    for elem in ____:\n        count += 1\n    return count\n\nprint(count_elements([____]))",
            "options": ["lst", "1, 2, 3, 4"],
            "solutions": ["lst", "1, 2, 3, 4"]
        },
        {
            "function": "def multiply_list(lst):\n    product = 1\n    for num in ____:\n        product *= num\n    return product\n\nprint(multiply_list([____]))",
            "options": ["lst", "1, 2, 3, 4"],
            "solutions": ["lst", "1, 2, 3, 4"]
        },
        {
            "function": "def disp_last_character(s):\n    last_character = s[____]\n    return last_character\n\nprint(reverse_string(____))",
            "options": ["-1", "'hello'"],
            "solutions": ["-1", "'hello'"]
        },
        {
            "function": "def check_key(d, key):\n    if ____ in ____:\n        return True\n    return False\n\nprint(check_key({____}, 'age'))",
            "options": ["d", "key", "'name': 'Alice', 'age': 25"],
            "solutions": ["d", "key", "'name': 'Alice', 'age': 25"]
        },
        {
            "function": "def find_max(lst):\n    max_val = ____\n    for num in lst:\n        if num > max_val:\n            max_val = num\n    return max_val\n\nprint(find_max([____]))",
            "options": ["float('-inf')", "1, 2, 3, 4"],
            "solutions": ["float('-inf')", "1, 2, 3, 4"]
        },
        {
            "function": "def calculate_average(lst):\n    total = sum(____)\n    average = total / len(lst)\n    return average\n\nprint(calculate_average([____]))",
            "options": ["lst", "10, 20, 30, 40"],
            "solutions": ["lst", "10, 20, 30, 40"]
        },
        {
            "function": "def is_even(____):\n    return num % 2 == ____\n\nprint(is_even(____))",
            "options": ["num", "0", "4"],
            "solutions": ["num", "0", "4"]
        },
        {
            "function": "def filter_even_numbers(lst):\n\tfor num in lst:\n\t\tif num % ____ == 0:\n\t\t\tevens.append(____)\n    return evens\n\nprint(filter_even_numbers([____]))",
            "options": ["2", "num", "1, 2, 3, 4, 5, 6"],
            "solutions": ["2", "num", "1, 2, 3, 4, 5, 6"]
        },
        {
            "function": "def find_min(lst):\n    min_val = ____\n    for num in lst:\n        if num < min_val:\n            min_val = num\n    return min_val\n\nprint(find_min([____]))",
            "options": ["float('inf')", "7, 3, 9, 1"],
            "solutions": ["float('inf')", "7, 3, 9, 1"]
        },
        {
            "function": "def concatenate_strings(s1, s2):\n    return s1 + ____\n\nprint(concatenate_strings(____, ____))",
            "options": ["s2", "s1='Hello, '", "'World!'"],
            "solutions": ["s2", "s1='Hello, '", "'World!'"]
        },
        {
            "function": "def find_length(s):\n    return len(____)\n\nprint(find_length(____))",
            "options": ["s", "'Python'"],
            "solutions": ["s", "'Python'"]
        },
        {
            "function": "def calculate_bmi(weight, height, und_value, norm_value):\n    bmi = weight / (____ ** 2)\n    if bmi < ____:\n        return 'Underweight'\n    elif bmi < ____:\n        return 'Normal weight'\n    else:\n        return 'Overweight'\n\nprint(calculate_bmi(____, ____, ____, ____))",
            "options": ["height", "und_value", "norm_value", "1.75", "weight=80", "18.5", "25"],
            "solutions": ["height", "und_value", "norm_value", "ov_value", "weight=80", "1.75", "18.5", "25"]
        },
        {
            "function": "def find_duplicates(lst):\n    seen = set()\n    duplicates = set()\n    for item in ____:\n        if item in ____:\n            duplicates.add(item)\n        else:\n            seen.add(____)\n    return duplicates\n\nprint(find_duplicates([____]))",
            "options": ["lst", "seen", "item", "1, 2, 3, 2, 4, 1"],
            "solutions": ["lst", "seen", "item", "1, 2, 3, 2, 4, 1"]
        },
        {
            "function": "def calculate_power(base, exp):\n    result = 1\n    for _ in range(____):\n        result *= ____\n    return result\n\nprint(calculate_power(____, ____))",
            "options": ["exp", "base", "base=2", "3"],
            "solutions": ["exp", "base", "base=2", "3"]
        },
        {
            "function": "def find_index(lst, target):\n    for i in range(len(____)):\n        if lst[____] == ____:\n            return i\n    return -1\n\nprint(find_index([____], ____))",
            "options": ["lst", "i", "target", "10, 20, 30, 40", "30"],
            "solutions": ["lst", "i", "target", "10, 20, 30, 40", "30"]
        },
        {
            "function": "def guess_the_number(secret, guess):\n    if guess < ____:\n        return 'Too low'\n    elif guess > ____:\n        return 'Too high'\n    else:\n        return 'Correct!'\n\nprint(guess_the_number(____, ____))",
            "options": ["secret", "secret", "50", "guess=30"],
            "solutions": ["secret", "secret", "50", "guess=30"]
        },
        {
            "function": "def categorize_age(age):\n    if age < ____:\n        return 'Child'\n    elif age < ____:\n        return 'Teen'\n    elif age < ____:\n        return 'Adult'\n    else:\n        return 'Senior'\n\nprint(categorize_age(____))",
            "options": ["13", "20", "65", "age=45"],
            "solutions": ["13", "20", "65", "age=45"]
        },
        {
            "function": "def word_count(sentence):\n    words = sentence.split(____)\n    count = 0\n    for word in ____:\n        count += 1\n    return count\n\nprint(word_count(____))",
            "options": ["' '", "words", "'This is a sample sentence'"],
            "solutions": ["' '", "words", "'This is a sample sentence'"]
        },
        {
            "function": "def determine_pass_fail(score, passing_score):\n    if score >= ____:\n        return 'Pass'\n    else:\n        return 'Fail'\n\nprint(determine_pass_fail(____, ____))",
            "options": ["passing_score", "50", "85"],
            "solutions": ["passing_score", "85", "passing_score=50"]
        },
        {
            "function": "def temperature_advice(temp, cold_temp=15, hot_temp=30):\n    if temp < ____:\n        return 'It is cold, wear a jacket.'\n    elif temp > ____:\n        return 'It is hot, stay hydrated.'\n    else:\n        return 'The temperature is comfortable.'\n\nprint(temperature_advice(____))",
            "options": ["cold_temp", "hot_temp", "25"],
            "solutions": ["cold_temp", "hot_temp", "25"]
        },
        {
            "function": "from random import randint\ndef roulette(x, ___):\n    if x < y:\n        first_res = randint(____,____)\n        second_res = randint(____,____)\n    else:\n        return _____\n    return first_res, second_res\n\na = 3\n\nroulette(____, ____)",
            "options": ["y", "x", "x", "y", "y", "'This function needs the first number to be lower than the second'",
                        "a", "5"],
            "solutions": ["y", "x", "y", "x", "y", "'This function needs the first number to be lower than the second'",
                          "a", "5"]
        },
        {
            "function": "def shopping_list(items):\n    for item in ____:\n        print(f'You need to buy {____}')\n    return f'Total items: {len(____)}'\n\nprint(shopping_list([____]))",
            "options": ["items", "item", "items)", "'milk', 'eggs', 'bread', 'butter'"],
            "solutions": ["items", "item", "items)", "'milk', 'eggs', 'bread', 'butter'"]
        },
        {
            "function": "def travel_time(distance, speed):\n    if speed <= 0:\n        return 'Speed must be greater than ____'\n    time = ____ / ____\n    return f'Travel time is {____}.'\n\nprint(travel_time(____, ____))",
            "options": ["0", "distance", "speed", "time", "speed=150", "50"],
            "solutions": ["0", "distance", "speed", "time", "50", "speed=150"]
        },
        {
            "function": "def detect_even_odd(numbers):\n    evens = []\n    odds = []\n    for num in ____:\n        if num % ____ == 0:\n            evens.append(num)\n        else:\n            odds.append(____)\n    return evens, odds\n\nprint(detect_even_odd([____]))",
            "options": ["numbers", "2", "num", "1, 2, 3, 4, 5, 6, 7"],
            "solutions": ["numbers", "2", "num", "1, 2, 3, 4, 5, 6, 7"]
        }
    ]

def run_exercise():
    functions = load_functions()
    for idx, func in enumerate(functions):
        print(f"Function {idx + 1}:")
        print(func["function"])
        print("Options:")
        options = func["options"]
        random.shuffle(options)
        for i, opt in enumerate(options, start=1):
            print(f"{i}. {opt}")

        user_answers = []
        for _ in func["solutions"]:
            user_input = input("Fill in the blank: ")
            user_answers.append(user_input)

        correct = 0
        for user, solution in zip(user_answers, func["solutions"]):
            if user == solution:
                correct += 1

        score = (correct / len(func["solutions"])) * 100
        print(f"Your score: {score:.2f}%")

        if score < 100:
            retry = input("Do you want to try this function again? (yes/no): ").lower()
            if retry == "yes":
                continue

        next_func = input("Do you want to move on to the next function? (yes/no): ").lower()
        if next_func != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    run_exercise()
