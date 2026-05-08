# PBC Fibrosis Biomarker Discovery Pipeline

![Python](https://img.shields.io/badge/Python-3.12-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-XGBoost-green)
![Explainable AI](https://img.shields.io/badge/Explainable%20AI-SHAP-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)
![Bioinformatics](https://img.shields.io/badge/Bioinformatics-Translational%20Oncology-purple)
# PBC Fibrosis Biomarker Discovery Pipeline

## Overview

This project implements an end-to-end translational bioinformatics pipeline for biomarker discovery in Primary Biliary Cholangitis (PBC) using liver transcriptomic data.

It integrates:
- Differential gene expression analysis
- Machine learning biomarker discovery
- SHAP explainable AI
- Pathway enrichment analysis
- Clinical-style risk prediction
- Streamlit web application

---

## Methods

Differential gene expression analysis was performed using statistical testing (Welch’s t-test) between high-risk and low-risk fibrosis samples. P-values were adjusted using False Discovery Rate (FDR) correction to control for multiple hypothesis testing. Volcano plots were generated to visualize significantly dysregulated genes.

---

## Machine Learning

A supervised classification model was trained using an XGBoost classifier to predict fibrosis risk (high vs low).

- Input features: normalized gene expression matrix
- Output: binary fibrosis risk label
- Model optimization: tree-based boosting with regularization
- Evaluation: train-test split with ROC-AUC scoring

The model achieved strong predictive performance, demonstrating that transcriptomic signatures can separate fibrosis risk groups

---

## Explainable AI (SHAP)

SSHAP (SHapley Additive exPlanations) was used to interpret the trained model.

Key outputs:

- Feature importance ranking of genes
- Direction of gene contribution (risk-increasing vs protective)
- Identification of stable biomarker candidates

This enables biological interpretability of machine learning predictions

---

## Pathway Enrichment

Functional enrichment analysis was performed using GSEApy / Enrichr against KEGG 2021 Human pathways.

Significant pathways included:

- Complement and coagulation cascades
- Cytokine-cytokine receptor interaction
- Th17 cell differentiation
- Systemic lupus erythematosus
- Immune and inflammatory signaling pathways

These pathways highlight immune-driven mechanisms of fibrosis progression.

---

## Top Biomarkers

Top ranked biomarkers identified through SHAP and differential expression:

FCER2
ITGB4
DDX50
CCL15
NFKB2
RORA
TLR3
CD44
IL27
PRKCD

These genes are associated with:

- immune regulation
- inflammation
- cytokine signaling
- fibrosis and tissue remodeling

---

## Biological Findings

Key biological insights:

- Identified immune and complement-associated fibrosis biomarkers in PBC.
- SHAP analysis highlighted FCER2, ITGB4, NFKB2, RORA, and TLR3 as highly predictive genes.
- Pathway enrichment revealed strong activation of:
  - Complement and coagulation cascades
  - Th17 differentiation
  - Cytokine signaling
  - Innate immune activation
- XGBoost achieved strong classification performance on fibrosis-risk stratification.

Overall, results support fibrosis as an immune-driven transcriptional disease.

---

## Model Performance

- ROC-AUC: 1.00
- Classification: High-risk vs Low-risk fibrosis

Note: Dataset size is small (n=16 samples), so results represent a proof-of-concept translational model, not a clinical-grade diagnostic system.

---

## Translational Relevance

This project demonstrates an end-to-end translational bioinformatics workflow integrating:

- transcriptomic biomarker discovery
- explainable machine learning
- pathway biology
- fibrosis risk prediction
- deployable clinical-style dashboarding

The framework can be extended to:
- liver fibrosis
- NASH/MASH
- oncology biomarker discovery
- precision medicine pipelines

---
## Streamlit App

Interactive dashboard includes:
- Biomarker sliders
- Risk prediction
- Probability output
- Biomarker table visualization

---

## Limitations

- Small cohort size (n=16)
- Requires external validation in independent cohorts
- Transcriptomic-only model without multi-omics integration
- Exploratory research pipeline, not clinical-grade diagnostic software

---

## Future Directions

- Multi-cohort validation
- Survival modeling integration
- Multi-omics biomarker fusion
- Cloud-native deployment
- CAP/CLIA-compatible pipeline extension

---

## Technologies Used

Python, pandas, numpy, scikit-learn, XGBoost, SHAP, GSEApy, Streamlit, GEOparse

---

## Author

Dr. Divya Mishra, PhD

Bioinformatics | Translational Genomics | Biomarker Discovery

---

## Disclaimer

Research use only. Not for clinical diagnosis.
