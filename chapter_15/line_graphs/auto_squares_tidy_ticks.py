import matplotlib.pyplot as plt

x = range(1, 1001)
y = [n**2 for n in x]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.scatter(x, y, s=8, c='dodgerblue', alpha=0.7, edgecolors='none')

ax.set_title("Squares (1–1000)", fontsize=22)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Value²", fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=10)

# Zoom slightly past the data so dots aren’t glued to edges
ax.axis([0, 1050, 0, (1000**2)*1.05])

plt.show()
