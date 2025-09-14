import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=3, marker='o', markersize=8)

ax.set_title("Squares (basic line)", fontsize=22)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value²", fontsize=14)
ax.tick_params(axis='both', labelsize=12)

plt.show()
