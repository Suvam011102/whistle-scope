import streamlit as st
import numpy as np
from analysis.referee import compute_referee_stats
from analysis.bias import compute_home_bias
from analysis.var_impact import compute_var_impact
from utils.session import ensure_session_state
ensure_session_state()

df = st.session_state["df"]
min_matches = st.session_state["min_matches"]

st.title("📄 Analytical Report")

col1, col2 = st.columns(2)
run = col1.button("▶ Generate report")
reset = col2.button("🔄 Reset")

if reset:
    st.rerun()

if run:
    # -------------------------------------------------
    st.subheader("👨‍⚖️ Referee Consistency")

    ref = compute_referee_stats(df, min_matches)
    iqr = (
        np.percentile(ref["avg_fouls"], 75)
        - np.percentile(ref["avg_fouls"], 25)
    )

    st.markdown(
        f"""
        Referee foul enforcement shows **systematic variability**.

        - Interquartile range of average fouls: **{iqr:.2f}**
        - Indicates consistent but non-uniform application of match control
        """
    )

    # -------------------------------------------------
    st.subheader("🏠 Home–Away Bias")

    bias = compute_home_bias(df, min_matches)

    st.markdown(
        f"""
        The average home–away foul differential is **{bias['mean_bias']:.2f}**.

        - p-value: **{bias['p_value']:.4f}**
        - Suggests modest aggregate bias with localized variation
        """
    )

    # -------------------------------------------------
    st.subheader("🎥 VAR Impact")

    summary, _ = compute_var_impact(df)
    pre = summary[summary["VAR_Era"] == "Pre-VAR"].iloc[0]
    post = summary[summary["VAR_Era"] == "Post-VAR"].iloc[0]

    st.markdown(
        f"""
        VAR introduction corresponds with a **structural change in enforcement**.

        - Fouls per match changed from **{pre.avg_fouls:.2f}** to **{post.avg_fouls:.2f}**
        - Cards per foul increased from **{pre.avg_cards_per_foul:.3f}**
          to **{post.avg_cards_per_foul:.3f}**

        This suggests a recalibration of disciplinary thresholds rather than increased randomness.
        """
    )

    # -------------------------------------------------
    st.subheader("📊 Executive Takeaways")

    st.markdown(
        """
        - Refereeing decisions are consistent but heterogeneous
        - Home–away bias is small in aggregate but non-uniform
        - VAR altered disciplinary efficiency at a system level

        These findings highlight the value of **distribution-aware analysis**
        when evaluating subjective decision systems.
        """
    )
