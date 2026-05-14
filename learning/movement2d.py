import random
from src.vec.vec2 import Vec2
from src.draw_vertices import draw
from src.signal_filters import median_filter, calculate_mse, outliers_filter, moving_average_filter

trajectory = []

for y in range(-50, 50):
    x = random.gauss(0, 0.2)
    vec = Vec2(x, y/25)
    trajectory.append(vec)

removed_outliers = outliers_filter([vec.x for vec in trajectory])
# new_x = median_filter([vec.x for vec in trajectory], 10)
new_x = moving_average_filter(removed_outliers, 10)

trajectory_filtered = []
for i, vec in enumerate(trajectory):
    trajectory_filtered.append(Vec2(new_x[i], vec.y))

i = 0
showing = trajectory
filtered = False
def get_trajectory():
    global i, showing, filtered
    if i > len(showing) - 1:
        if filtered:
            showing = trajectory
            filtered = False
        else:
            showing = trajectory_filtered
            filtered = True

        i = 0

    vec = showing[i]
    i += 1
    return [[vec.x, vec.y]]

# TODO, create circle with sin and cos, add noise, and then smooth it out

# create many points with t val that is between 0 and 1
# x = cos(t)
# y = sin(t)

mse = calculate_mse([1,2,3], [1, 4, 2])
# print("MSE:", mse)

filtered_mse = calculate_mse([0 for _ in trajectory], [vec.x for vec in trajectory_filtered])
print(filtered_mse)

draw(get_trajectory)