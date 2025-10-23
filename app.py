import streamlit as st 
from sections.intro import show_intro
from sections.overview import show_kpis_filtered
from utils.prep import clean_data
from utils.io import load_data
from sections.overview import show_kpis
from utils.viz import volume_by_category, top_departments, category_distribution, radionuclide_counts
from sections.deep_dives import volume_by_category_analysis, top_departments_analysis, category_distribution_analysis, radionuclide_counts_analysis
from sections.conclusions import show_conclusion

st.set_page_config(page_title="Radioactive Waste in France Dashboard ", layout="wide")

st.title("Data Storytelling: Conditioned Radioactive Waste in France")
st.caption("Source: https://www.data.gouv.fr/datasets/inventaire-national-des-matieres-et-dechets-radioactifs/")

show_intro()

df = clean_data(load_data())

with st.sidebar:
    st.header("Filters")
    selected_dept = st.multiselect("Select Department", df["departement"].unique())
    selected_cat = st.multiselect("Select Category", df["categorie"].unique())
    if selected_dept:
        df = df[df["departement"].isin(selected_dept)]
    if selected_cat:
        df = df[df["categorie"].isin(selected_cat)]

# KPIs tied to filters

    show_kpis_filtered(df)
    st.markdown("""
    ***These KPIs are tied to the filters, so they change according to the filters you applied.*** 
    """)

    st.subheader("Filtered Data Preview")
    st.dataframe(df.head(20))   

from utils.viz import show_kpis, volume_by_category, top_departments, category_distribution, radionuclide_counts

df = clean_data(load_data())

show_kpis(df)

volume_by_category(df)
volume_by_category_analysis()

top_departments(df)
top_departments_analysis()

category_distribution(df)
category_distribution_analysis()

radionuclide_counts(df)
radionuclide_counts_analysis()

show_conclusion()


st.download_button("Download Cleaned Dataset", df.to_csv(index=False), "cleaned_data.csv")
