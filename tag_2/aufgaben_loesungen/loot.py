inventory = {"potion": 2, "shield": 1, "map": 2, "knife": 3}
loot = {"potion": 2, "map": 1, "food": 1}

inventory_new = {}
for key in loot | inventory:
    inventory_new[key] = inventory.get(key, 0) + loot.get(key, 0)
