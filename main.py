import yaml
from pydantic import BaseModel, EmailStr, ValidationError
from datetime import date
from typing import Optional


# Definer Pydantic model baseret på din YAML-kontrakt
class Customer(BaseModel):
    customer_id: str
    name: str
    email: EmailStr
    signup_date: date


def load_contract(file_path):
    # Indlæs YAML filen
    with open(file_path, 'r') as file:
        contract = yaml.safe_load(file)
    return contract


def validate_data(customer_data):
    try:
        # Valider dataen mod Customer-modellen
        customer = Customer(**customer_data)
        print("Data er gyldig:", customer)
    except ValidationError as e:
        print("Validation Error:", e.json())


if __name__ == "__main__":
    # Indlæs YAML kontrakten (vi bruger den ikke til validering her, men kan udvides senere)
    contract = load_contract('customer.yaml')
    print("Indlæst kontrakt:", contract)

    # Eksempel data som skal valideres
    test_data = {
        'customer_id': '12345',
        'name': 'John Doe',
        'email': 'johndoe@example.com',  # Prøv at ændre email til en ugyldig email for at teste validering
        'signup_date': '2023-09-01'
    }

    # Valider testdata mod modellen
    validate_data(test_data)
