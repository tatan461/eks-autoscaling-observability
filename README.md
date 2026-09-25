<h1 align="center">Kubernetes Cluster on Amazon EKS with Autoscaling & Observability</h1>

<p align="center">
<a href="https://aws.amazon.com/eks/">
<img src="https://img.shields.io/badge/Cloud-AWS-232F3E?style=flat-square&logo=amazonaws&logoColor=FF9900" alt="AWS">
</a>
<a href="https://kubernetes.io/">
<img src="https://img.shields.io/badge/Orchestration-Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="Kubernetes">
</a>
<a href="https://www.docker.com/">
<img src="https://img.shields.io/badge/Container-Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker">
</a>
<a href="https://github.com/features/actions">
<img src="https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=flat-square&logo=github-actions&logoColor=white" alt="GitHub Actions">
</a>
<a href="https://www.terraform.io/">
<img src="https://img.shields.io/badge/IaC-Terraform-623CE4?style=flat-square&logo=terraform&logoColor=white" alt="Terraform">
</a>
<a href="https://prometheus.io/">
<img src="https://img.shields.io/badge/Monitoring-Prometheus-E6522C?style=flat-square&logo=prometheus&logoColor=white" alt="Prometheus">
</a>
<a href="https://grafana.com/">
<img src="https://img.shields.io/badge/Observability-Grafana-F46800?style=flat-square&logo=grafana&logoColor=white" alt="Grafana">
</a>
</p>

<p align="center">
<a href="#overview">Overview</a> •
<a href="#architecture">Architecture</a> •
<a href="#features">Features</a> •
<a href="#tech-stack">Tech Stack</a> •
<a href="#getting-started">Getting Started</a> •
<a href="#deployment">Deployment</a> •
<a href="#monitoring--observability">Monitoring</a> •
<a href="#testing-autoscaling">Testing</a> •
<a href="#cleanup">Cleanup</a> •
<a href="#lessons-learned">Lessons Learned</a>
</p>

Overview
Production-ready Kubernetes cluster on Amazon EKS with automated CI/CD, horizontal pod autoscaling, and full observability using Prometheus + Grafana.

The application deploys automatically on every push to main, with Docker image security scanning and real-time metrics dashboards.

Live Demo: [Add your LoadBalancer URL here]

Architecture
text
┌─────────────────────────────────────────────────────────────────┐
│                         AWS Cloud                                │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    Amazon EKS Cluster                     │   │
│  │                                                            │   │
│  │  ┌────────────────────────────────────────────────────┐   │   │
│  │  │                 Kubernetes Namespace                │   │   │
│  │  │                                                      │   │   │
│  │  │  ┌──────────────┐    ┌──────────────┐              │   │   │
│  │  │  │   Pod 1      │    │   Pod 2      │  ...         │   │   │
│  │  │  │  (my-app)    │    │  (my-app)    │              │   │   │
│  │  │  └──────────────┘    └──────────────┘              │   │   │
│  │  │         ▲                    ▲                      │   │   │
│  │  │         │                    │                      │   │   │
│  │  │         └────────────────────┘                      │   │   │
│  │  │              Horizontal Pod Autoscaler (HPA)        │   │   │
│  │  │              Target CPU: 50%                        │   │   │
│  │  └────────────────────────────────────────────────────┘   │   │
│  │                                                            │   │
│  │  ┌────────────────────────────────────────────────────┐   │   │
│  │  │              Monitoring Namespace                   │   │   │
│  │  │  ┌──────────────┐    ┌──────────────┐              │   │   │
│  │  │  │  Prometheus  │    │   Grafana    │              │   │   │
│  │  │  │   (Metrics)  │    │ (Dashboards) │              │   │   │
│  │  │  └──────────────┘    └──────────────┘              │   │   │
│  │  └────────────────────────────────────────────────────┘   │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌──────────────────┐    ┌──────────────────┐                  │
│  │   Amazon ECR     │    │  ALB / NLB       │                  │
│  │  (Docker Images) │    │  (LoadBalancer)  │                  │
│  └──────────────────┘    └──────────────────┘                  │
└─────────────────────────────────────────────────────────────────┘
                              ▲
                              │
┌─────────────────────────────┴─────────────────────────────┐
│                    GitHub Actions                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │
│  │    Build    │→ │    Scan     │→ │   Deploy    │       │
│  │   (Docker)  │  │  (Trivy)    │  │    (EKS)    │       │
│  └─────────────┘  └─────────────┘  └─────────────┘       │
└───────────────────────────────────────────────────────────┘
Features
✅ Automated CI/CD pipeline with GitHub Actions

✅ Docker image build and push to Amazon ECR

✅ Security scanning with Trivy on every build

✅ Automatic deployment to EKS on every push to main

✅ Horizontal Pod Autoscaler (HPA) based on CPU usage (50% target)

✅ Multiple replicas for high availability

✅ Public LoadBalancer for application access

✅ Metrics Server for real-time resource metrics

✅ Prometheus + Grafana for complete observability

✅ Infrastructure as Code with Terraform

Tech Stack
Category	Technologies
Cloud Provider	AWS (EKS, ECR, IAM, VPC)
Orchestration	Kubernetes, Helm
Containers	Docker
CI/CD	GitHub Actions
Infrastructure	Terraform
Monitoring	Prometheus, Grafana, Metrics Server
Security	Trivy (vulnerability scanning)
Application	Python (Flask)
Getting Started
Prerequisites
AWS CLI configured with credentials

