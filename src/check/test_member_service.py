import pytest
from src.services.member_service import register_member, get_member_borrowings_count

def test_register_member():
    # Sample data for registration
    member_data = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "1234567890",
        "address": "123 Main St"
    }
    
    # Call the register_member function
    response = register_member(member_data)
    
    # Check if the response contains the expected fields
    assert "id" in response
    assert response["name"] == member_data["name"]
    assert response["email"] == member_data["email"]

def test_get_member_borrowings_count():
    # Assuming a member with ID 'some_member_id' exists
    member_id = 'some_member_id'  # Replace with an actual member ID for testing
    
    # Call the get_member_borrowings_count function
    count = get_member_borrowings_count(member_id)
    
    # Check if the count is an integer
    assert isinstance(count, int)
    # Optionally, check if the count is within expected limits
    assert count >= 0
