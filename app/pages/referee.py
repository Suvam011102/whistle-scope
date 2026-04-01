import streamlit as st
import plotly.express as px
from analysis.referee import compute_referee_stats
from utils.session import ensure_session_state
ensure_session_state()

df = st.session_state["df"]
min_matches = st.session_state["min_matches"]

st.title("👨‍⚖️ Officiating Variance")

col1, col2 = st.columns(2)
run = col1.button("▶ Run analysis")
reset = col2.button("🔄 Reset")

if reset:
    st.rerun()

if run:
    ref_stats = compute_referee_stats(df, min_matches)

    fig1 = px.box(
        ref_stats,
        x="avg_fouls",
        points="all",
        title="Referee Strictness Distribution"
    )
    st.plotly_chart(fig1, width="stretch")

    fig2 = px.scatter(
        ref_stats,
        x="avg_fouls",
        y="avg_cards",
        trendline="ols",
        title="Cards vs Fouls by Referee"
    )
    st.plotly_chart(fig2, width="stretch")
    st.markdown(
        "The box plot displays the distribution of average fouls called per match by referees, "
        "highlighting variability in officiating strictness. "
        "The scatter plot illustrates the relationship between average fouls and average cards issued, "
        "indicating how stricter referees tend to issue more cards."
    )
