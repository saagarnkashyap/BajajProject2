# Bajaj Finserv Health Challenge - REST API

A Flask-based REST API that processes arrays and returns categorized data including numbers, alphabets, and special characters with various transformations.

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd bajaj-assignment
   ```

2. **Set up virtual environment**
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python src/main.py
   ```

The API will be available at `http://localhost:5000`

## 📋 API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### POST /bfhl
Processes an array of mixed data types and returns categorized results.

**Request Body:**
```json
{
  "data": ["a", "1", "334", "4", "R", "$"]
}
```

**Response:**
```json
{
  "is_success": true,
  "user_id": "john_doe_17091999",
  "email": "john@xyz.com",
  "roll_number": "ABCD123",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

#### GET /bfhl
Returns the operation code for the API.

**Response:**
```json
{
  "operation_code": 1
}
```

## 🔧 API Logic

The API processes input data according to these rules:

1. **Number Classification**: Separates odd and even numbers (returned as strings)
2. **Alphabet Processing**: Converts all alphabetic characters to uppercase
3. **Special Characters**: Identifies non-alphanumeric characters
4. **Sum Calculation**: Adds all numeric values and returns as string
5. **String Concatenation**: Creates a string from alphabetic characters in reverse order with alternating case

### Processing Examples

#### Example 1
**Input:** `["a","1","334","4","R", "$"]`
- Odd numbers: `["1"]`
- Even numbers: `["334","4"]`
- Alphabets: `["A","R"]` (converted to uppercase)
- Special characters: `["$"]`
- Sum: `"339"` (1+334+4)
- Concat string: `"Ra"` (R-uppercase, a-lowercase, reversed)

#### Example 2
**Input:** `["2","a", "y", "4", "&", "-", "*", "5","92","b"]`
- Odd numbers: `["5"]`
- Even numbers: `["2","4","92"]`
- Alphabets: `["A", "Y", "B"]`
- Special characters: `["&", "-", "*"]`
- Sum: `"103"` (2+4+5+92)
- Concat string: `"ByA"` (b-uppercase, y-lowercase, a-uppercase, reversed)

#### Example 3
**Input:** `["A","ABcD","DOE"]`
- Odd numbers: `[]`
- Even numbers: `[]`
- Alphabets: `["A","ABCD","DOE"]`
- Special characters: `[]`
- Sum: `"0"`
- Concat string: `"EoDdCbAa"` (all characters reversed with alternating case)

## 🧪 Testing

Run the test script to verify API functionality:

```bash
python test_api.py
```

This will test all three example cases from the specification.

## 📁 Project Structure

```
bajaj-assignment/
├── src/
│   ├── models/
│   │   └── user.py          # Database models
│   ├── routes/
│   │   ├── user.py          # User-related routes
│   │   └── bajaj.py         # Main BFHL endpoint
│   ├── static/              # Frontend files
│   ├── database/
│   │   └── app.db          # SQLite database
│   └── main.py             # Application entry point
├── venv/                   # Virtual environment
├── requirements.txt        # Python dependencies
├── test_api.py            # API testing script
└── README.md              # This file
```

## 🌐 Deployment

The application is configured for deployment on platforms like:
- Vercel
- Railway
- Render
- Heroku

Key deployment features:
- CORS enabled for cross-origin requests
- Listens on `0.0.0.0` for external access
- Environment-ready configuration

## 🔑 Configuration

Update the following in `src/routes/bajaj.py` for your deployment:
- `user_id`: Format as `{full_name_ddmmyyyy}`
- `email`: Your email address
- `roll_number`: Your college roll number

## 📝 Response Format

All successful responses include:
- `is_success`: Boolean indicating operation status
- `user_id`: Formatted user identifier
- `email`: User email address
- `roll_number`: College roll number
- `odd_numbers`: Array of odd numbers as strings
- `even_numbers`: Array of even numbers as strings
- `alphabets`: Array of uppercase alphabetic characters
- `special_characters`: Array of special characters
- `sum`: Sum of all numbers as string
- `concat_string`: Concatenated alphabetic characters with alternating case

## 🚨 Error Handling

The API handles errors gracefully:
- Invalid JSON: Returns 400 with error message
- Missing data field: Returns 400 with error message
- Server errors: Returns 500 with error details

## 🛠️ Development

### Adding New Features
1. Create new route files in `src/routes/`
2. Register blueprints in `src/main.py`
3. Update requirements.txt if new dependencies are added

### Database Usage
The template includes SQLAlchemy setup for database operations if needed for future enhancements.

## 📄 License

This project is created for the Bajaj Finserv Health Challenge assignment.

---

**Author:** Manus AI  
**Created:** 2025  
**Version:** 1.0.0

