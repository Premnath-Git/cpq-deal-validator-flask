# CPQ Deal Validator – Backend Business Rule Engine

This is a Python-based backend project that simulates deal approval validations for a CPQ (Configure, Price, Quote) system, similar to workflows in enterprise platforms like SAP CPQ.

---

##  What It Does:

- Validates a list of deal records against key business rules:
  - Discount should not exceed 20%
  - Profit margin must be at least 10%
- Uses mock deal data (`sample_deals.json`) as input
- Prints clear validation results for each deal

---

##  Project Structure:

cpq-deal-validator/
├── data/ # Sample input deals (JSON format)
│ └── sample_deals.json
├── validators/ # Business validation rules
│ └── rules.py
├── utils/ # Helper functions (optional, reusable)
│ └── helpers.py
├── main.py # Main script to run validations
├── requirements.txt # Project dependencies
├── .gitignore # Git ignore settings
└── README.md # Project overview (this file)


---

##  How to Run:

```bash
# Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\Activate    # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the script
python main.py


Sample Output:

Validating Deal ID: 101
Deal is valid.

Validating Deal ID: 102
Invalid Deal:
 - Discount exceeds 20% limit
 - Profit margin below 10%


Skills Demonstrated:

Python scripting

JSON handling

Modular code organization

Business rule automation

Command-line tool design