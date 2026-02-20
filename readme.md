# 📊 Telco Customer Churn Prediction API

A production-style machine learning service that predicts whether a telecom customer is likely to churn. This project demonstrates end-to-end ML deployment, including model serving, feature consistency, containerization, CI/CD automation, and a browser-based UI.

---

## 🚀 Project Overview

This repository provides a real-time churn prediction API built with:

- **FastAPI** — REST API layer  
- **Gradio** — Browser UI for interactive predictions  
- **XGBoost / Scikit-learn** — Machine learning model  
- **Docker** — Containerized deployment  
- **GitHub Actions** — Automated build and push pipeline  
- **Docker Hub** — Container registry  

The goal of this project is to demonstrate how a trained ML model moves from experimentation into a production-ready inference service.

---

## 🧠 What the Model Does

The model predicts whether a telecom customer is likely to churn or not likely to churn based on behavioral, demographic, and billing-related features such as demographics, billing preferences, contract type, service subscriptions, monthly charges, and tenure. The inference pipeline ensures that serving-time transformations exactly match training-time transformations to prevent train/serve skew and maintain model reliability.

---

## 🏗️ Architecture

The project separates responsibilities into layered components:

Browser UI (Gradio)  
→ FastAPI Application Layer  
→ Model Layer (Inference Pipeline)

### 🔹 Model Layer (`src/serving/inference.py`)
Responsible for loading model artifacts, applying feature transformations, maintaining feature ordering, and generating predictions. This layer is UI-agnostic and reusable across APIs, batch pipelines, command-line tools, or other services.

### 🔹 API Layer (`src/app/main.py`)
Handles HTTP request routing, input validation, endpoint definitions, and integration with the Gradio UI.

### 🔹 UI Layer (Gradio)
Provides a browser interface for testing predictions without writing code. Accessible locally at:

http://localhost:8000/ui

---