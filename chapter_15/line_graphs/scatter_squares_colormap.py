import matplotlib.pyplot as plt

x = list(range(1, 51))
y = [n**2 for n in x]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
sizes = [n*2 for n in x]  # bigger number → bigger dot

sc = ax.scatter(x, y, c=y, s=sizes, cmap=plt.cm.magma, edgecolors='none')

ax.set_title("Squares (scatter with size + magma colormap)", fontsize=20)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Value²", fontsize=12)
ax.tick_params(axis='both', labelsize=10)

plt.show()
