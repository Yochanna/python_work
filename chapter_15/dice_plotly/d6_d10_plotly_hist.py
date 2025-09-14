from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline

def roll(n): return randint(1, n)

rolls = 10_000
die1, die2 = 6, 10
results = [roll(die1) + roll(die2) for _ in range(rolls)]

min_sum, max_sum = 2, die1 + die2
x_vals = list(range(min_sum, max_sum + 1))
freqs = [results.count(v) for v in x_vals]

bars = Bar(x=x_vals, y=freqs, hovertext=[f"Sum {x}, {f} times" for x, f in zip(x_vals, freqs)])
layout = Layout(
    title=f"Rolling a D{die1} + D{die2} — {rolls} rolls",
    xaxis={'title': 'Sum'},
    yaxis={'title': 'Frequency'}
)

offline.plot({'data': [bars], 'layout': layout}, filename='d6_d10_sums.html')
