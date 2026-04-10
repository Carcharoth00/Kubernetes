# Proyecto Kubernetes - Aprendizaje

## Servicios

| Servicio | Tecnología | Puerto |
|---|---|---|
| Backend | Python + Flask | 5000 |
| Frontend | Flutter Web + Nginx | 80 |
| n8n | Imagen oficial | 5678 |
| PostgreSQL | Imagen oficial | 5432 |

## Requisitos previos

- Ubuntu Server 22.04
- Docker instalado
- k3s instalado

## Pasos para levantar el proyecto

### 1. Clonar el repositorio

git clone https://github.com/Carcharoth00/Kubernetes.git
cd Kubernetes

### 2. Construir las imágenes Docker

cd backend
docker build -t backend:v1 .
cd ../frontend
docker build -t frontend:v1 .

### 3. Importar las imágenes a k3s

docker save backend:v1 | sudo k3s ctr images import -
docker save frontend:v1 | sudo k3s ctr images import -

### 4. Desplegar en Kubernetes

export KUBECONFIG=~/.kube/config
cd ../k8s
kubectl apply -f .

### 5. Verificar que los pods están corriendo

kubectl get pods

### 6. Acceder a los servicios

kubectl get services

Backend: http://localhost:PUERTO_BACKEND/health
Frontend: http://localhost:PUERTO_FRONTEND
