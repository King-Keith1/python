import numpy as np
import plotly.graph_objects as go

# Simulating reshuffling in a card game
np.random.seed(42)
rounds = 1000  # Number of rounds played

# Function to reshuffle the results and update the histogram
def reshuffle_data():
    return np.random.randint(0, 10, size=rounds)  # Reshuffle to simulate new "deck" or game

# Create the initial figure with the histogram
fig = go.Figure()

# Add initial trace for the histogram (reshuffled data will be applied after the play button is clicked)
reshuffled_data = reshuffle_data()  # Initial reshuffle
fig.add_trace(go.Histogram(
    x=reshuffled_data,  # Display reshuffled data
    nbinsx=10,
    marker=dict(
        color='#FF6F61',  # Coral Red Bars
        line=dict(color='black', width=2),  # Black outline for contrast
        opacity=0.9
    ),
    name="Wins per Round",
    hoverinfo="x+y"
))

# Define the layout
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
    plot_bgcolor="#D3D3D3",  # Light Gray Plot Background
    paper_bgcolor="#ADD8E6",  # Light Blue Figure Background
    showlegend=False,
    margin=dict(l=40, r=40, t=80, b=40),
    font=dict(family="Arial, sans-serif", color="black", size=16),
    updatemenus=[  # Play button for reshuffling and starting a new game
        dict(
            type="buttons",
            showactive=False,
            buttons=[dict(
                label="Play",
                method="animate",
                args=[None, dict(
                    frame=dict(duration=500, redraw=True), 
                    fromcurrent=True,
                    mode="immediate"
                )]
            )]
        )
    ],
)

# Function to create frames with reshuffled data
def create_frames():
    reshuffled_data = reshuffle_data()  # Reshuffle the data for new game
    frames = [
        go.Frame(
            data=[go.Histogram(x=reshuffled_data[:k], nbinsx=10)], 
            name=str(k)
        ) for k in range(10, rounds + 1, 10)  # Increment by 10 each time
    ]
    return frames

# Set the frames dynamically when the Play button is clicked
fig.frames = create_frames()

fig.show()