# Prometheus & Grafana Setup

## Installation (Local)

```bash
# Add Helm repositories
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

# Install Prometheus
helm install prometheus prometheus-community/prometheus \
  --namespace monitoring \
  --create-namespace

# Install Grafana
helm install grafana grafana/grafana \
  --namespace monitoring \
  --create-namespace \
  --set adminPassword=admin
```

## Access Dashboards

```bash
# Prometheus
kubectl port-forward svc/prometheus-server 9090:80 -n monitoring

# Grafana
kubectl port-forward svc/grafana 3000:80 -n monitoring
# Username: admin
# Password: admin
```

## Useful Dashboards

- Kubernetes Cluster
- Pod Metrics
- Node Metrics
- Application Metrics
