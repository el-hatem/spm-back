# spm-back

Welcome to the **spm Backend**
------------------------------

## 📚 Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Tech Stack](#tech-stack)
* [Project Structure](#project-structure)
* [Getting Started](#getting-started)

  * [Environment Variables](#environment-variables)
  * [Docker Setup](#docker-setup)
  * [Manual Setup](#manual-setup)
* [Running Tests](#running-tests)
* [Management Commands](#management-commands)
* [Static & Media Files](#static--media-files)
* [Localization (i18n)](#localization-i18n)
* [Pre-commit Hooks & Code Quality](#pre-commit-hooks--code-quality)
* [Deployment](#deployment)
* [Changelog](#changelog)
* [License](#license)
* [Contributing](#contributing)
* [Contact](#contact)

---

## 📘 Project Overview

This repository provides the backend logic and APIs for the spm ecosystem. It is fully containerized using Docker and is designed for seamless development, testing, and deployment across environments (local, QA, production).

---

## ✨ Features

* 🔐 JWT-based user authentication and authorization
* 🧾 Multi-environment config support (local, QA, production)
* 📦 Modular Django app structure
* 🖼 Media and static file handling
* 🌍 Localization with `django-locale`
* 🧰 Pre-commit hooks with linting/formatting tools

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Framework:** Django 5.x, Django REST Framework
* **Containerization:** Docker, Docker Compose
* **Database:** PostgreSQL (via Docker)
* **Environment Management:** `.env`, `config/`
* **Dependency Management:** `pip`, `requirements/`, `pyproject.toml`

---

## 🗂 Project Structure

```
.
├── config/                          # Environment-specific Django settings
├── docker/                          # Docker build files and scripts
├── locale/                          # Translation and i18n files
├── media/                           # Uploaded user files
├── requirements/                    # Dev/Prod/Test dependencies
├── static/                          # Static files (CSS/JS/images)
├── staticfiles/                     # Files collected via collectstatic
├── spm/                           # Core Django app logic
├── .devcontainer/                   # VSCode remote dev container setup
├── .github/                         # GitHub Actions/Workflows
├── .pytest_cache/                   # Pytest cache
├── docker-compose-local.yml        # Local development compose file
├── docker-compose-qa.yml           # QA environment compose file
├── docker-compose-production.yml   # Production environment compose file
├── manage.py                        # Django management utility
├── .env.example                     # Environment variables template
├── .gitignore                       # Git ignore rules
├── .dockerignore                    # Docker ignore rules
├── .pre-commit-config.yaml          # Pre-commit hook configuration
├── README.md                        # This file
└── pyproject.toml / setup.cfg       # Python tool configuration
```

---

## 🛠️ Development

To set up a local development environment, follow these steps:

### Prerequisites

* Python 3.10+
* Docker & Docker Compose
* Git
* Make (optional for command shortcuts)

### Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/el-hatem/spm-back.git
   cd spm-back
   ```
2. **Build containers**:

   ```bash
   docker-compose -f docker-compose-local.yml build
   ```
3. **Run initial migrations (optional)**:

   ```bash
   docker-compose -f docker-compose-local.yml run django python manage.py makemigrations
   ```
4. **Create a superuser (optional)**:

   ```bash
   docker-compose -f docker-compose-local.yml run django python manage.py createsuperuser
   ```
5. **run containers**:

   ```bash
   docker-compose -f docker-compose-local.yml up
   ```
   
6. **Access the project**:

   * API root: [http://localhost:8000](http://localhost:8000)
   * Admin panel: [http://localhost:8000/admin/](http://localhost:8000/admin/)
   * swagger: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

---


## 📄 License

This project is licensed under the [MIT License](./LICENSE).

---

## 🤝 Contributing

We welcome contributions! You can contribute in several ways:

### 📂 Types of Contributions (Conventional Commits)

Use the following prefixes when making a commit:

* `feat:` – A new feature
* `fix:` – A bug fix
* `docs:` – Documentation only changes
* `style:` – Code style changes (formatting, missing semi-colons, etc.)
* `refactor:` – Code change that neither fixes a bug nor adds a feature
* `perf:` – Performance improvements
* `test:` – Adding or fixing tests
* `chore:` – Maintenance changes (build tasks, package manager configs, etc.)
* `ci:` – Changes to CI configuration files and scripts

### 🔹 Contribution Steps

1. **Fork** the repository.
2. Create your **feature branch**: `git checkout -b feat/your-feature`
3. Commit your changes using [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):

   ```bash
   git commit -m "feat: add login API endpoint"
   ```
4. **Push** to the branch: `git push origin feat/your-feature`
5. Create a **Pull Request**.

---
