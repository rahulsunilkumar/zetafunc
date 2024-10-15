import streamlit as st
import plotly.graph_objs as go

# Set up Streamlit app
def main():
    st.title("Exploring the Riemann Hypothesis: Visualizing Non-Trivial Zeros")
    st.write("This app visualizes some known non-trivial zeros of the Riemann zeta function along the critical line (Re(s) = 0.5).")

    # Sidebar configuration for user inputs
    st.sidebar.header("Visualization Options")
    show_all = st.sidebar.checkbox("Show all precomputed zeros", value=True)

    # Precomputed known zeros of the Riemann zeta function (first few on the critical line)
    known_zeros = [
        (0.5, 14.134725),
        (0.5, 21.022040),
        (0.5, 25.010858),
        (0.5, 30.424876),
        (0.5, 32.935062),
        (0.5, 37.586178),
        (0.5, 40.918719),
        (0.5, 43.327073),
        (0.5, 48.005150),
        (0.5, 49.773832)
    ]

    # Filter zeros if needed
    zeros_to_plot = known_zeros if show_all else known_zeros[:5]

    # Visualization
    st.write("## Non-Trivial Zeros of the Riemann Zeta Function")
    plot_zeros(zeros_to_plot)

    # Explanation and references
    st.write("### Explanation")
    st.markdown(
        "The **Riemann zeta function** is a complex-valued function that plays a key role in number theory. This app visualizes some precomputed non-trivial zeros along the critical line where the real part of \(s\) is 0.5.")
    st.write("### References")
    st.markdown("- [Riemann Hypothesis - Wikipedia](https://en.wikipedia.org/wiki/Riemann_hypothesis)")


# Plot zeros using Plotly for interactivity
def plot_zeros(zeros):
    re_vals, im_vals = zip(*zeros)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=re_vals,
        y=im_vals,
        mode='markers',
        marker=dict(size=10, color='blue')
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
