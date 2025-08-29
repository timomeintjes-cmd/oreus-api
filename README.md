# Oreus API

AI Service Orchestrator with Integrated Code Editor - Backend API Service

## Features

- **FastAPI Framework** with async support
- **Monaco Editor Integration** for web-based development
- **Project Management** with multiple templates (FastAPI, React, Node.js, Python)
- **Development Server Orchestration** for live preview
- **AWS Integration** (ECS, ECR, Secrets Manager)
- **Multi-AI Provider Support** (OpenAI, Anthropic, xAI)

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Visit the code editor
open http://localhost:8000/v1/editor
```

## API Endpoints

### Core API
- `GET /` - Root endpoint
- `GET /v1/health` - Health check for load balancers
- `GET /v1/config` - Configuration status
- `POST /v1/ai/completion` - AI service integration
- `GET /v1/providers` - Available AI providers

### Code Editor API
- `GET /v1/editor` - Web-based code editor interface
- `GET /v1/projects` - List all projects
- `POST /v1/projects` - Create new project
- `GET /v1/projects/{id}/files` - File tree
- `GET /v1/projects/{id}/files/{path}` - Get file content
- `PUT /v1/projects/{id}/files/{path}` - Save file
- `POST /v1/projects/{id}/dev-server` - Start development server
- `DELETE /v1/projects/{id}/dev-server` - Stop development server
- `POST /v1/projects/{id}/deploy` - Deploy to production

## Environment Variables

### Required
- `APP_ENV` - Environment (development, staging, production)
- `AWS_REGION` - AWS region
- `PROJECT_NAME` - Project identifier

### Optional
- `DATABASE_URL` - PostgreSQL connection string
- `REDIS_URL` - Redis connection string
- `SQS_URL` - SQS queue URL

### Secrets (AWS Secrets Manager)
- `OPENAI_API_KEY` - OpenAI API access
- `ANTHROPIC_API_KEY` - Anthropic Claude API access
- `XAI_API_KEY` - xAI Grok API access

## Project Templates

### FastAPI
Complete FastAPI starter with health checks and async support.

### React
Modern React 18 application with development server integration.

### Node.js
Express.js server with RESTful API structure.

### Python
Clean Python project structure with main entry point.

## Deployment

This API is designed to run on AWS ECS Fargate with:
- Application Load Balancer for HTTPS termination
- AWS Secrets Manager for secure API key storage
- CloudWatch for logging and monitoring
- Auto-scaling based on CPU/memory usage

## Development

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Code formatting
black main.py
isort main.py

# Type checking
mypy main.py
```

## Architecture

The Oreus API serves as the central orchestrator for:
1. **Code Editor Backend** - File management, project templates
2. **Development Server Management** - Live preview capabilities
3. **AI Service Integration** - Multi-provider AI completions
4. **Deployment Pipeline** - Production deployment automation
5. **AWS Service Integration** - ECS, ECR, Secrets Manager

Built with modern Python async patterns for high performance and scalability.