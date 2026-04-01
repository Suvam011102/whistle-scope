import streamlit as st
import plotly.express as px
from analysis.var_impact import compute_var_impact
from utils.session import ensure_session_state
ensure_session_state()

df = st.session_state["df"]

st.title("🎥 VAR Impact Analysis")

col1, col2 = st.columns(2)
run = col1.button("▶ Run analysis")
reset = col2.button("🔄 Reset")

if reset:
    st.rerun()

if run:
    _, df_var = compute_var_impact(df)

    fig1 = px.box(
        df_var,
        x="VAR_Era",
        y="TotalCards",
        title="Cards per Match: Pre vs Post VAR"
    )
    st.plotly_chart(fig1, width="stretch")

    fig2 = px.box(
        df_var,
        x="VAR_Era",
        y="CardsPerFoul",
        title="Cards per Foul: Pre vs Post VAR"
    )
    st.plotly_chart(fig2, width="stretch")

    fig3 = px.box(
        df_var,
        x="VAR_Era",
        y="TotalFouls",
        title="Fouls per Match: Pre vs Post VAR"
    )
    st.plotly_chart(fig3, width="stretch")
    st.markdown(
        "The box plots compare key disciplinary metrics before and after the implementation of VAR. "
        "Notable shifts in cards per match, cards per foul, and fouls per match suggest that VAR "
        "has had a significant impact on officiating and player behavior."
    )