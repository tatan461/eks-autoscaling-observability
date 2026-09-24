# Kubernetes Cluster on Amazon EKS with Autoscaling & Observability

## Problem

Applications running on a single container platform cannot self-heal, scale under load, or provide visibility into cluster health.

## Solution

A containerized application deployed to Amazon EKS with Terraform, Horizontal Pod Autoscaling, Helm, Prometheus, and Grafana. Images are pushed to Amazon ECR through GitHub Actions with automated tests and vulnerability scanning before deployment.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     GitHub Actions CI/CD                     │
│  (Build → Test → Scan → Push to ECR → Deploy to EKS)        │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    Amazon EKS Cluster                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Kubernetes Pods (Auto-scaled)            │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌────────────┐  │   │
│  │  │   Pod 1      │  │   Pod 2      │  │   Pod N    │  │   │
│  │  │  (my-app)    │  │  (my-app)    │  │  (my-app)  │  │   │
│  │  └──────────────┘  └──────────────┘  └────────────┘  │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
│  ┌──────────────────┐  ┌─────────────────────────────────┐  │
│  │   Prometheus     │  │        Grafana                  │  │
│  │  (Metrics)       │  │   (Dashboards & Visualization)  │  │
│  └──────────────────┘  └─────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Stack

- **Container**: Docker
- **Orchestration**: Amazon EKS, Kubernetes
- **IaC**: Terraform
- **Package Manager**: Helm
- **Registry**: Amazon ECR
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus, Grafana
- **Autoscaling**: Horizontal Pod Autoscaler (HPA)

## Project Structure

```
eks-autoscaling-observability/
├── README.md
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── infra/
│   └── terraform/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
├── app/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── src/
│       └── main.py
├── helm/
│   └── my-app-chart/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           ├── deployment.yaml
│           ├── service.yaml
│           └── hpa.yaml
├── monitoring/
│   └── prometheus-grafana/
├── local/
│   └── kind-config.yaml
└── docs/
    └── runbook.md
```

## Quick Start (Local Development)

### Prerequisites

- Docker
- kind (Kubernetes in Docker)
- kubectl
- Helm

### Setup

```bash
# 1. Create kind cluster
kind create cluster --config local/kind-config.yaml --name eks-portfolio

# 2. Build Docker image
cd app
docker build -t my-app:latest .

# 3. Load image into kind
kind load docker-image my-app:latest --name eks-portfolio

# 4. Deploy with Helm
cd ../helm
helm install my-app ./my-app-chart

# 5. Test the application
kubectl port-forward svc/my-app 8000:80
# Open: http://localhost:8000/health
```

## AWS EKS Deployment (Final Validation)

For production-like validation, deploy to Amazon EKS using Terraform:

```bash
cd infra/terraform
terraform init
terraform plan
terraform apply
```

## Monitoring

Access Grafana dashboard:

```bash
kubectl port-forward svc/grafana 3000:80
# Open: http://localhost:3000
```

## Cost Optimization

This project is designed for portfolio use with minimal costs:

- **Local Development**: Free (kind, Docker, Helm)
- **AWS EKS**: Only for final validation (~$5-15 per session)
- **GitHub Actions**: Free for public repositories

## Lessons Learned

- [Add your lessons here]

## Author

Jhon - Junior Cloud Engineer Portfolio

## License

MIT
