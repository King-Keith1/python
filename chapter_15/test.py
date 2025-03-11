# import matplotlib.pyplot as plt
# import numpy as np

# # Group members' contributions
# contributions = [23, 39, 48, 49]

# plt.style.use('seaborn-v0_8')
# fig, ax = plt.subplots()

# # Set custom background colors
# fig.patch.set_facecolor("#ADD8E6")  # Light blue background for the figure
# ax.set_facecolor("#D3D3D3")  # Light gray background for the plot area

# # Create a histogram
# ax.hist(contributions, bins=4, color="#FF6F61", edgecolor="black", alpha=0.9, density=True)

# # Set chart title and labels with contrasting colors
# ax.set_title("404 Avengers GitHub Contributions", fontsize=16, color="black")
# ax.set_xlabel("Number of Contributions", fontsize=12, color="black")
# ax.set_ylabel("Percentage of Total", fontsize=12, color="black")

# # Customize grid lines for visibility
# ax.grid(color="white", linestyle="--", linewidth=0.6, alpha=0.8)

# # Display the histogram
# plt.show()

import numpy as np
import plotly.graph_objects as go

np.random.seed(42)
rounds = 1000  
wins_per_round = np.random.randint(0, 10, size=rounds)  

fig = go.Figure()


fig.add_trace(go.Histogram(
    x=wins_per_round,
    nbinsx=10,
    marker=dict(
        color='#FF6F61',  
        line=dict(color='black', width=2), 
        opacity=0.9
    ),
    name="Wins per Round",
    hoverinfo="x+y"
))

fig.update_layout(
    title="🌟 Ultra-Cool Cyberpunk Wins in Card Game 🃏",
    title_font=dict(family="Arial", size=30, color="black"),
    xaxis=dict(
        title="Number of Wins per Round",
        title_font=dict(family="Arial", size=20, color="black"),
        tickfont=dict(color="black"),
        showgrid=True,
        gridcolor="black",
        zeroline=False
    ),
    yaxis=dict(
        title="Frequency",
        title_font=dict(family="Arial", size=20, color="black"),
        tickfont=dict(color="black"),
        showgrid=True,
        gridcolor="black",
        zeroline=False
    ),
    plot_bgcolor="#D3D3D3", 
    paper_bgcolor="#ADD8E6",  
    showlegend=False,
    margin=dict(l=40, r=40, t=80, b=40),  
    font=dict(family="Arial, sans-serif", color="black", size=16),
    updatemenus=[  
        dict(
            type="buttons",
            showactive=False,
            buttons=[dict(label="Play",
                          method="animate",
                          args=[None, dict(frame=dict(duration=500, redraw=True), fromcurrent=True)])]
        )
    ],
)

fig.show()
