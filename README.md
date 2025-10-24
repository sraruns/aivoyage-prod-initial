# AI Voyage - FastAPI Deployment Guide

## Prerequisites
- Node.js installed
- Python virtual environment activated
- OpenAI API key

## Setup Commands

### 1. Install Vercel CLI globally
```bash
npm install -g vercel
```

### 2. Add npm to PATH (Windows PowerShell)
```powershell
$env:PATH += ";C:\Users\User\AppData\Roaming\npm"
```

### 3. Login to Vercel
```bash
vercel login
```

## Deployment Commands

### Deploy to Vercel (Development)
```bash
vercel .
```

### Deploy to Production
```bash
vercel --prod
```

### Run Development Server Locally
```bash
vercel --dev
```

## Environment Variables Management

### Add Environment Variables via CLI
```bash
vercel env add OPENAI_API_KEY
```

### List Environment Variables
```bash
vercel env ls
```

### Pull Environment Variables to Local
```bash
vercel env pull .env.local
```

## Environment Variables
Set the following environment variable in your Vercel dashboard:
- `OPENAI_API_KEY`: Your OpenAI API key from https://platform.openai.com/api-keys

## Local Development
```bash
# Activate virtual environment
.\prod-venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run locally
uvicorn initial:app --reload
```

