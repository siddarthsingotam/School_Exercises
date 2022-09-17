

















sys.exit(0)

import sys


def pizza(cost, d):
    f = cost / (3.14*(d/2)**2)
    return f

f1 = round(pizza(10, 8),2)
print(f1)

sys.exit(0)