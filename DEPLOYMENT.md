# Deployment Guide

## Quick Deployment Steps

### 1. GitHub Setup
1. Create a new repository on GitHub
2. Upload all files from this project (excluding `venv/` folder)
3. Ensure `.gitignore` is included to prevent unnecessary files

### 2. Platform Deployment

#### Option A: Vercel
1. Connect your GitHub repository to Vercel
2. Set build command: `pip install -r requirements.txt`
3. Set start command: `python src/main.py`
4. Deploy

#### Option B: Railway
1. Connect GitHub repository to Railway
2. Railway will auto-detect Flask app
3. Set start command: `python src/main.py`
4. Deploy

#### Option C: Render
1. Create new Web Service on Render
2. Connect GitHub repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `python src/main.py`
5. Deploy

### 3. Configuration Updates

Before deployment, update these values in `src/routes/bajaj.py`:

```python
# Replace with your actual details
"user_id": "your_name_ddmmyyyy",  # e.g., "john_doe_17091999"
"email": "your_email@domain.com",
"roll_number": "YOUR_ROLL_NUMBER"
```

### 4. Testing Deployment

Once deployed, test your API:

```bash
curl -X POST https://your-deployment-url.com/bfhl \
  -H "Content-Type: application/json" \
  -d '{"data": ["a","1","334","4","R", "$"]}'
```

### 5. Form Submission

Submit your deployed API URL with `/bfhl` endpoint to:
https://forms.office.com/r/ZeVpUYp3zV

Example: `https://your-app.vercel.app/bfhl`

## Important Notes

- Ensure your API returns status code 200 for successful requests
- Numbers must be returned as strings in the response
- The `/bfhl` route must implement the exact logic specified
- Test all three example cases before submission

## Troubleshooting

### Common Issues:
1. **CORS errors**: Already handled with flask-cors
2. **Port binding**: App listens on 0.0.0.0 for external access
3. **Dependencies**: All requirements in requirements.txt

### Local Testing:
```bash
python test_api.py
```

This will verify your API works correctly before deployment.

