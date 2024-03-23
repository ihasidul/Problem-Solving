from collections import OrderedDict


item_collection = OrderedDict()

for _ in range(int(input())):
    input_str = input()
    item_price = int(input_str.strip().split(" ")[-1])
    item_name = " ".join(input_str.strip().split()[:-1])

    if item_collection.get(item_name):
        item_collection[item_name] = item_collection[item_name] + item_price
    else:
        item_collection[item_name] = item_price

for item in item_collection:
    print(item, item_collection[item])
