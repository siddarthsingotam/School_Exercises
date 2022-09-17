# Faulty program, infinite loop
import random
x = random.randint(1, 6)
rolls = 0
while x != 6:
    x = random.randint(1, 6)
    rolls = rolls + 1
    print(f"For roll {rolls} we get output {x}")


