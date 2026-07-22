# 1. Count vowels
def count_vowels(word):
    """Count the number of german vowels in a Word."""
    vowels = "aeiouüöä"
    return len([char for char in word.lower() if char in vowels])


number_of_vocals = count_vowels("teleport")
print(number_of_vocals)

assert count_vowels("teleport") == 3
assert count_vowels("Ööll") == 2
assert count_vowels("Auge") == 3
assert count_vowels("Python") == 1
assert count_vowels("AEIOU") == 5
assert count_vowels("äöü") == 3
assert count_vowels("") == 0
assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0


# 3. Filter
def filter_input(values, accepted):
    """Filter Function."""
    return [value for value in values if value in accepted]


values = ["gold", "gelb", "gelb", "rot", "gelb"]
accepted = ["gelb", "rot"]
input_filtered = filter_input(values, accepted)
print(input_filtered)


# 4. Umdrehen
def reverse_cutter(n):
    # Diese Version ist schwer les- und verstehbar
    # Petersburg
    # [-2:0:-1]: starte bei index len(string)-2 (r)
    # gehe zu 0 (exkusive) (e)
    # und gehe rückwärts (-1)
    return n[-2:0:-1].lower()


def reverse_cutter_better(n):
    """Besser lesbar"""
    # umdrehen und lowercase
    n = n.lower()[::-1]

    # erstes und letztes Zeichen rausschneiden
    return n[1:-1]


assert reverse_cutter("Petersburg") == "rubsrete"
assert reverse_cutter("Python") == "ohty"
assert reverse_cutter("Hallo") == "lla"
assert reverse_cutter("AB") == ""
assert reverse_cutter("A") == ""
assert reverse_cutter("") == ""
assert reverse_cutter("Test") == "se"
assert reverse_cutter("Äpfel") == "efp"


# 5. max
def max_value(values):
    if not values:
        return None

    max_ = values.pop(0)
    for value in values:
        if value > max_:
            max_ = value
    return max_


max_val = max_value([100, 2, 3, 1, 99, -1, 109])
print("max value: ", max_val)

assert max_value([100, 2, 3, 1, 99, -1, 109]) == 109
assert max_value([1]) == 1
assert max_value([-5, -10, -2, -8]) == -2
assert max_value([0, -1, -2]) == 0
assert max_value([-100]) == -100
assert max_value([5, 5, 5]) == 5
assert max_value([-3, 7, -1, 4]) == 7
assert max_value([]) is None


# 6. Median
def median(values):
    values_sorted = sorted(values)
    index = len(values_sorted) // 2
    # wenn anzahl ungerade
    if len(values_sorted) % 2:
        median = values_sorted[index]
    else:
        median = values_sorted[index - 1 : index + 1]
        median = sum(median) / 2
    return median


assert median([1, 2, 3]) == 2
assert median([1, 2, 3, 4]) == 2.5
assert median([1, 2, 4, 8, 3, 19]) == 3.5
assert median([42]) == 42
assert median([-10, -5, 5, 10]) == 0.0


# 7. Schwellenwertfunktion
def heaviside(i):
    """Schwellenwertfunktion."""
    if i >= 0:
        return 1
    return 0


heavisides = [heaviside(i) for i in range(-10, 11)]
print("heavesides:", heavisides)


def clamp(value: float, minimum: float, maximum: float) -> float:
    """Begrenzt einen Wert auf einen vorgegebenen Bereich."""
    return max(minimum, min(value, maximum))


print(clamp(50, 0, 100))  # 50
print(clamp(-10, 0, 100))  # 0
print(clamp(120, 0, 100))  # 100
print(clamp(42, 20, 40))  # 40
