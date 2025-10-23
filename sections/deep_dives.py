import streamlit as st

# 2. Volume by Category
def volume_by_category_analysis():    
    st.markdown("""
    The category 'SANS CATEGORIE' dominates the dataset in terms of volume, which raises questions about classification practices. 
    It could represent legacy waste or entries that weren’t properly categorized. FMA-VC also shows a significant volume, suggesting 
    a strong presence of intermediate-level waste with long-lived radionuclides. Categories like 'FA-VL', 'DSF', and 'TFA' have tighter ranges and lower volumes, indicating more standardized reporting or smaller-scale waste. 
    Overall, the chart highlights that some categories are highly heterogeneous, while others are more uniform in volume distribution.
    This distribution helps identify where classification efforts need to be strengthened.
    """)

def top_departments_analysis():
    st.markdown("""
    This horizontal bar chart shows a clear disparity in radioactive waste volumes across the top 10 departments. Department 11 stands out with nearly 1 million m³, while the others contribute significantly less. This concentration suggests that waste management efforts are not evenly distributed across the country. 
    It likely reflects the presence of major facilities or centralized storage in that leading department. The steep drop-off between the top contributor and the rest highlights the need for targeted oversight and possibly a reevaluation of regional storage strategies.
    """)

def category_distribution_analysis():
    st.markdown("""
    This boxplot shows that 'SANS CATEGORIE' has the widest volume spread, with several high-value outliers reaching close to 400,000 m³. That level of variability suggests inconsistent classification or legacy entries with large declared volumes. 
    'FMA-VC' also shows a broad distribution, though more compact than 'SANS CATEGORIE'. Categories like 'FA-VL', 'TFA', 'DSF', and 'VTC' have tighter ranges and lower volumes, which points to more standardized reporting or smaller-scale waste. This breakdown helps identify which categories are most heterogeneous and where classification practices might need to be reviewed.
    """)

def radionuclide_counts_analysis():
        st.markdown("""
        This chart shows that the most frequently declared radionuclide is 'ND', which likely stands for 'non déterminé' or 'not declared'. That alone suggests a gap in reporting or classification. Beyond that, we see a strong presence of industrial and medical isotopes like 54Mn, 60Co, 65Zn, 110mAg, and 137Cs. These are consistent with common sources of radioactive waste. The appearance of uranium isotopes (234U, 235U, 238U), thorium (232Th), and radium (226Ra) points to legacy or high-risk waste. 
        This breakdown helps clarify the types of radioactive materials being handled and can guide containment and monitoring strategies.
        """)



