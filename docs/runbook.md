# Runbook - EKS Autoscaling & Observability

## Cluster Operations

### Start Local Cluster

```bash
kind create cluster --config local/kind-config.yaml --name eks-portfolio
```

### Stop Local Cluster

```bash
kind delete cluster --name eks-portfolio
```

### Deploy Application

```bash
cd app
docker build -t my-app:latest .
kind load docker-image my-app:latest --name eks-portfolio

cd ../helm
helm install my-app ./my-app-chart
```

### Uninstall Application

```bash
helm uninstall my-app
```

## Monitoring

### Access Grafana

```bash
kubectl port-forward svc/grafana 3000:80
# Open: http://localhost:3000
```

### Access Prometheus

```bash
kubectl port-forward svc/prometheus 9090:80
# Open: http://localhost:9090
```

## Troubleshooting

### Pods Not Starting

```bash
kubectl get pods
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

### HPA Not Scaling

```bash
kubectl get hpa
kubectl describe hpa my-app
kubectl top pods
```

### Service Not Accessible

```bash
kubectl get svc
kubectl get endpoints
kubectl port-forward svc/my-app 8000:80
```

## Cost Optimization

- Use local development with kind for most work
- Only deploy to AWS EKS for final validation
- Delete EKS cluster immediately after testing
- Use t3.small instances for nodes

## AWS EKS Deployment

```bash
cd infra/terraform
terraform init
terraform plan
terraform apply

# After validation, delete to avoid costs:
terraform destroy
```
