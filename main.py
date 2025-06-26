import json
from validators.rules import run_all_validations

def load_deals(filepath):
    """Load deals from a JSON file"""
    with open(filepath, "r") as file:
        return json.load(file)

def validate_deals(deals):
    """Loop through each deal and run validations"""
    for deal in deals:
        print(f"\nValidating Deal ID: {deal['id']}")
        errors = run_all_validations(deal)
        if errors:
            print("Invalid Deal:")
            for error in errors:
                print(f" - {error}")
        else:
            print("Deal is valid.")

if __name__ == "__main__":
    deals = load_deals("data/sample_deals.json")
    validate_deals(deals)