from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline

def roll_die(num_sides=6):
    return randint(1, num_sides)

results = [roll_die(6) for _ in range(5000)]
values = list(range(1, 6+1))
frequencies = [results.count(v) for v in values]

data = [Bar(x=values, y=frequencies)]
layout = Layout(
    title="Rolling one D6 — 5000 rolls",
    xaxis={'title': 'Face'},
    yaxis={'title': 'Frequency'}
)

offline.plot({'data': data, 'layout': layout}, filename='d6_5000.html')
