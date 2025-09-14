import matplotlib.pyplot as plt
from random_walk import RandomWalk

plt.style.use('classic')

rw = RandomWalk(20_000)
rw.fill_walk()

fig, ax = plt.subplots(figsize=(14, 8))
step_numbers = range(rw.num_points)

ax.scatter(rw.x_values, rw.y_values, c=step_numbers, cmap=plt.cm.Blues,
           s=1, edgecolors='none', zorder=1)

# Start (green) and end (red)
ax.scatter(0, 0, c='green', s=80, edgecolors='none', zorder=2)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=80, edgecolors='none', zorder=2)

# Clean presentation
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_title("Random Walk — start (green) to end (red)", fontsize=16)

plt.show()
