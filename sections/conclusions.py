import streamlit as st 
def show_conclusion():
    st.subheader("CONCLUSION")
    st.markdown("""
    This dashboard reveals a strong concentration of radioactive waste in a few departments, notably Aude (11), 
    and a large volume of unclassified waste under 'SANS CATEGORIE'. These patterns suggest the need for 
    improved classification protocols and targeted regional oversight. Future work could include time-series 
    analysis, site-level mapping, and integration of treatment or risk data.
    """)
