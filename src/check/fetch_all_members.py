from src.services.member_service import get_members  # Import the function to get members

if __name__ == "__main__":
    members = get_members()  # Fetch all members
    print("Available Members:")
    for member in members:
        print(f"ID: {member['id']}, Name: {member['name']}")
