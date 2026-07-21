from pprint import pprint


def get_dict(address_list):
    head = address_list.pop(0)
    address_dict = {}
    for row in address_list:
        address_dict[row[1]] = dict(zip(head, row))
    return address_dict


address_list = [
    (
        "salutation",
        "first_name",
        "last_name",
        "street",
        "city",
    ),
    (
        "Mr.",
        "Frodo",
        "Baggins",
        "Bag End 1",
        "Hobbiton",
    ),
    (
        "Mr.",
        "Samwise",
        "Gamgee",
        "Bagshot Row 2",
        "Hobbiton",
    ),
    (
        "Mrs.",
        "Galadriel",
        "Elb",
        "189 Flower Gardens",
        "Lothlorien",
    ),
]


address_dict = get_dict(address_list)
pprint(address_dict, depth=2)
print(address_dict["Frodo"])
print(address_dict["Frodo"]["street"])
print(address_dict["Frodo"]["last_name"])
