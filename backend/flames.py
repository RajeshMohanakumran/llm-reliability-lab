def calculate_flames(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    l1 = list(name1)
    l2 = list(name2)

    for ch in name1:
        if ch in l2:
            l1.remove(ch)
            l2.remove(ch)

    count = len(l1) + len(l2)

    flames = ["F", "L", "A", "M", "E", "S"]

    while len(flames) > 1:
        split = (count % len(flames)) - 1

        if split >= 0:
            flames = flames[split+1:] + flames[:split]
        else:
            flames.pop()

    result_map = {
        "F": "Friends",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }

    return result_map[flames[0]]