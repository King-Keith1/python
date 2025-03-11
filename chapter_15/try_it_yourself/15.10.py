import plotly.graph_objects as go
from die import Die

die = Die(6)

steps = 1000
walk = [0]

for _ in range(steps):
    roll = die.roll()
    move = 1 if roll % 2 == 0 else -1  
    walk.append(walk[-1] + move)

fig = go.Figure(data=go.Scatter(x=list(range(steps + 1)), y=walk, mode='lines'))
fig.update_layout(title='Random Walk Simulation (Based on Die Rolls)',
                  xaxis_title='Steps',
                  yaxis_title='Position')
fig.show()
