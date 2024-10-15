import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import mpmath
import plotly.graph_objs as go
import plotly.animation as animation
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

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=[],
        y=[],
        mode='markers',
        marker=dict(size=5, color='blue')
    ))

    fig.update_layout(
        title='Non-Trivial Zeros of the Riemann Zeta Function',
        xaxis=dict(title='Real Part (Re(s))'),
        yaxis=dict(title='Imaginary Part (Im(s))'),
        showlegend=False
    )

    # Animation loop
    for i in range(1, len(re_vals) + 1):
        fig.data[0].x = re_vals[:i]
        fig.data[0].y = im_vals[:i]
        st.plotly_chart(fig, use_container_width=True)
        time.sleep(0.01)


if __name__ == "__main__":
    main()
