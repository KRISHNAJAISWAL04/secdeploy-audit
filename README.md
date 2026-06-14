# 🛡️ SecDeploy-Audit

A lightweight, automated Python-based security auditing utility designed to scan local repository structures for exposed sensitive secrets and configuration mismatches. 

Built specifically for modern **DevSecOps** and **Cloud Infrastructure Protection** workflows.

## 🚀 Key Automation Features
*   **Secret Detection**: Automatically crawls directory architectures to flags loose, high-risk security files (like unprotected `.env`, `config.json`, or SSH credentials).
*   **Permission Enforcement**: Validates environment directory write-privileges against standard security configuration baselines.
*   **DevOps Ready**: Pre-packaged inside a multi-stage, containerized secure Linux image execution pipeline.

## 🛠️ Quick Infrastructure Setup

### Prerequisites
Make sure your system configuration has the Docker core architecture active:
```bash
docker --version
```

### 1. Container Image Building
To compile and build the secure automation container scanner locally, execute:
```bash
docker build -t secdeploy-audit:latest .
```

### 2. Execution & Local Verification
To execute the sandboxed Python auditing logic inside the secure container scope, run:
```bash
docker run --rm secdeploy-audit:latest
```

## 🤝 Open Source Contributions
This is a fully transparent, open-source community layout. We welcome contributions to enhance scanning parameters! 

If you want to support this project, feel free to clone, open a bug ticket under the **Issues** dashboard, or submit an upstream **Pull Request**.

## 📄 Licensing
Distributed under the **MIT License**. Feel free to fork, optimize, and share!
