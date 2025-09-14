import matplotlib.pyplot as plt
from random import choices

x_vals, y_vals = [0], [0]
max_points = 30_000
stop_radius = 400  # stop early if we wander far

# Bias: more chance to step +1 than -1
def step():
    # weighted choices: (value, weight)
    dx = choices([-1, 0, 1], weights=[3, 2, 5])[0]
    dy = choices([-1, 0, 1], weights=[3, 2, 5])[0]
    return dx, dy

while len(x_vals) < max_points:
    dx, dy = step()
    if dx == 0 and dy == 0:
        continue
    x_vals.append(x_vals[-1] + dx)
    y_vals.append(y_vals[-1] + dy)
    if abs(x_vals[-1]) + abs(y_vals[-1]) > stop_radius:
        break

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(14, 8))
ax.plot(x_vals, y_vals, linewidth=1)
ax.scatter(x_vals[0], y_vals[0], c='green', s=80, edgecolors='none')
ax.scatter(x_vals[-1], y_vals[-1], c='red', s=80, edgecolors='none')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_title("Biased Random Walk (stop when far enough)", fontsize=16)
plt.show()
