# End-to-End MLOps Showcase

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://docker.com)
[![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=flat&logo=kubernetes&logoColor=white)](https://kubernetes.io/)

A comprehensive MLOps project demonstrating the complete machine learning lifecycle from experimentation to production deployment. This repository showcases three interconnected MLOps stages, each implemented in its own directory.

## 🏗️ Project Structure

```
end-to-end-mlops-showcase/
├── SetUp_basic_MLOps/          # Stage 1: ML Experimentation & Tracking
├── end_to_end_ML_pipeline/      # Stage 2: ML Pipeline Development
├── ML_model_deploy_k8s/         # Stage 3: Production Deployment
└── README.md
```

## 📋 Stages Overview

### 1. SetUp_basic_MLOps - Foundation & Experimentation
**Focus:** Establishing MLOps infrastructure with experiment tracking and containerization.

**Key Components:**
- MLflow integration for experiment tracking
- Docker containerization setup
- Basic ML training pipeline (Iris classification)
- Logging infrastructure

**Technologies:** Python, MLflow, Docker, Docker Compose

### 2. end_to_end_ML_pipeline - Pipeline Development
**Focus:** Complete machine learning pipeline from data to model deployment.

**Key Components:**
- Data preprocessing and feature engineering
- Model training (Random Forest on California Housing dataset)
- Model evaluation and validation
- Model serialization for deployment

**Technologies:** Python, scikit-learn, pandas, Jupyter Notebook

### 3. ML_model_deploy_k8s - Production Deployment
**Focus:** Containerized model serving with Kubernetes orchestration.

**Key Components:**
- Flask REST API for model predictions
- Docker containerization
- Kubernetes deployment manifests
- Service configuration for load balancing

**Technologies:** Python, Flask, Docker, Kubernetes

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Docker & Docker Compose
- Kubernetes cluster (for Stage 3)
- Git

### Running Each Stage

#### Stage 1: Basic MLOps Setup
```bash
cd SetUp_basic_MLOps
docker compose up --build
```

#### Stage 2: ML Pipeline
```bash
cd end_to_end_ML_pipeline
jupyter notebook pathToProd.ipynb
```

#### Stage 3: Kubernetes Deployment
```bash
cd ML_model_deploy_k8s
# Build and deploy
docker build -t ml-model-api .
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

## 📊 MLflow Tracking

For experiment tracking in Stage 1:
```bash
cd SetUp_basic_MLOps
python src/train.py
# View results at http://localhost:5000
```

## 🔧 API Usage

Once Stage 3 is deployed, make predictions:

```python
import requests

# Example prediction request
response = requests.post('http://your-service-url/predict',
                        json={'features': [8.3, 41.0, 6.98, 1.0, 322.0, 2.18, 37.88, -122.23]})
print(response.json())
```

## 🛠️ Technologies Used

- **Machine Learning:** scikit-learn, pandas, numpy
- **Experiment Tracking:** MLflow
- **Containerization:** Docker, Docker Compose
- **Orchestration:** Kubernetes
- **Web Framework:** Flask
- **Development:** Jupyter Notebook

## 📈 Learning Outcomes

This project demonstrates:
- Setting up ML experiment tracking with MLflow
- Building end-to-end ML pipelines
- Containerizing ML models for deployment
- Orchestrating ML services with Kubernetes
- Best practices for MLOps workflows

## 🤝 Contributing

Feel free to fork this repository and enhance the MLOps pipeline. Suggestions for improvements are welcome!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- California Housing dataset from scikit-learn
- Iris dataset from scikit-learn
- MLflow community for experiment tracking tools
- Kubernetes community for orchestration tools

---

**Showcase your MLOps expertise!** This repository demonstrates a complete MLOps workflow that can serve as a foundation for production ML systems.
