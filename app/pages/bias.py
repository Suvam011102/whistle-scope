import streamlit as st
import plotly.express as px
from analysis.bias import compute_home_bias
from utils.session import ensure_session_state
ensure_session_state()

df = st.session_state["df"]
min_matches = st.session_state["min_matches"]

st.title("🏠 Home–Away Bias")

col1, col2 = st.columns(2)
run = col1.button("▶ Run analysis")
reset = col2.button("🔄 Reset")

if reset:
    st.rerun()

if run:
    result = compute_home_bias(df, min_matches)
    bias_df = result["data"]

    st.metric("Mean Bias (Away − Home)", round(result["mean_bias"], 2))
    st.metric("p-value", round(result["p_value"], 4))

    fig = px.histogram(
        bias_df,
        x="HomeBias",
        nbins=40,
        title="Home–Away Bias Distribution"
    )
    fig.add_vline(x=0, line_dash="dash")
    st.plotly_chart(fig, width="stretch")
    st.markdown(
        "The histogram illustrates the distribution of foul differentials "
        "between home and away teams. A bias greater than zero indicates "
        "that away teams receive more fouls on average, while a bias less than "
        "zero suggests home teams are favored."
    )
