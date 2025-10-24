# Conditioned Radioactive Waste in France — Data Storytelling Dashboard

This Streamlit dashboard explores the distribution, classification, and composition of conditioned radioactive waste declared across France. Built using public data from [data.gouv.fr](https://www.data.gouv.fr/datasets/inventaire-national-des-matieres-et-dechets-radioactifs/), the app provides interactive visualizations and narrative insights to support environmental monitoring and strategic planning.

---



##  Objectives

- Analyze total and average waste volumes across sites and departments
- Identify dominant waste categories and their variability
- Highlight the most frequent radionuclides in declared waste
- Provide actionable insights through interactive storytelling

---

##  Dataset

- **Source:** [data.gouv.fr – Déchets radioactifs conditionnés déclarés par site](https://www.data.gouv.fr/datasets/inventaire-national-des-matieres-et-dechets-radioactifs/)
- **License:** Open data, reusable for academic purposes
- **Format:** CSV
- **Fields used:** `volume_equivalent_conditionne`, `departement`, `categorie`, `principaux_radionucleides`, `nom_site`, `latitude`, `longitude`

---

##  Features

- Sidebar filters by department and category
- KPI header tied to filters (total volume, average per site, top department)
- Interactive bar charts, boxplots, and radionuclide frequency
- Geographic map of waste sites (if coordinates available)
- Data quality section (missing values, duplicates)
- Narrative blocks for each visual
- Download button for cleaned dataset

---

##  Project Structure
```
project_root/ ├── app.py ├── data/ │ └── dechets-declares-a-fin-2023.csv ├── sections/ │ ├── intro.py │ ├── overview.py │ ├── deep_dives.py │ ├── data_quality.py │ └── conclusions.py ├── utils/ │ ├── io.py │ ├── prep.py │ └── viz.py ├── assets/ │ └── logos, icons, images └── README.md 
```




---

##  Installation & Run Instructions

### Clone the repo
git clone <your-repo-url>
cd project_root

### Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

### Install dependencies
pip install -r requirements.txt

### Run the app
streamlit run app.py


---
##  Streamlit app

Link deployed : https://radioactive-waste-dashboardwithapp-softmjs9ehug5xepmwe3zt.streamlit.app/


---
##  Repo Link

Link : https://github.com/zorobabel33/radioactive-waste-dashboard_with_streamlit

---

## 🎥 Demo Video

Watch the full walkthrough of the dashboard:  the video is inside the project folder.


---