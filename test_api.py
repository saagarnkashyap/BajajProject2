#!/usr/bin/env python3
import requests
import json

def test_bfhl_endpoint():
    url = "http://localhost:5000/bfhl"
    
    # Test case 1 from the examples
    test_data_1 = {"data": ["a","1","334","4","R", "$"]}
    
    try:
        response = requests.post(url, json=test_data_1)
        print("Test 1 Response:")
        print(json.dumps(response.json(), indent=2))
        print(f"Status Code: {response.status_code}")
        print("-" * 50)
        
        # Test case 2
        test_data_2 = {"data": ["2","a", "y", "4", "&", "-", "*", "5","92","b"]}
        response = requests.post(url, json=test_data_2)
        print("Test 2 Response:")
        print(json.dumps(response.json(), indent=2))
        print(f"Status Code: {response.status_code}")
        print("-" * 50)
        
        # Test case 3
        test_data_3 = {"data": ["A","ABcD","DOE"]}
        response = requests.post(url, json=test_data_3)
        print("Test 3 Response:")
        print(json.dumps(response.json(), indent=2))
        print(f"Status Code: {response.status_code}")
        
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Make sure Flask is running on localhost:5000")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_bfhl_endpoint()