kubectl installed and configured

Helm 3.x installed

Terraform 1.x installed

Docker installed (optional for local testing)

Repository Structure
text
eks-autoscaling-observability/
├── .github/
│   └── workflows/
│       └── ci-cd.yml              # CI/CD pipeline
├── app/
│   ├── Dockerfile                 # Application Docker image
│   ├── app.py                     # Python Flask application
│   └── requirements.txt           # Python dependencies
├── k8s/
│   ├── deployment.yaml            # Kubernetes Deployment
│   ├── service.yaml               # LoadBalancer Service
│   └── hpa.yaml                   # Horizontal Pod Autoscaler
├── terraform/
│   ├── main.tf                    # EKS Cluster + Node Group
│   ├── variables.tf               # Terraform variables
│   ├── outputs.tf                 # Cluster outputs
│   └── ecr.tf                     # ECR Repository
├── helm/
│   └── values.yaml                # Custom Helm values
├── docs/
│   └── images/
│       └── architecture.png       # Architecture diagram
├── README.md                      # This file
└── .gitignore
Deployment
1. Clone the repository
bash
git clone https://github.com/<your-username>/eks-autoscaling-observability.git
cd eks-autoscaling-observability
2. Deploy infrastructure with Terraform
bash
cd terraform

# Initialize Terraform
terraform init

# Plan deployment
terraform plan -out=tfplan

# Apply infrastructure (EKS + ECR)
terraform apply tfplan
Important outputs:

eks_cluster_name - EKS cluster name

ecr_repository_url - ECR repository URL

configure_kubectl - Command to configure kubectl

3. Configure kubectl
bash
# Run the command from Terraform output
aws eks update-kubeconfig --region <region> --name <cluster-name>

# Verify connection
kubectl get nodes
4. Deploy the application
bash
# Navigate to app directory
cd ../app

# Build and push Docker image
docker build -t <ecr-url>:latest .
docker push <ecr-url>:latest

# Apply Kubernetes manifests
kubectl apply -f ../k8s/

# Verify deployment
kubectl get pods
kubectl get svc
kubectl get hpa
5. Install Prometheus + Grafana
bash
# Add Prometheus repository
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# Install monitoring stack
helm install monitoring prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace \
  --set grafana.service.type=LoadBalancer

# Verify installation
kubectl get pods -n monitoring
6. Access Grafana
bash
# Get Grafana LoadBalancer URL
kubectl get svc -n monitoring monitoring-grafana \
  -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'

# Or use port-forward
kubectl port-forward svc/monitoring-grafana -n monitoring 8080:80
Credentials:

Username: admin

Password: prom-operator

Monitoring & Observability
Useful Commands
bash
# Check cluster status
kubectl get pods -A
kubectl get svc -A
kubectl get hpa

# View real-time metrics
kubectl top pods
kubectl top nodes

# View pod logs
kubectl logs <pod-name>
kubectl logs -f <pod-name>
Grafana Dashboards
Once inside Grafana, explore these pre-configured dashboards:

Kubernetes / Compute Resources / Cluster - Cluster overview

Kubernetes / Compute Resources / Node (Pods) - Per-node metrics

Kubernetes / Compute Resources / Pod - Per-pod metrics

Grafana / Stats - Grafana statistics

Access Prometheus
bash
kubectl port-forward svc/monitoring-kube-prometheus-prometheus -n monitoring 9090:9090
URL: http://localhost:9090

Testing Autoscaling
Generate Load
bash
# Install Apache Bench (if not already installed)
sudo apt-get install apache2-utils  # Linux
brew install httpd                  # macOS

# Generate load for 60 seconds
ab -n 10000 -c 100 http://<loadbalancer-url>/
Monitor Scaling
bash
# Watch HPA in real-time
watch kubectl get hpa my-app -n default

# Or monitor pods
watch kubectl get pods -l app=my-app
Cleanup
Remove monitoring stack
bash
helm uninstall monitoring --namespace monitoring
kubectl delete namespace monitoring
Remove application
bash
kubectl delete -f k8s/
Remove AWS infrastructure
bash
cd terraform
terraform destroy
⚠️ Important: Make sure to delete all resources to avoid unnecessary costs.

Lessons Learned
EKS is powerful but complex — Kubernetes adds significant operational overhead compared to ECS or serverless. For simple workloads, managed services are often more cost-effective.

HPA requires metrics — The Metrics Server must be installed and healthy before HPA can scale based on CPU/memory.

LoadBalancer security groups — AWS creates security groups automatically, but they may need manual adjustment for external access.

Prometheus resource consumption — The full kube-prometheus-stack is resource-intensive. For small clusters, consider lightweight alternatives or managed solutions like Amazon Managed Service for Prometheus.

Terraform state management — Always use remote state (S3 + DynamoDB) for production EKS clusters to prevent state file loss.

License
This project is licensed under the MIT License. See the LICENSE file for details.

<div align="center">

Found this project helpful? ⭐ Give it a star on GitHub

Author: Jhon



</div>

<p align="center">
<em>Portfolio project — Junior Cloud Engineer / AWS Solutions Architect Associate + AI Practitioner</em>
</p>