WEEKEND = ("Saturday", "Sunday")
MIN_TEMPERATURE = 30

weekday_temperatures = [
    {"day": "Monday", "date": "2019-07-15", "temperature": 31},
    {"day": "Tuesday", "date": "2019-07-16", "temperature": 33},
    {"day": "Wednesday", "date": "2019-07-17", "temperature": 27},
    {"day": "Thursday", "date": "2019-07-18", "temperature": 25},
    {"day": "Friday", "date": "2019-07-19", "temperature": 30},
    {"day": "Saturday", "date": "2019-07-20", "temperature": 31},
    {"day": "Sunday", "date": "2019-07-21", "temperature": 29},
    {"day": "Monday", "date": "2019-07-22", "temperature": 25},
    {"day": "Tuesday", "date": "2019-07-23", "temperature": 31},
    {"day": "Wednesday", "date": "2019-07-24", "temperature": 26},
    {"day": "Thursday", "date": "2019-07-25", "temperature": 23},
    {"day": "Friday", "date": "2019-07-26", "temperature": 22},
    {"day": "Saturday", "date": "2019-07-27", "temperature": 23},
    {"day": "Sunday", "date": "2019-07-28", "temperature": 32},
]


def get_hot_work_days(temp: list[dict], min_temp: int) -> list[tuple]:
    return [
        (workday["date"], workday["temperature"])
        for workday in temp
        if workday["day"] not in WEEKEND
        if workday["temperature"] >= min_temp
    ]


hot_work_days = get_hot_work_days(weekday_temperatures, min_temp=MIN_TEMPERATURE)
print(hot_work_days)

assert get_hot_work_days(weekday_temperatures, 30) == [
    ("2019-07-15", 31),
    ("2019-07-16", 33),
    ("2019-07-19", 30),
    ("2019-07-23", 31),
]

assert get_hot_work_days(weekday_temperatures, 31) == [
    ("2019-07-15", 31),
    ("2019-07-16", 33),
    ("2019-07-23", 31),
]

assert get_hot_work_days(weekday_temperatures, 33) == [
    ("2019-07-16", 33),
]

assert get_hot_work_days(weekday_temperatures, 40) == []
