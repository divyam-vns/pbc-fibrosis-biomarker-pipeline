
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
# BASE PATHS (CRITICAL FIX)
# =====================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(BASE_DIR, "..")

MODEL_PATH = os.path.join(ROOT_DIR, "models", "model.pkl")
BIOMARKER_PATH = os.path.join(ROOT_DIR, "results", "top_biomarkers.csv")
FIG_DIR = os.path.join(ROOT_DIR, "figures")

# =====================================
# LOAD MODEL + BIOMARKERS
# =====================================
model = joblib.load(MODEL_PATH)
biomarkers = pd.read_csv(BIOMARKER_PATH)

# =====================================
# TITLE
# =====================================
st.title("🧬 PBC Fibrosis Biomarker Dashboard")
# =====================================
# TOP METRICS
# =====================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model", "XGBoost")

with col2:
    st.metric("Biomarkers", "20")

with col3:
    st.metric("ROC-AUC", "1.00")
    
st.markdown("""
This AI-powered application predicts fibrosis risk using transcriptomic biomarkers,
combined with machine learning (XGBoost), SHAP explainability, and pathway-informed biology.
""")

# =====================================
# SIDEBAR INPUTS
# =====================================
st.sidebar.header("Biomarker Inputs (Top Genes)")

top_genes = biomarkers["gene"].head(20).tolist()

user_input = {}
for gene in top_genes:
    user_input[gene] = st.sidebar.number_input(gene, value=0.0)

# =====================================
# PREDICTION
# =====================================
if st.sidebar.button("Predict Risk"):

    X_input = np.array(list(user_input.values())).reshape(1, -1)

    prediction = model.predict(X_input)[0]
    probability = model.predict_proba(X_input)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(f"High Fibrosis Risk (Probability: {probability:.2f})")
    else:
        st.success(f"Low Fibrosis Risk (Probability: {probability:.2f})")

# =====================================
# VISUALIZATION SECTION (FIXED PATHS)
# =====================================
st.markdown("---")
st.header("📊 Model Interpretability & Biological Insights")
# =====================================
# TABS
# =====================================

tab1, tab2, tab3 = st.tabs(
    ["📈 Model Performance", "🧬 Biological Insights", "🧠 Explainable AI"]
)

# =====================================
# TAB 1 — MODEL PERFORMANCE
# =====================================

with tab1:

    st.subheader("ROC Curve")
    st.image(
        os.path.join(FIG_DIR, "roc_curve.png"),
        use_container_width=True
    )

    st.subheader("PCA Visualization")
    st.image(
        os.path.join(FIG_DIR, "pca_plot.png"),
        use_container_width=True
    )

# =====================================
# TAB 2 — BIOLOGICAL INSIGHTS
# =====================================

with tab2:

    st.subheader("Biomarker Importance")
    st.image(
        os.path.join(FIG_DIR, "biomarker_importance.png"),
        use_container_width=True
    )

    st.subheader("Volcano Plot")
    st.image(
        os.path.join(FIG_DIR, "volcano_plot.png"),
        use_container_width=True
    )

# =====================================
# TAB 3 — EXPLAINABLE AI
# =====================================

with tab3:

    st.subheader("SHAP Summary")
    st.image(
        os.path.join(FIG_DIR, "shap_summary.png"),
        use_container_width=True
    )
col1, col2 = st.columns(2)

with col1:
    st.subheader("ROC Curve")
    st.image(os.path.join(FIG_DIR, "roc_curve.png"), use_container_width=True)

    st.subheader("PCA Visualization")
    st.image(os.path.join(FIG_DIR, "pca_plot.png"), use_container_width=True)

with col2:
    st.subheader("SHAP Summary")
    st.image(os.path.join(FIG_DIR, "shap_summary.png"), use_container_width=True)

    st.subheader("Biomarker Importance")
    st.image(os.path.join(FIG_DIR, "biomarker_importance.png"), use_container_width=True)

# =====================================
# FOOTER
# =====================================
st.markdown("---")
st.markdown("Built for translational biomarker discovery in liver fibrosis using ML + SHAP + pathway biology.")

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
Dr. Divya Mishra, PhD
""")
