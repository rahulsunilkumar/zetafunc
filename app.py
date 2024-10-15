import streamlit as st
import numpy as np
import mpmath
import plotly.graph_objs as go

# Set up Streamlit app
def main():
    st.title("Exploring the Riemann Hypothesis: Visualizing Non-Trivial Zeros")
    st.write("This app visualizes the non-trivial zeros of the Riemann zeta function along the critical line (Re(s) = 0.5).")

    # Sidebar configuration for user inputs
    st.sidebar.header("Parameters")
    st.sidebar.write("Adjust the parameters below to explore different parts of the zeta function's critical line.")
    max_imaginary = st.sidebar.slider("Maximum Imaginary Part", 10, 500, 100, 10)  # Updated range to 500 with default of 100
    precision = st.sidebar.slider("Precision (Decimal Places)", 5, 50, 15, 5)  # Updated default precision to 15

    # Set mpmath precision
    mpmath.mp.dps = precision

    # Calculate the zeta zeros based on user input
    zeros = find_riemann_zeros(max_imaginary)

    # Visualization
    if zeros:
        st.write("## Non-Trivial Zeros of the Riemann Zeta Function")
        plot_zeros(zeros)
    else:
        st.write("No zeros found within the given range.")

    # Explanation and references
    st.write("### Explanation")
    st.markdown(
        "The **Riemann zeta function** is a complex-valued function that plays a key role in number theory. This app visualizes the non-trivial zeros along the critical line where the real part of \(s\) is 0.5.")
    st.write("### References")
    st.markdown("- [Riemann Hypothesis - Wikipedia](https://en.wikipedia.org/wiki/Riemann_hypothesis)")


# Function to find non-trivial zeros
@st.cache_data
def find_riemann_zeros(max_imaginary):
    zeros = []
    for t in np.linspace(0, max_imaginary, 1000):  # Reduced number of points to avoid long computation times
        s = 0.5 + t * 1j
        value = mpmath.zeta(s)
        if abs(value) < 1e-3:  # Relaxed threshold for zero detection
            zeros.append((mpmath.re(s), mpmath.im(s)))
    return zeros


# Plot zeros using Plotly for interactivity
def plot_zeros(zeros):
    re_vals, im_vals = zip(*zeros) if zeros else ([], [])

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=re_vals,
        y=im_vals,
        mode='markers',
        marker=dict(size=5, color='blue')
    ))

    fig.update_layout(
        title='Non-Trivial Zeros of the Riemann Zeta Function',
        xaxis=dict(title='Real Part (Re(s))'),
        yaxis=dict(title='Imaginary Part (Im(s))'),
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()
