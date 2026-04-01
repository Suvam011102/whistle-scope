import streamlit as st
import plotly.express as px
from utils.session import ensure_session_state
ensure_session_state()

df = st.session_state["df"]

st.title("📌 Executive Summary")

col1, col2 = st.columns(2)
run = col1.button("▶ Run analysis")
reset = col2.button("🔄 Reset")

if reset:
    st.rerun()

if run:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Matches", len(df))
    c2.metric("Referees", df["Referee"].nunique())
    c3.metric("Teams", df["HomeTeam"].nunique())
    c4.metric("Seasons", df["Season"].nunique())

    st.markdown("---")

    col1, col2 = st.columns(2)

    fig1 = px.histogram(df, x="TotalFouls", nbins=40,
                        title="Total Fouls per Match")
    col1.plotly_chart(fig1, width="stretch")

    fig2 = px.histogram(df, x="TotalCards", nbins=30,
                        title="Total Cards per Match")
    col2.plotly_chart(fig2, width="stretch")
else:
    st.info("Click the ▶ Run analysis button to generate the executive summary.")
