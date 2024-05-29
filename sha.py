import hashlib
import os

# File path to store message-to-hash mappings
file_path = "message_hashes.txt"

def compute_sha256(message):
    # Compute the SHA-256 hash of the message
    hash_object = hashlib.sha256(message.encode())
    return hash_object.hexdigest()

def save_message(message):
    # Compute the SHA-256 hash of the message
    hashed_message = compute_sha256(message)
    
    # Load existing message-to-hash mappings from the file
    message_hashes = load_message_hashes()
    
    if hashed_message in message_hashes:
        print("Message already exists in the database.")
    else:
        # Save the message-to-hash mapping to the file
        with open(file_path, 'a') as file:
            file.write(f"{hashed_message}:{message}\n")
        print("Message hashed and saved successfully.")

def load_message_hashes():
    # Initialize an empty dictionary for message-to-hash mappings
    message_hashes = {}
    
    # Check if the file exists
    if os.path.exists(file_path):
        # Load message-to-hash mappings from the file into the dictionary
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    hashed_message, message = line.split(':')
                    message_hashes[hashed_message] = message
    
    return message_hashes

def encode_message():
    user_input = input("Enter a message to hash and save: ")
    save_message(user_input)

def decode_hash():
    user_input = input("Enter a SHA-256 hash to verify: ").strip().lower()
    if len(user_input) != 64 or not all(c in '0123456789abcdef' for c in user_input):
        print("Invalid SHA-256 hash format.")
        return
    
    # Load existing message-to-hash mappings from the file
    message_hashes = load_message_hashes()
    
    # Check if the provided hash exists in the loaded mappings
    if user_input in message_hashes:
        original_message = message_hashes[user_input]
        print(f"Matching message found: {original_message}")
    else:
        print("No matching message found for the provided SHA-256 hash.")

# Ensure that the file is created if it doesn't exist
open(file_path, 'a').close()

# Main menu loop
while True:
    print("\nSelect an option:")
    print("1. Encode a message (generate SHA-256 hash and save)")
    print("2. Decode a SHA-256 hash (retrieve original message)")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        encode_message()
    elif choice == '2':
        decode_hash()
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
