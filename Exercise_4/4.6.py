import random

numbers_of_points = int(input(("Enter a high value integer : ")))
points_inside_circle = 0
for x in range(numbers_of_points) :
    p_x = random.uniform(-1,1)
    p_y = random.uniform(-1,1)
    if p_x ** 2  +  p_y ** 2  < 1:
        points_inside_circle = points_inside_circle + 1
    else:
        continue

pi_approx = ((4 * points_inside_circle)/numbers_of_points)
print("Approximate value of Pi value is :", pi_approx)