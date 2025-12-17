# Medical Insurance Cost Prediction  
### End-to-End Machine Learning System (Production-Ready)

This project is a **full end-to-end Machine Learning pipeline** designed to predict **medical insurance costs** based on customer demographics and health indicators.

The focus of this project goes beyond model training — it demonstrates **real-world ML engineering practices**, including modular code design, logging, exception handling, CI/CD, Dockerization, and cloud deployment on AWS.

---

## Problem Statement

Medical insurance charges vary significantly based on factors such as age, BMI, smoking habits, and geographic region. This dataset was used for training the model: https://www.kaggle.com/datasets/mirichoi0218/insurance/data. The objective of this project is to **predict insurance charges** using regression models and deploy the model as a **production-ready web application**.

---

## Solution Overview

- Performed Exploratory Data Analysis (EDA) and feature engineering
- Trained and evaluated multiple regression models
- Built a modular ML pipeline using `scikit-learn`
  - Data Ingestion: Automated loading of raw data, Train-test split for downstream processing
  - Data Transformation: Feature engineering, Scaling numerical features, Encoding categorical variables using a preprocessing pipeline
  - Model Training and Evaluation : Training multiple regression models, Integration with preprocessing using `scikit-learn` Pipelines, Performance comparison using R², MAE, and RMSE (accuracy of testing data 89.17%)
  - Prediction Pipeline: Separate inference pipeline for real-time predictions, Ensures consistent preprocessing between training and inference (R² score of 96.56%)
- Model Deployment: Exposed the trained model via a Flask web application
- Containerized the application using Docker
- Deployed the application to AWS EC2 using Amazon ECR
- Automated deployment using GitHub Actions (CI/CD)

---
> To avoid ongoing cloud charges:
> - The **EC2 instance has been deleted**
> - The **self-hosted GitHub Actions runner has been removed**
>
> The project remains fully reproducible using:
> - Docker
> - GitHub Actions workflow
> - Modular ML pipelines
---

---
## Run Locally

```bash
git clone https://github.com/nishka-shah/mlproject
cd mlproject
docker build -t insurance-cost-predictor .
docker run -p 8000:8000 nishkalearns/insurance-cost-predictor
```
Open in browser:
```bash
http://localhost:8000/predictdata
```
Or
Pull from Docker Hub and run directly
```bash
docker run -p 8000:8000 nishkalearns/insurance-cost-predictor:latest

