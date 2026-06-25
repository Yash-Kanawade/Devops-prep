## Kubernetes Day 1 — June 20, 2025

### What I learned:
- Why Kubernetes exists: Docker doesn't auto-heal, scale, or manage multiple servers
- K8s architecture: Control Plane (API server, etcd, scheduler, controller manager)
  vs Worker Nodes (kubelet, kube-proxy, container runtime)
- Core objects: Pod, Deployment, Service, ConfigMap, Namespace
- The declarative mindset: YAML files declare desired state, K8s reconciles
- kubectl: apply, get, describe, logs, exec, delete, scale, port-forward
- minikube: local single-node K8s cluster for development
- Self-healing: deleted a pod manually, K8s recreated it automatically

### Commands I can use from memory:
- kubectl apply -f file.yaml
- kubectl get pods/deployments/services
- kubectl describe pod/deployment/service name
- kubectl logs podname
- kubectl exec -it podname -- /bin/bash
- kubectl scale deployment name --replicas=N
- kubectl port-forward pod/name 8000:8000
- minikube start/stop/status/dashboard

### The moment it clicked:
[Write: what was the "aha" moment today?]

### How this connects to ptc-monitor:
My /health endpoint is exactly what K8s livenessProbe will call tomorrow.