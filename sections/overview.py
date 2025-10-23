import streamlit as st

def show_kpis(df):
    total_volume = df["volume_equivalent_conditionne"].sum()
    mean_volume = df["volume_equivalent_conditionne"].mean()
    top_dept = df.groupby("departement")["volume_equivalent_conditionne"].sum().idxmax()
    top_dept_volume = df.groupby("departement")["volume_equivalent_conditionne"].sum().max()

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Volume (m³)", f"{total_volume:,.0f}")
    c2.metric("Average per Site", f"{mean_volume:,.1f}")
    c3.metric("Top Département", f"{top_dept} ({top_dept_volume:,.0f} m³)")

    st.markdown("""
    France has declared over **{:,} m³** of conditioned radioactive waste, with an average of **{:.1f} m³** per site. The department **{}** alone accounts for the highest volume, indicating a concentration of nuclear infrastructure or specialized storage.

    These figures help prioritize regional oversight and inform national waste management strategies.
    """.format(int(total_volume), mean_volume, top_dept))


import streamlit as st

def show_kpis_filtered(df):
    total_volume = df["volume_equivalent_conditionne"].sum()
    mean_volume = df["volume_equivalent_conditionne"].mean()

    if not df.empty:
        dept_volumes = df.groupby("departement")["volume_equivalent_conditionne"].sum()
        top_dept = dept_volumes.idxmax()
        top_dept_volume = dept_volumes.max()
    else:
        top_dept = "N/A"
        top_dept_volume = 0

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Volume (m³)", f"{total_volume:,.0f}")
    c2.metric("Average per Site", f"{mean_volume:,.1f}")
    c3.metric("Top Département", f"{top_dept} ({top_dept_volume:,.0f} m³)")
