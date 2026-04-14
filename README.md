# Proyecto Kubernetes - Aprendizaje

Arquitectura mínima para aprender Docker, Kubernetes y CI/CD.

## Ramas

| Rama | Descripción |
|---|---|
| `master` | Versión básica con imágenes locales |
| `cicd` | Versión profesional con GitHub Registry y GitHub Actions |

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

## Rama master — Imágenes locales

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

### 5. Verificar pods y servicios

kubectl get pods
kubectl get services

## Rama cicd — GitHub Registry y GitHub Actions

### 1. Configurar el secret en Kubernetes

kubectl create secret docker-registry ghcr-secret \
  --docker-server=ghcr.io \
  --docker-username=TU_USUARIO \
  --docker-password=TU_TOKEN

### 2. Desplegar en Kubernetes

export KUBECONFIG=~/.kube/config
cd k8s
kubectl apply -f .

### 3. El build es automático

Cada vez que hagas git push a la rama cicd, GitHub Actions
construirá las imágenes y las subirá a GitHub Registry
automáticamente.

### 4. Actualizar los pods

kubectl rollout restart deployment backend
kubectl rollout restart deployment frontend

## Acceder a los servicios desde Windows

Configurar reenvío de puertos en VirtualBox:

| Servicio | Puerto VM | Puerto Windows |
|---|---|---|
| Frontend | 31423 | 8080 |
| Backend | 31197 | 5000 |

- Frontend: http://127.0.0.1:8080
- Backend: http://127.0.0.1:5000/health
- Backend hello: http://127.0.0.1:5000/hello
