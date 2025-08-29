from flask import Blueprint, jsonify, request
import re

bajaj_bp = Blueprint('bajaj', __name__)

@bajaj_bp.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json
        if not data or 'data' not in data:
            return jsonify({"is_success": False, "error": "Invalid input"}), 400
        
        input_array = data['data']
        
        # Initialize arrays
        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        
        # Process each element
        for item in input_array:
            item_str = str(item)
            
            # Check if it's a number
            if item_str.isdigit():
                num = int(item_str)
                if num % 2 == 0:
                    even_numbers.append(item_str)
                else:
                    odd_numbers.append(item_str)
            # Check if it's alphabetic
            elif item_str.isalpha():
                alphabets.append(item_str.upper())
            # Otherwise it's a special character
            else:
                special_characters.append(item_str)
        
        # Calculate sum of all numbers
        total_sum = 0
        for item in input_array:
            item_str = str(item)
            if item_str.isdigit():
                total_sum += int(item_str)
        
        # Create concatenation string in reverse order with alternating caps
        concat_string = ""
        if alphabets:
            # Get all alphabetic characters from original input (preserve original case)
            alpha_chars = []
            for item in input_array:
                item_str = str(item)
                if item_str.isalpha():
                    alpha_chars.extend(list(item_str))
            
            # Reverse the order
            alpha_chars.reverse()
            
            # Apply alternating caps
            for i, char in enumerate(alpha_chars):
                if i % 2 == 0:
                    concat_string += char.upper()
                else:
                    concat_string += char.lower()
        
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Replace with actual user details
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }
        
        return jsonify(response), 200
        
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

@bajaj_bp.route('/bfhl', methods=['GET'])
def get_operation_code():
    """GET method to return operation code"""
    return jsonify({"operation_code": 1}), 200

