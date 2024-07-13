import numpy as np
import streamlit as st
from heart_disease_prediction import main
from explore import show_explore_page


page = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore"))

if page == "Predict":
    main()
else:
    show_explore_page()