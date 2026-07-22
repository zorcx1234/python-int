def filter_integer_data(values):
    """Entferne aus einer Sequenz alle Elemente, die kein Integer sind."""
    return [el for el in values if isinstance(el, int)]


result = filter_integer_data(["3", 4, 2, 3.3, 89])
print(result)

assert filter_integer_data(["a", 3, 1, 3.3]) == [3, 1]
assert filter_integer_data([1, 2, 3]) == [1, 2, 3]
assert filter_integer_data([1.1, 2.2, 3.3]) == []
assert filter_integer_data(["x", True, 5]) == [True, 5]  # bei isinstance()
assert filter_integer_data(["x", None, [], {}, 7]) == [7]
assert filter_integer_data([]) == []


def check_values(values, interval):
    """Prüfe, ob Werte im geschlossenen Intervall vorhanden sind."""
    a, b = interval
    return all(a <= value <= b for value in values)


values = [2, 2.2, 4, 2.3, 1.1]
interval = (1, 5.2)

result = check_values(values, interval)
print(f"Die Daten sind korrekt: {result}")

assert check_values([2, 2.2, 4, 2.3], (1, 5.3)) is True
assert check_values([2, 2.2, 4, 2.3, 0.1], (1, 5.3)) is False
assert check_values([1, 5.3], (1, 5.3)) is True
assert check_values([1.0, 3.2, 5.3], (1, 5.3)) is True
assert check_values([0.99], (1, 5.3)) is False
assert check_values([5.31], (1, 5.3)) is False
assert check_values([], (1, 5.3)) is True
