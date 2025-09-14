import matplotlib.pyplot as plt
from datetime import datetime

x = list(range(1, 21))
y = [n**2 for n in x]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=3)

ax.set_title("Squares (saved)", fontsize=18)
ax.set_xlabel("Value")
ax.set_ylabel("Value²")

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"squares_{stamp}.png"
plt.savefig(filename, bbox_inches='tight')  # saves to your folder
plt.show()  # also pops up
