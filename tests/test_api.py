import requests
import json

# Replace with your actual API Gateway URL
API_BASE_URL = "https://your-api-url.execute-api.us-east-1.amazonaws.com/prod"

def test_get_balance():
    """Test balance inquiry endpoint"""
    response = requests.get(f"{API_BASE_URL}/balance/test123")
    print(f"Balance Response: {response.status_code}")
    print(f"Body: {response.json()}")
    return response.status_code == 200

def test_credit_transaction():
    """Test credit transaction"""
    payload = {
        "accountId": "test123",
        "amount": 100,
        "type": "credit"
    }
    response = requests.post(f"{API_BASE_URL}/transaction", 
                           json=payload,
                           headers={"Content-Type": "application/json"})
    print(f"Credit Response: {response.status_code}")
    print(f"Body: {response.json()}")
    return response.status_code == 200

def test_debit_transaction():
    """Test debit transaction"""
    payload = {
        "accountId": "test123", 
        "amount": 50,
        "type": "debit"
    }
    response = requests.post(f"{API_BASE_URL}/transaction",
                           json=payload, 
                           headers={"Content-Type": "application/json"})
    print(f"Debit Response: {response.status_code}")
    print(f"Body: {response.json()}")
    return response.status_code == 200

if __name__ == "__main__":
    print("Testing Banking API...")
    print("1. Testing balance inquiry...")
    test_get_balance()
    print("\n2. Testing credit transaction...")
    test_credit_transaction()
    print("\n3. Testing debit transaction...")
    test_debit_transaction()
