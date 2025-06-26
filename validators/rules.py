def validate_discount(deal):
    """Rule: Discount should not exceed 20%"""
    if deal["discount"] > 20:
        return False, "Discount exceeds 20% limit"
    return True, ""

def validate_margin(deal):
    """Rule: Profit margin should be at least 10%"""
    profit = deal["price"] - deal["cost"]
    margin = (profit / deal["price"]) * 100
    if margin < 10:
        return False, "Profit margin below 10%"
    return True, ""

def run_all_validations(deal):
    """Run all validation rules and collect errors"""
    validators = [validate_discount, validate_margin]
    errors = []
    for rule in validators:
        valid, message = rule(deal)
        if not valid:
            errors.append(message)
    return errors