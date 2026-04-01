import sys
from pathlib import Path
import streamlit as st
from PIL import Image

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from analysis.data_loader import load_data

st.set_page_config("RefInsight", layout="wide")

@st.cache_data
def load_cached():
    return load_data()

df = load_cached()

if (Path("app/assets/logo.png")).exists():
    st.sidebar.image(Image.open("app/assets/logo.png"), width=160)

st.sidebar.markdown("### RefInsight")
st.sidebar.caption("Premier League Refereeing Analytics")

selected_seasons = st.sidebar.multiselect(
    "Seasons", sorted(df["Season"].unique()),
    default=sorted(df["Season"].unique())
)

min_matches = st.sidebar.slider("Minimum matches per referee", 5, 35, 15)

df = df[df["Season"].isin(selected_seasons)]

st.session_state["df"] = df
st.session_state["min_matches"] = min_matches

st.title("⚽ RefInsight")
st.markdown("Analytics dashboard exploring refereeing patterns, bias, and VAR impact.")

c1, c2, c3 = st.columns(3)
c1.metric("Matches", len(df))
c2.metric("Referees", df["Referee"].nunique())
c3.metric("Seasons", df["Season"].nunique())
