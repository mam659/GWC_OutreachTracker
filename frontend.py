import streamlit as st
import pandas as pd

st.title("Recruitment Points Tracker")

# Mock data based on your PDF entries [cite: 5, 6, 9]
data = pd.DataFrame({
    'Member': ['Member A', 'Member B', 'Member C'],
    'Total Points': [125, 75, 50] 
})

st.bar_chart(data.set_index('Member'))

if st.button('Add 25 Points for Contacting'):
    st.success("Points logged successfully!")
