# CPQ Deal Validator

## Project Overview

This is a simple CPQ Deal Validator built using Python Flask. It validates deals data based on basic business rules like discount limits and profit margin requirements. Users can input deals data in JSON format through the web interface and view validation results immediately.

## Features

- Validate multiple deals at once
- Checks for:
  - Discount not exceeding 20%
  - Profit margin of at least 10%
- Displays validation results on the same page

## Technologies Used

- Python
- Flask
- HTML, CSS, JavaScript

## Setup Instructions

1. Clone this repository

git clone https://github.com/Premnath-Git/cpq-deal-validator.git
cd cpq-deal-validator

2. Install dependencies

pip install flask

3. Run the Flask app

python app.py

4. Open your browser and go to http://localhost:5000

## Sample Input

[
{"id": 1, "price": 100, "cost": 80, "discount": 10},
{"id": 2, "price": 150, "cost": 145, "discount": 25}
]

## Output

[
  {
    "deal_id": 1,
    "status": "Valid"
  },
  {
    "deal_id": 2,
    "status": "Invalid",
    "errors": [
      "Discount exceeds 20% limit",
      "Profit margin below 10%"
    ]
  }
]
