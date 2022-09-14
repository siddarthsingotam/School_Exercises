def dice():
    import random
    x = None
    rolls = 0
    while x != 6:
        x = random.randint(1, 6)
        rolls = rolls + 1
        print(f"For roll {rolls} we get output {x}")
    print(f"Therefore it took {rolls} rolls to get 6")

dice()