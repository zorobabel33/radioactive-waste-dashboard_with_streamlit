import streamlit as st

def show_intro():
    st.markdown("""
    This dashboard explores the distribution and classification of conditioned radioactive waste across France, based on public data from [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/dechets-radioactifs-conditionnes-declares-par-site/).  
    The goal is to provide clear insights into waste volumes, regional disparities, and classification practices, using interactive visualizations and narrative analysis.

    **Key questions addressed:**
    - What is the overall scale of radioactive waste in France?
    - Which categories and regions dominate the declared volumes?
    - How variable is the waste within each classification?
    - Which radionuclides are most frequently present?

    **Note:** Some fields contain missing or non-standard values (e.g., 'ND' for radionuclides), which may affect interpretation.
    """)
