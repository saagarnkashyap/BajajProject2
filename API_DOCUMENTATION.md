# API Documentation

## Overview
This REST API processes arrays of mixed data types and returns categorized results. It's designed for the Bajaj Finserv Health Challenge.

## Authentication
No authentication required.

## Base URL
- Local: `http://localhost:5000`
- Production: `https://your-deployment-url.com`

## Endpoints

### POST /bfhl

**Description:** Processes an array of mixed data and returns categorized results.

**Headers:**
```
Content-Type: application/json
```

**Request Schema:**
```json
{
  "data": ["string", "number", "special_char", ...]
}
```

**Response Schema:**
```json
{
  "is_success": boolean,
  "user_id": "string",
  "email": "string", 
  "roll_number": "string",
  "odd_numbers": ["string"],
  "even_numbers": ["string"],
  "alphabets": ["string"],
  "special_characters": ["string"],
  "sum": "string",
  "concat_string": "string"
}
```

**Status Codes:**
- `200`: Success
- `400`: Bad Request (invalid input)
- `500`: Internal Server Error

### GET /bfhl

**Description:** Returns operation code for the API.

**Response:**
```json
{
  "operation_code": 1
}
```

## Data Processing Rules

1. **Numbers**: Classified as odd or even, returned as strings
2. **Alphabets**: Converted to uppercase
3. **Special Characters**: Non-alphanumeric characters
4. **Sum**: Total of all numeric values as string
5. **Concatenation**: Alphabetic characters in reverse order with alternating case

## Error Responses

**400 Bad Request:**
```json
{
  "is_success": false,
  "error": "Invalid input"
}
```

**500 Internal Server Error:**
```json
{
  "is_success": false,
  "error": "Error description"
}
```

## Rate Limiting
No rate limiting implemented.

## CORS
Cross-Origin Resource Sharing (CORS) is enabled for all origins.

