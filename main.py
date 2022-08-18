import streamlit as st
from api.spreadsheet import get_satisfaction, get_label
import numpy as np
import pandas as pd

st.title("Dash Board")


satisfaction = get_satisfaction()
labels = get_label()
chart_data = pd.DataFrame(
    satisfaction,
    index=labels,
    columns=['満足度']
)
st.line_chart(chart_data)