# let sides be the parameter for defining the number of sides in the cube
def dice(sides):
    import random

    x = None
    rolls = 0
    while x != sides:
        x = random.randint(1, sides)
        rolls = rolls + 1
        print(f"For roll {rolls} we get side {x}")
    print(f"Therefore it took {rolls} rolls to get side {sides}")


dice(21)