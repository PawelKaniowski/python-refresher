houses = [
    "Eric's house",
    "Kenny's house",
    "Kyle's house",
    "Stan's house"
]


def deliver_presents_iteratively():
    for house in houses:
        print("Delivering presents to", house)


def deliver_presents_recursively(houses):
    if len(houses) == 1:
        print("Delivering presents to", houses[0])
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # first elf
        deliver_presents_recursively(first_half)
        # second elf
        deliver_presents_recursively(second_half)
