# catalog
# 📚 BookCatalog

A Django-based web application for browsing, searching, and managing a catalog of books. Built as part of a DevOps course, the project is fully containerised with Docker and orchestrated via Kubernetes, using PostgreSQL as its production database.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Environment Variables](#environment-variables)
  - [Run with Docker Compose](#run-with-docker-compose)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Database](#database)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

BookCatalog is a full-stack Django web application that allows users to browse, search, and perform full CRUD operations on a book collection. The project focuses on DevOps best practices, including containerisation, environment-based configuration, and Kubernetes-based deployment.

---

## Features

- Browse and search the book catalog
- Add, edit, and delete book entries (CRUD)
- Persistent storage with PostgreSQL
- Containerised with Docker and Docker Compose for local development
- Production-ready Kubernetes manifests for deployment

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.x / Django |
| Database | PostgreSQL |
| Containerisation | Docker / Docker Compose |
| Orchestration | Kubernetes (kubectl) |
| Web Server | Gunicorn (production) / Django dev server (local) |

---

## Project Structure

```
bookcatalog/
├── bookcatalog/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── catalog/              # Main Django app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── k8s/                  # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   └── postgres/
│       ├── deployment.yaml
│       └── pvc.yaml
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── manage.py
```

---

## Getting Started

### Prerequisites

Make sure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/) (for Kubernetes deployment)
- Python 3.10+ (for local development without Docker)

### Environment Variables

Create a `.env` file at the root of the project. Use `.env.example` as a reference:

```env
# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# PostgreSQL
POSTGRES_DB=bookcatalog
POSTGRES_USER=postgres
POSTGRES_PASSWORD=yourpassword
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

> **Note:** Never commit your `.env` file. It is listed in `.gitignore`.

### Run with Docker Compose

```bash
# 1. Clone the repository
git clone https://github.com/your-username/bookcatalog.git
cd bookcatalog

# 2. Build and start all services
docker compose up --build

# 3. In a separate terminal, run migrations
docker compose exec web python manage.py migrate

# 4. (Optional) Create a superuser for the Django admin
docker compose exec web python manage.py createsuperuser
```

The application will be available at [http://localhost:8000](http://localhost:8000).

---

## Kubernetes Deployment

All manifests are located in the `k8s/` directory.

```bash
# 1. Apply PostgreSQL resources first
kubectl apply -f k8s/postgres/

# 2. Apply the application resources
kubectl apply -f k8s/

# 3. Check that pods are running
kubectl get pods

# 4. Run migrations inside the web pod
kubectl exec -it <web-pod-name> -- python manage.py migrate
```

To access the application locally via Kubernetes:

```bash
kubectl port-forward service/bookcatalog-service 8000:80
```

Then open [http://localhost:8000](http://localhost:8000).

> **Tip:** If you are using Minikube, run `minikube service bookcatalog-service` instead.

---

## Database

The project uses **PostgreSQL** for both local (Docker Compose) and production (Kubernetes) environments.

The Django app connects to the database using the environment variables defined in `.env` or your Kubernetes `ConfigMap`/`Secret`.

To create the database tables:

```bash
python manage.py migrate
```

To load initial fixture data (if provided):

```bash
python manage.py loaddata catalog/fixtures/initial_books.json
```

---

## Usage

Once the application is running:

| URL | Description |
|---|---|
| `/` | Home page — browse the book catalog |
| `/books/` | Full list of books with search |
| `/books/<id>/` | Book detail view |
| `/books/add/` | Add a new book |
| `/books/<id>/edit/` | Edit an existing book |
| `/books/<id>/delete/` | Delete a book |
| `/admin/` | Django admin interface |

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

This project was created for educational purposes as part of a DevOps course. Feel free to use and adapt it for your own learning.
