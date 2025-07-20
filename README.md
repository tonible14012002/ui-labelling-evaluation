# API Proxy

The repository hosts the core source code for the API proxy for Google Geocode Services.

## Presiquite
- poetry
- python>=3.12,<4.0
- docker & docker-compose 
- make

## Quick start

```bash
git clone git@gitlab.com:...
cd api-proxy
poetry install
```

## Use with Pyenv and Virtualenv
```bash
pyenv virtualenv 3.12 <env-name>
pyenv activate <env-name>
poetry install
```

Then, you can rnu locally in development mode with live reload
```
make dev
```

Open [http://localhost:8000](http://localhost:8000) with your favorite browser to see your project.

## Technical Documentation

### Overview
This project is inspired by [clean architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) to that focus on maintaining **separation of concerns** and promoting dependency rules where inner layers (domain, core) must not depend on outer layers (frameworks, UI, databases) (`src/internal`).

### Code Organization
```
├── cmd                         # application entry points
│   └── server.py               # entrypoint for server
├── docker                      # Docker configurations
├── docs                        # Documentation
├── scripts                     # bash scripts
├── src                          
│   ├── config                  # Application configuration
│   │   ├── __init__.py
│   │   └── settings.py         # Settings and env
│   ├── core                    # Core business logic
│   │   ├── domain              # Define domain models
│   │   ├── ports               # Interface adapters for external services (ports)
│   │   └── services            # Application business services
│   └── internal                # Framework-specific code & external services implementation
│       ├── api                 # API layer
│       │   ├── dependencies    # FastAPI dependencies
│       │   ├── exceptions      # FastAPI exceptions
│       │   ├── requests        # API Request schema 
│       │   └── routes          # Route definitions
│       │       ├── v1          # API versioning
│       │       │   └── __init__.py
│       │       ├── __init__.py
│       ├── cache               # Cache implementations (redis)
│       ├── geocode             # geocode serverice implementation (google geocode API)
│       └── repository          # Repository implementation (postgres)
```

