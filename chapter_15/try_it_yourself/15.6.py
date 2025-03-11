import plotly.express as px
import pandas as pd
from die import Die

die_1 = Die(8)
die_2 = Die(8)

rolls = [die_1.roll() + die_2.roll() for _ in range(1000)]

df = pd.DataFrame({'Sum': rolls})

fig = px.histogram(df, x="Sum", nbins=16, title="Sum of Two D8 Dice Rolls (1000 Rolls)",
                   labels={'Sum': 'Sum of Dice'}, histnorm=None)

fig.update_traces(marker=dict(line=dict(color='black', width=1)))
fig.update_layout(xaxis=dict(tickmode='linear', dtick=1))

fig.show()
