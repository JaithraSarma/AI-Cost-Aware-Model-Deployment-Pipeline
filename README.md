# AI Cost-Aware Model Deployment Pipeline  
### *MLOps + FinOps Automation Template (Azure / AWS Ready)*

---

## What This Project Is  
This repository provides a **ready-to-use MLOps + FinOps pipeline** designed to automate:
- **Model training, packaging, and deployment**
- **Cost monitoring and optimization**
- **Cross-cloud CI/CD workflows (Azure or AWS)**

It combines **machine learning automation** (MLOps) with **cost governance** (FinOps) principles — giving teams a reusable framework to deploy and operate AI workloads efficiently.

---

## Tech Stack  
| Category | Tools / Services |
|-----------|------------------|
| **Orchestration / CI-CD** | Jenkins |
| **Containerization** | Docker |
| **Infrastructure as Code** | Docker Compose (demo) |
| **Programming / Automation** | Python 3.11 |
| **Machine Learning** | Scikit-learn |
| **FinOps / Cost Optimization** | Simulated engine (JSON reports) |
| **Cloud Integration** | Azure ML, Azure AKS, AWS SageMaker, or ECS (optional) |

---

## When & Why To Use It  
Use this template if you need to:
- Build **automated ML pipelines** that deploy trained models as APIs.  
- Simulate or implement **cost-aware cloud optimization** (FinOps).  
- Create a **DevOps-ready AI pipeline** using real cloud tooling.  
- Demonstrate **multi-cloud engineering ability** with CI/CD, ML, and cost control integration.  

It is ideal for:
- **Cloud & AI engineers** building ML workloads.  
- **DevOps / FinOps teams** implementing cost visibility automation.  
- **Students & professionals** showcasing AI cloud pipelines on portfolios.

---

## Architecture 
<div style="text-align: center;">
    <img src="AI based pipeline.png" alt="Flowchart">
</div>
---

## Implementation (Azure or AWS)
### 1. Fork & Clone
```bash
git clone https://github.com/JaithraSarma/ai-cost-aware-pipeline.git
cd ai-cost-aware-pipeline
```

### 2. Configure Jenkins
Create a Jenkins Pipeline job and point it to this repository. The pipeline uses a parameter named ```CLOUD_PROVIDER``` with three options:
```nginx 
simulate | azure | aws
```

### 3. Set Up Cloud Credentials
- For Azure

| Variable  | Description   |
|-----------|------------------|
| **AZURE_TENANT_ID** | Directory (tenant) ID |
| **AZURE_SUBSCRIPTION_ID** | Subscription ID |
| **AZURE_CLIENT_ID** | Service Principal ID |
| **AZURE_CLIENT_SECRET** | SP password  |
| **AZURE_RESOURCE_GROUP** | Scikit-learn |
| **AZURE_REGION** | Resource Group name  |
| **Cloud Integration** | Deployment region |

- For AWS

| Variable  | Description   |
|-----------|------------------|
| **AWS_ACCESS_KEY_ID** | IAM access key  |
| **AWS_SECRET_ACCESS_KEY** | IAM secret key  |
| **AWS_DEFAULT_REGION** | e.g. `Asia Pacific(Mumbai)` |
| **AWS_ECR_REPO** | Optional: ECR repo for images  |

These can be stored locally in Jenkins Credentials or GitHub Secrets

### 4. Run the pipeline
Select one of the 3 build parameters given below:
- ```simulate``` -> runs everything locally and produces cost reports.

- ```azure``` -> triggers deploy_azure.py (ready for Azure ML / AKS integration).

- ```aws``` -> triggers deploy_aws.py (ready for SageMaker / ECS integration).

All generated reports will be saved under ```reports``` folder that is created after running.

---

## Summary
This project unifies automation, intelligence, and cost awareness, enabling engineers to deploy AI models efficiently across any cloud.
