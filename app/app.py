
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="PBC Fibrosis Biomarker Dashboard",
    layout="wide"
)

# =====================================
# BASE DIRECTORY
# =====================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# =====================================
# LOAD MODEL + BIOMARKERS
# =====================================

model_path = os.path.join(BASE_DIR, "..", "models", "model.pkl")
biomarker_path = os.path.join(BASE_DIR, "..", "results", "top_biomarkers.csv")

model = joblib.load(model_path)
biomarkers = pd.read_csv(biomarker_path)

# =====================================
# TITLE
# =====================================

st.title("PBC Fibrosis Biomarker Dashboard")

st.markdown("""
This application predicts fibrosis risk using a machine learning
biomarker panel derived from liver transcriptomic profiling.
""")

# =====================================
# SIDEBAR
# =====================================

st.sidebar.header("Biomarker Inputs")

top_genes = biomarkers["gene"].head(10).tolist()

inputs = {}

for gene in top_genes:
    inputs[gene] = st.sidebar.slider(
        gene,
        min_value=0.0,
        max_value=15.0,
        value=5.0,
        step=0.1
    )

# =====================================
# PREPARE INPUT DATA
# =====================================

input_df = pd.DataFrame([inputs])

# Align features with training model
expected_features = model.feature_names_in_

for feature in expected_features:
    if feature not in input_df.columns:
        input_df[feature] = 0

input_df = input_df[expected_features]

# =====================================
# PREDICTION
# =====================================

prediction = model.predict(input_df)[0]
probability = model.predict_proba(input_df)[0][1]

# =====================================
# DISPLAY RESULTS
# =====================================

st.subheader("Prediction Results")

risk_label = "High Risk" if prediction == 1 else "Low Risk"

st.metric(
    label="Predicted Fibrosis Risk",
    value=risk_label
)

st.metric(
    label="High Risk Probability",
    value=f"{probability:.2%}"
)

# =====================================
# BIOMARKER PANEL
# =====================================

st.subheader("Top Biomarkers")

st.dataframe(
    biomarkers.head(20),
    use_container_width=True
)

# =====================================
# ABOUT
# =====================================

st.subheader("Project Summary")

st.markdown("""
### Translational Biomarker Pipeline

This project includes:

- Differential expression analysis
- Machine learning biomarker discovery
- SHAP explainability
- Pathway enrichment analysis
- XGBoost fibrosis prediction model

Dataset:
GSE79850 (Primary Biliary Cholangitis liver transcriptomics)

Author:
Divya Mishra, PhD
""")
