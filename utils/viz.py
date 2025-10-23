import streamlit as st
import plotly.express as px

# 1. KPI Overview
def show_kpis(df):
    total_volume = df["volume_equivalent_conditionne"].sum()
    mean_volume = df["volume_equivalent_conditionne"].mean()
    dept_volumes = df.groupby("departement")["volume_equivalent_conditionne"].sum()

    if not dept_volumes.empty:
        top_dept = dept_volumes.idxmax()
        top_dept_volume = dept_volumes.max()
    else:
        top_dept = "N/A"
        top_dept_volume = 0

    st.subheader(" What is the overall scale of radioactive waste in France?")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Volume (m³)", f"{total_volume:,.0f}")
    c2.metric("Average per Site", f"{mean_volume:,.1f}")
    c3.metric("Top Département", f"{top_dept} ({top_dept_volume:,.0f} m³)")

    st.markdown("""
    France has declared over **{:,} m³** of conditioned radioactive waste, with an average of **{:.1f} m³** per site. 
    The department **{}** alone accounts for the highest volume, more than half the national total.
    This concentration likely reflects the presence of major nuclear infrastructure or centralized storage facilities. 
    It’s a clear signal that some regions carry a disproportionate share of the national waste burden, which has direct implications for oversight and resource allocation.
    """.format(int(total_volume), mean_volume, top_dept))


# 2. Volume by Category
def volume_by_category(df):
    st.subheader(" How is waste volume distributed across categories?")
    cat_volume = df.groupby("categorie")["volume_equivalent_conditionne"].sum().reset_index()
    fig = px.bar(cat_volume, x="categorie", y="volume_equivalent_conditionne",
                 title="Volume by Waste Category",
                 labels={"volume_equivalent_conditionne": "Volume (m³)", "categorie": "Category"},
                 color="categorie")
    st.plotly_chart(fig, use_container_width=True)


# 3. Top Departments
def top_departments(df):
    st.subheader("Which departments contribute most to the national waste volume?")
    top_depts = df.groupby("departement")["volume_equivalent_conditionne"].sum().sort_values(ascending=False).head(10).reset_index()
    fig = px.bar(top_depts, x="volume_equivalent_conditionne", y="departement", orientation="h",
                 title="Top 10 Departments by Waste Volume",
                 labels={"volume_equivalent_conditionne": "Volume (m³)", "departement": "Department"})
    st.plotly_chart(fig, use_container_width=True)


# 4. Volume Distribution by Category
def category_distribution(df):
    st.subheader("How variable is the waste volume within each category?")
    fig = px.box(df, x="categorie", y="volume_equivalent_conditionne",
                 title="Volume Distribution by Category",
                 labels={"volume_equivalent_conditionne": "Volume (m³)", "categorie": "Category"},
                 color="categorie")
    st.plotly_chart(fig, use_container_width=True)


# 5. Radionuclide Presence (if usable)
def radionuclide_counts(df):
    st.subheader(" Which radionuclides appear most frequently?")
    if "principaux_radionucleides" in df.columns:
        nuclide_counts = df["principaux_radionucleides"].value_counts().head(10).reset_index()
        nuclide_counts.columns = ["Radionuclide", "Count"]
        fig = px.bar(nuclide_counts, x="Radionuclide", y="Count",
                     title="Top Radionuclides in Declared Waste",
                     color="Radionuclide")
        st.plotly_chart(fig, use_container_width=True)

