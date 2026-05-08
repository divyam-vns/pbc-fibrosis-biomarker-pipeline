
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

<<<<<<< HEAD
Input features: normalized gene expression matrix
Output: binary fibrosis risk label
Model optimization: tree-based boosting with regularization
Evaluation: train-test split with ROC-AUC scoring
=======
- Input features: normalized gene expression matrix
- Output: binary fibrosis risk label
- Model optimization: tree-based boosting with regularization
- Evaluation: train-test split with ROC-AUC scoring
>>>>>>> dc7f8e0e3f13cff7bff797e382d87b0a0ac4fa32

The model achieved strong predictive performance, demonstrating that transcriptomic signatures can separate fibrosis risk groups

---

## Explainable AI (SHAP)

SSHAP (SHapley Additive exPlanations) was used to interpret the trained model.

Key outputs:

<<<<<<< HEAD
Feature importance ranking of genes
Direction of gene contribution (risk-increasing vs protective)
Identification of stable biomarker candidates
=======
- Feature importance ranking of genes
- Direction of gene contribution (risk-increasing vs protective)
- Identification of stable biomarker candidates
>>>>>>> dc7f8e0e3f13cff7bff797e382d87b0a0ac4fa32

This enables biological interpretability of machine learning predictions

---

## Pathway Enrichment

Functional enrichment analysis was performed using GSEApy / Enrichr against KEGG 2021 Human pathways.

Significant pathways included:

<<<<<<< HEAD
Complement and coagulation cascades
Cytokine-cytokine receptor interaction
Th17 cell differentiation
Systemic lupus erythematosus
Immune and inflammatory signaling pathways
=======
- Complement and coagulation cascades
- Cytokine-cytokine receptor interaction
- Th17 cell differentiation
- Systemic lupus erythematosus
- Immune and inflammatory signaling pathways
>>>>>>> dc7f8e0e3f13cff7bff797e382d87b0a0ac4fa32

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

<<<<<<< HEAD
immune regulation
inflammation
cytokine signaling
fibrosis and tissue remodeling
=======
- immune regulation
- inflammation
- cytokine signaling
- fibrosis and tissue remodeling
>>>>>>> dc7f8e0e3f13cff7bff797e382d87b0a0ac4fa32

---

## Biological Findings

Key biological insights:

<<<<<<< HEAD
Strong immune and inflammatory activation in high-risk fibrosis samples
Complement system and coagulation pathways significantly enriched
T-cell differentiation pathways (Th17 axis) implicated in disease progression
Viral response pathways also enriched, suggesting immune dysregulation
=======
- Strong immune and inflammatory activation in high-risk fibrosis samples.
- Complement system and coagulation pathways significantly enriched.
- T-cell differentiation pathways (Th17 axis) implicated in disease progression.
- Viral response pathways also enriched, suggesting immune dysregulation.
>>>>>>> dc7f8e0e3f13cff7bff797e382d87b0a0ac4fa32

Overall, results support fibrosis as an immune-driven transcriptional disease.

---

## Model Performance

<<<<<<< HEAD
ROC-AUC: 1.00
Classification: High-risk vs Low-risk fibrosis
=======
- ROC-AUC: 1.00
- Classification: High-risk vs Low-risk fibrosis
>>>>>>> dc7f8e0e3f13cff7bff797e382d87b0a0ac4fa32

Note: Dataset size is small (n=16 samples), so results represent a proof-of-concept translational model, not a clinical-grade diagnostic system.

---

## Streamlit App

Interactive dashboard includes:
- Biomarker sliders
- Risk prediction
- Probability output
- Biomarker table visualization

---

## Technologies Used

Python, pandas, numpy, scikit-learn, XGBoost, SHAP, GSEApy, Streamlit, GEOparse

---

## Author

<<<<<<< HEAD
Divya Mishra, PhD
=======
Dr. Divya Mishra, PhD
>>>>>>> dc7f8e0e3f13cff7bff797e382d87b0a0ac4fa32

Bioinformatics | Translational Genomics | Biomarker Discovery

---

## Disclaimer

Research use only. Not for clinical diagnosis.
