# Professional ISMS & QMS Assistant

A professional web application designed to help employees with Information Security Management System (ISMS) and Quality Management System (QMS) queries.

## Features

- **No Authentication Required**: Direct access for all employees
- **ISMS Support**: Information security policies, procedures, and best practices
- **QMS Support**: Quality management standards including ISO 9001
- **Risk Assessment**: Security and quality risk evaluation guidance
- **Compliance**: Regulatory and audit requirements assistance
- **Professional UI**: Clean, modern interface optimized for workplace use

## Quick Start

### Using Docker Compose (Recommended)
```bash
docker-compose up --build
```

### Manual Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python isms_qms_server.py
```

The application will be available at `http://localhost:5199`

## Configuration

Update the `FLOWISE_API_URL` in `isms_qms_server.py` to point to your ISMS/QMS knowledge base API endpoint.

## Usage

1. Open the application in your web browser
2. Use the suggestion cards for common queries or type your own question
3. Get instant answers about ISMS and QMS topics
4. No login required - designed for easy employee access

## Key Topics Covered

- **ISMS Policies**: Information security policies and procedures
- **QMS Standards**: ISO 9001 and quality management guidelines  
- **Risk Assessment**: Security and quality risk evaluation methods
- **Compliance**: Regulatory requirements and audit preparation

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript, Tailwind CSS
- **Containerization**: Docker & Docker Compose
- **API Integration**: Flowise/LangChain compatible# ISMS-BOT
