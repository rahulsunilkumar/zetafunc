import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import mpmath
import plotly.graph_objs as go
import time

# Set up Streamlit app
def main():
    st.title("Exploring the Riemann Hypothesis: Visualizing Non-Trivial Zeros")
    st.write("This app visualizes the non-trivial zeros of the Riemann zeta function along the critical line (Re(s) = 0.5).")

    # Sidebar configuration for user inputs
    st.sidebar.header("Parameters")
    st.sidebar.write("Adjust the parameters below to explore different parts of the zeta function's critical line.")
    max_imaginary = st.sidebar.slider("Maximum Imaginary Part", 10, 100, 40, 5)
    precision = st.sidebar.slider("Precision (Decimal Places)", 5, 50, 15, 5)

    # Set mpmath precision
    mpmath.mp.dps = precision

    # Calculate the zeta zeros based on user input
    zeros = find_riemann_zeros(max_imaginary)

    # Visualization
    st.write("## Non-Trivial Zeros of the Riemann Zeta Function")
    plot_zeros_with_animation(zeros)

    # Explanation and references
    st.write("### Explanation")
    st.markdown(
        "The **Riemann zeta function** is a complex-valued function that plays a key role in number theory. This app visualizes the non-trivial zeros along the critical line where the real part of \(s\) is 0.5.")
    st.write("### References")
    st.markdown("- [Riemann Hypothesis - Wikipedia](https://en.wikipedia.org/wiki/Riemann_hypothesis)")


# Function to find non-trivial zeros
@st.cache
def find_riemann_zeros(max_imaginary):
    zeros = []
    for t in np.linspace(0, max_imaginary, 1000):
        s = 0.5 + t * 1j
        value = mpmath.zeta(s)
        if abs(value) < 1e-5:  # Approximate zero check
            zeros.append((mpmath.re(s), mpmath.im(s)))
    return zeros


# Plot zeros with animation using Plotly for interactivity
def plot_zeros_with_animation(zeros):
    re_vals, im_vals = zip(*zeros)

    # Create figure
    fig = go.Figure()

    # Add trace with all data points for smoother animation
    fig.add_trace(go.Scatter(
        x=re_vals,
        y=im_vals,
        mode='markers',
        marker=dict(size=5, color='blue')
    ))

    # Update layout for better visualization
    fig.update_layout(
        title='Non-Trivial Zeros of the Riemann Zeta Function',
        xaxis=dict(title='Real Part (Re(s))'),
        yaxis=dict(title='Imaginary Part (Im(s))'),
        showlegend=False
    )

    # Add frames for animation
    frames = [
        go.Frame(data=[go.Scatter(x=re_vals[:i], y=im_vals[:i])])
        for i in range(1, len(re_vals) + 1, 10)
    ]

    fig.update(frames=frames)

    # Add animation settings
    fig.update_layout(updatemenus=[{
        "buttons": [
            {
                "args": [None, {"frame": {"duration": 50, "redraw": True}, "fromcurrent": True}],
                "label": "Play",
                "method": "animate"
            },
            {
                "args": [[None], {"frame": {"duration": 0, "redraw": False}, "mode": "immediate", "transition": {"duration": 0}}],
                "label": "Pause",
                "method": "animate"
            }
        ],
        "direction": "left",
        "pad": {"r": 10, "t": 87},
        "showactive": False,
        "type": "buttons"
    }])

    # Plot figure
    st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()
